import VueRouter from 'vue-router'

import AuthGuard from './auth-guard.js'

import NoteEditor from '../pages/NoteEditor/NoteEditor.vue'
import Login from '../pages/Auth/Login.vue'
import Registration from '../pages/Auth/Registration.vue'

export default new VueRouter({
    routes: [
        {
            path: '/',
            component: NoteEditor,
            beforeEnter: AuthGuard
        },
        {
            path: '/login',
            component: Login,
        },
        {
            path: '/registration',
            component: Registration,
        }
    ],
    mode: 'history'
})