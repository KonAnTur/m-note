import Vue from 'vue'
import VueResource from 'vue-resource'
Vue.use(VueResource)

export default {
    state: {
        token: localStorage.getItem('Authorization') || null
    },
    getters: {
        isUserLoggedIn (state) {
            return state.token !== null
        }
    },
    mutations: {
        tokenUser(state, token){
            localStorage.setItem('Authorization', token);
            state.token = localStorage.getItem('Authorization') || null
            Vue.http.interceptors.push(request => {
                request.headers.set('Authorization', 'Token ' + token)
            })
        },
        deleteTokenUser(state){
            localStorage.removeItem('Authorization')
            state.token = null
        }
    },
    actions: {
        async registerUser({commit}, {username, email, password}){
            commit('clearError')
            commit('setLoading', true)
            try {
                //const user = 
                await Vue.http.post('/api/users/', {username, email, password})
                commit('setLoading', false)
            } catch(error) {
                commit('setLoading', false)
                commit('setError', error.message)
                throw error
            }
        },
        async loginUser({commit}, {username, email, password}) {
            commit('clearError')
            commit('setLoading', true)
            try {
                const user = await Vue.http.post('/api/login/', {username, email, password})
                commit('tokenUser', user.body.token)
                commit('setLoading', false)
            } catch(error) {
                localStorage.removeItem('Authorization')
                commit('setLoading', false)
                commit('setError', error.message)
                throw error
            }
        },
        autoLoginUser ({commit}, token) {
            commit('tokenUser', token)
        },
        logoutUser({commit}) {
            commit('deleteTokenUser')
        }
    }
}