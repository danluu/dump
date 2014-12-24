import json
import itertools

def normalize(text):
  return (" ".join(text.split())).lower()

class WebUI:
  def __init__(self, client):
    self.player = None
    self.client = client
    self.next_id = 1
    self.play_mode = None
    self.autoplay = {}

  def WithId(self, cmd):
    d = { "id": self.next_id, "command": cmd }
    self.next_id += 1
    return d

  def Say(self, msg):
    self.client.Say(msg)

  def Choose(self, prompt, choices, min=0, max=10000, repeat=False):
    d = self.WithId("choose")
    d["prompt"] = prompt
    d["choices"] = list(choices)
    d["min"] = min
    d["max"] = max
    d["repeat"] = repeat
    self.client.SendMessage(d)
    r = self.client.AwaitResponse(d["id"])
    print("raw answer is", r)
    return r["answer"]

  def PickOne(self, prompt, choices, aliases=None):
    while True:
      answer = self.Choose(prompt, choices, min=1, max=1)
      if len(answer) == 1:
        answer = answer[0].lower()
        if aliases:
          answer = aliases.get(answer, answer)
        if answer in choices:
          return answer
      self.Say("Didn't understand that answer.")

  def AskYesNo(self, prompt):
    yn = self.PickOne(prompt, ("yes", "no"), aliases={"y": "yes", "n": "no"})
    return yn == "yes"









