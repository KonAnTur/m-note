import Vue from 'vue'
import Vuex from 'vuex'

import VueResource from 'vue-resource'
Vue.use(VueResource)

import user from './user.js'
import notes from './notes.js'
import shared from './shared.js'

Vue.use(Vuex)

export default new Vuex.Store({
    modules: {
        notes,
        user,
        shared
    }
})