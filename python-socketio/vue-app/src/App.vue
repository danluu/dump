<template>
  <div>
    <p v-if="isConnected">We're connected to the server!</p>
    <p v-if="username == null"><input v-model="input_username" @keyup.enter="sendUsername()" placeholder="username required"></p>
    <p v-else>username: {{input_username}}</p>
    <p v-if="gamename == null && username != null"><input v-model="input_gamename" @keyup.enter="sendGamename()" placeholder="enter game name"></p>
    <p v-else>gamename: {{input_gamename}}</p>
    <p>Message from server: "{{socketMessage}}"</p>
    <button @click="pingServer()">Ping Server</button>
    <button @click="sendMessage()">Send Message</button>
  </div>
</template>

<script>
export default {
  name: 'app',
  data() {
    return {
      isConnected: false,
      username: null,
      gamename: null,
      socketMessage: '',
    };
  },

  props:
  ['input_username',
    'input_gamename'],

  sockets: {
    connect() {
      // Fired when the socket connects.
      this.isConnected = true;
    },

    disconnect() {
      this.isConnected = false;
    },

    // Fired when the server sends something on the "messageChannel" channel.
    messageChannel(data) {
      this.socketMessage = data;
    },
  },

  methods: {
    sendUsername() {
      this.username = this.input_username;
      this.$socket.emit('username', this.username);
    },

    sendGamename() {
      this.gamename = this.input_gamename;
      this.$socket.emit('gamename', this.gamename);
    },

    pingServer() {
      // Send the "pingServer" event to the server.
      this.$socket.emit('pingServer', 'PING!');
    },
    sendMessage() {
      this.$socket.send('hello this is a message');
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
