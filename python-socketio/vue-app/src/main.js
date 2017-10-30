// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import App from './App'
import router from './router'
import socketio from 'socket.io-client/dist/socket.io'
import Vue from 'vue'
import VueSocketIO from 'vue-socket.io'

export const SocketInstance = socketio('http://localhost:4113')

Vue.use(VueSocketIO, SocketInstance)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
