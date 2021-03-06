import Vue from 'vue'
import VueResource from 'vue-resource'

import { apiHost } from '../config.js'

Vue.use(VueResource)

export default {
    state: {
        token: localStorage.getItem('Authorization') || null,
        username: localStorage.getItem('UserName') || null
    },
    getters: {
        isUserLoggedIn(state) {
            return state.token !== null
        },
        userName(state) {
            return state.username
        }
    },
    mutations: {
        tokenUser(state, token){
            localStorage.setItem('Authorization', token)
            state.token = localStorage.getItem('Authorization') || null  
            Vue.http.interceptors.push(request => {
                if(state.token !== null) {
                    request.headers.set('Authorization', 'Token ' + state.token)
                }
            })
        },
        nameUser(state, username) {
            localStorage.setItem('UserName', username);
            state.username = localStorage.getItem('UserName') || null
        },
        deleteTokenAndUser(state){
            localStorage.removeItem('Authorization')
            localStorage.removeItem('UserName')
            localStorage.removeItem('startNote')
            state.token = null
            state.username = null
        }
    },
    actions: {
        async registerUser({commit}, {username, email, password}){
            commit('clearError')
            commit('setLoading', true)
            try {
                await Vue.http.post(apiHost + '/api/users/registration/', {username, email, password})
                commit('setLoading', false)
            } catch(error) {
                commit('setLoading', false)
                if(error.body.email) {
                    commit('setError', error.body.email[0])
                } else if(error.body.username) {
                    commit('setError', error.body.username[0])
                } else if(error.body) {
                    commit('setError', error.body)
                }
                throw error
            }
        },
        async loginUser({commit}, {username, email, password}) {
            commit('clearError')
            commit('setLoading', true)
            try {
                const user = await Vue.http.post(apiHost + '/api/users/authorization/', 
                                                           {username, email, password})
                commit('tokenUser', user.body.token)
                commit('nameUser', user.body.username)
                commit('setLoading', false)
            } catch(error) {
                localStorage.removeItem('Authorization')
                localStorage.removeItem('UserName')
                commit('setLoading', false)
                commit('setError', error.body.error)
                throw error
            }
        },
        autoLoginUser ({commit}, token) {
            commit('tokenUser', token)
        },
        logoutUser({commit}) {
            commit('deleteTokenAndUser')
        }
    }
}
