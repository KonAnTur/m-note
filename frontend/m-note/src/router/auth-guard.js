import store from '../store/index.js'

export default function(to, from, next) {
    if(store.getters.isUserLoggedIn) {
        next()
    } else {
        next('/login')
    }
}