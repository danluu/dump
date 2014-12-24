goog.require('goog.net.XhrIo');
goog.require('goog.json.Serializer');

function log(message) {
    var new_span = document.createElement('span');
    new_span.innerHTML = message;
    document.getElementById('log').appendChild(new_span);
    document.getElementById('log').appendChild(document.createElement('br'));
}

var client_id = null;
var waiter = null;

function MakeChoice(id, answer) {
    var el = document.getElementById('ch_' + id);
    document.getElementById('choices').removeChild(el);

    s = new goog.json.Serializer();
    thing = {
	id: id,
	answer: [answer],
    };
    txt = s.serialize(thing);
    goog.net.XhrIo.send("/reply/" + client_id, function(){}, "POST", txt);
}

function BindMakeChoice(id, answer) {
    return function() { MakeChoice(id, answer); };
}

function Dispatch() {
    this.say = function(json) {
	log(json.message);
    }
    this.choose = function(json) {
	var item = document.createElement('div');
	item.id = "ch_" + json.id;

	var new_span = document.createElement('span');
	new_span.innerHTML = json.prompt;
	item.appendChild(new_span);

	for (c in json.choices) {
	    var text = json.choices[c];
	    var a = document.createElement('a');
	    a.className = "choice";
	    a.onclick = BindMakeChoice(json.id, text);
	    a.innerHTML = text;
	    item.appendChild(a);
	}

	document.getElementById('choices').appendChild(item);
    }
}

function Waiter(id) {
    this.id = id;
    this.xhr = new goog.net.XhrIo();
    this.other_xhr = new goog.net.XhrIo();
    this.dispatch = new Dispatch();
    this.count = 0;
    this.waitcomplete = function() {
	var json = this.xhr.getResponseJson();
	var command = json.command;

	var fn = this.dispatch[json.command];
	if (fn != undefined) {
	    fn(json);
	}

	this.count++;
	var temp = this.xhr;
	this.xhr = this.other_xhr;
	this.other_xhr = temp;

	this.xhr.send("/wait/" + this.count + "/" + this.id);
    };
    goog.events.listen(this.xhr, goog.net.EventType.COMPLETE, this.waitcomplete, false, this);
    goog.events.listen(this.other_xhr, goog.net.EventType.COMPLETE, this.waitcomplete, false, this);
    this.xhr.send("/wait/" + this.count + "/" + this.id);
}

function register(name) {
    var xhr = new goog.net.XhrIo();

    goog.events.listen(xhr, goog.net.EventType.COMPLETE, function() {
	    client_id = this.getResponseText();
	    waiter = new Waiter(client_id);
	});

    s = new goog.json.Serializer();
    thing = new Object();
    thing.name = name;
    txt = s.serialize(thing);

    xhr.send("/", "POST", txt);
}
