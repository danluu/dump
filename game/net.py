import sys

if sys.hexversion < 0x03000000:
  print("Need python 3.0 or higher")
  sys.exit(1)

import socketserver
import http.server
import json
import threading
import queue

import ui

class Client:
  CV = threading.Condition()
  BY_ID = {}
  UNATTACHED = []

  def __init__(self, id, name):
    self.id = id
    self.name = name
    self.q = queue.Queue(0)
    self.rcv = threading.Condition()
    self.r = {}
    self.receiver = None

    with Client.CV:
      Client.BY_ID[id] = self
      Client.UNATTACHED.append(self)
      Client.CV.notify_all()

  def BlockingGet(self):
    return self.q.get(True)

  def Say(self, msg):
    d = { "command": "say", "message": msg }
    self.SendMessage(d)

  def UpdateGameState(self, items):
    items["command"] = "game_state"
    print("sending", items)
    self.SendMessage(items)

  def SendMessage(self, item):
    self.q.put(json.dumps(item).encode())

  def PostResponse(self, data):
    item = json.loads(data.decode())
    print("item is {0}".format(item))
    id = item.get("id", None)
    if not id: return
    with self.rcv:
      self.r[id] = item
      self.rcv.notify_all()

  def AwaitResponse(self, id, timeout=None):
    """Wait for response 'id' to be posted and return it.  Returns
    None on timeout."""
    with self.rcv:
      while id not in self.r:
        self.rcv.wait(timeout=timeout)
      return self.r.pop(id, None)

  def HandleRequest(self, request):
    if not self.receiver:
      return None
    return self.receiver.HandleRequest(request).encode()


class MyHandler(http.server.BaseHTTPRequestHandler):
  def address_string(self):
    return self.client_address[0]

  def do_GET(self):
    print("path is " + self.path)

    if self.path.startswith("/wait/"):
      id = int(self.path.split("/")[-1])

      with Client.CV:
        c = Client.BY_ID.get(id)

      if not c:
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"No such client id.\n")
      else:
        item = c.BlockingGet()
        print("sending item {0}".format(item))
        self.send_response(200)
        self.end_headers()
        self.wfile.write(item)

    elif self.path.startswith("/request/"):
      request, id = self.path.split("/")[-2:]
      id = int(id)

      with Client.CV:
        c = Client.BY_ID.get(id)

      if not c:
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"No such client id.\n")
      else:
        self.send_response(200)
        self.end_headers()
        self.wfile.write(c.HandleRequest(request))

    elif self.path.startswith("/client"):
      path = self.path.lstrip("/")
      print(path)
      ext = path.split(".")[-1]
      mimetype = { "css": "text/css",
                   "html": "text/html",
                   "js": "text/javascript" }
      data = open(path, "rb").read()
      self.send_response(200)
      self.send_header("Content-type", mimetype.get(ext, "text/plain"))
      self.end_headers()
      self.wfile.write(data)


  def do_POST(self):
    if self.path == "/":
      length = int(self.headers["Content-length"])
      data = self.rfile.read(length)
      info = json.loads(data.decode())
      name = info.get("name", "mudd")

      # new client
      with self.server.lock:
        id = self.server.next_id
        self.server.next_id += 1

      c = Client(id, name)

      self.send_response(200)
      self.send_header("Content-type", "text/plain")
      self.end_headers()
      self.wfile.write(str(id).encode())

    elif self.path.startswith("/reply/"):
      id = int(self.path.split("/")[-1])

      with Client.CV:
        c = Client.BY_ID.get(id)

      if not c:
        self.send_response(404)
        self.end_headers()
        self.wfile.write(b"No such client id.\n")
      else:
        length = int(self.headers["Content-length"])
        data = self.rfile.read(length)
        c.PostResponse(data)
        self.send_response(200)
        self.end_headers()

class Server(socketserver.ThreadingMixIn, http.server.HTTPServer):
  daemon_threads = True
  lock = threading.Lock()
  allow_reuse_address = True
  next_id = 1


def run_server():
  HOST, PORT = "", 9999
  server = Server((HOST, PORT), MyHandler)
  server.serve_forever()

def main():
  th = threading.Thread(target=run_server)
  th.start()

  while True:
    with Client.CV:
      while len(Client.UNATTACHED) < int(sys.argv[1]):
        print("unattached is", Client.UNATTACHED)
        Client.CV.wait()
      clients = Client.UNATTACHED
      Client.UNATTACHED = []

    print("starting game with", clients)

    # here we would start the game.

    players = [ui.WebUI(c) for c in clients]

    for i, p in enumerate(players):
      p.Say("hello, player {0}".format(i+1))
    likes_ice_cream = players[0].AskYesNo("do you like ice cream? ")
    for p in players:
      p.Say("player 1 likes ice cream: " + ("yes" if likes_ice_cream else "no"))
    if likes_ice_cream:
      flavor = players[1 % len(players)].PickOne("what flavor> ", ("chocolate", "vanilla", "strawberry"))
      for p in players:
        p.Say("yum, " + flavor)
    for p in players:
      p.Say("game over")


if __name__ == "__main__":
  main()


