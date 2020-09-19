import Vue from 'vue'
import VueResource from 'vue-resource'
Vue.use(VueResource)

import { apiHost } from '../config.js'

export default {
    state: {
        notes: [],
    },
    getters: {
        notes(state) {
            return state.notes
        },
        noteById (state) {
            return noteId => {
              return state.notes.find(note => note.id === noteId)
            }
          }
    },
    mutations: {
        viewNotes(state, notes) {
            state.notes = notes
        },
        saveNote(state, note) {
            state.notes[state.notes.map(function(e) { return e.id; }).indexOf(note.id)].body = note.body
            state.notes[state.notes.map(function(e) { return e.id; }).indexOf(note.id)].title = note.title
        },
        createNote(state, newNote) {
            state.notes.push(newNote)
        },
        deleteNote(state, id) {
            const index = state.notes.map(function(e) { return e.id; }).indexOf(id)
            state.notes.splice(index, 1);
        }
    },
    actions: {
        async viewNotes({commit}){
            try {
                const notes = await Vue.http.get(apiHost + '/api/notes/')
                commit('viewNotes', notes.body)
            } catch(error) {
                console.log(error)
                throw error
            }
        },
        async saveNote({commit}, note){
            try {
                await Vue.http.put(apiHost + '/api/notes/' + note.id + '/', note)
                commit('saveNote', note)
            } catch(error) {
                console.log(error)
                throw error
            }
        },
        async createNote({commit}, note){
            try {
                const newNote = await Vue.http.post(apiHost + '/api/notes/', note)
                console.log(newNote)
                commit('createNote', newNote.body)
            } catch(error) {
                console.log(error)
                throw error
            }
        },
        async deleteNote({commit}, id){
            try {
                await Vue.http.delete(apiHost + '/api/notes/' + id + '/')
                commit('deleteNote', id)
            } catch(error) {
                console.log(error)
                throw error
            }
        },
    }
}