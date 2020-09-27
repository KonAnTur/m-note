import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import vClickOutside from 'v-click-outside'

import App from './App.vue'
import vuetify from './plugins/vuetify';
import store from './store/index.js'
import router from './router/routes.js'

import Editor from 'vue-editor-js'
 
Vue.use(Editor)
Vue.use(VueRouter)
Vue.use(VueResource)
Vue.use(vClickOutside)

Vue.config.productionTip = false

Vue.http.options.root = 'http://localhost:3000/'

new Vue({
  vuetify,
  store,
  render: h => h(App),
  router,
  created () {
    const token = localStorage.getItem('Authorization')
    if(token) {
      this.$store.dispatch('autoLoginUser', token)
    }
  }
}).$mount('#app')
