import VueRouter from 'vue-router'

import AuthGuard from './auth-guard.js'

import NoteEditor from '../components/NoteEditor/NoteEditor.vue'
import Login from '../components/Auth/Login.vue'
import Registration from '../components/Auth/Registration.vue'

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