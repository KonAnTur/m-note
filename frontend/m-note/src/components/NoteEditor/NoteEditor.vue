<template>
  <div id="app">
    <v-navigation-drawer v-model="drawer" class="menu" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            {{ userName }}
          </v-list-item-title>
          <v-list-item-subtitle>
            <button @click="logout">logout</button>
          </v-list-item-subtitle>
          
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense nav>
        <v-list-item 
          v-for="note in notes"
          :key="note.id"
          class="link-note"
        >
          <v-list-item-content @click="noteShow(note.id)">
            <v-list-item-title>{{ showNoteTitle(note.title) }}</v-list-item-title>
          </v-list-item-content>
          <v-list-item-action>
            <delete-note-button :deleteNoteId="note.id" @deleted-note="deletedNote($event)"></delete-note-button>
          </v-list-item-action>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <div class="menu-btn" fixed>
        <v-speed-dial fixed class="btn-group">
          <template v-slot:activator>
            <v-btn tile icon color="indigo" class="crud-btn" @click="drawer = !drawer">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn tile icon color="indigo" class="crud-btn" @click="createNote">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
          </template>
        </v-speed-dial>
      </div>
      <v-col cols="10" xs="2" sm="6" class="col-in">
        <v-text-field
          v-if="!overlay"
          class="note-title"
          v-model="noteTitle"
          placeholder="Untitled"
          @change="onChange"
          single-line
        ></v-text-field>
      </v-col>
      <v-col cols="12" class="col-in">
        <editor v-if="!overlay" autofocus header list code inlineCode embed marker table raw delimiter quote paragraph checklist ref="editor" holder-id="codex-editor" :init-data="initData" @save="save" @ready="onReady" @change="onChange" />
      </v-col>
      <div class="text-center">
        <v-overlay :value="overlay" z-index="5">
        </v-overlay>
      </div>
    </v-main>
  </div>
</template>

<script>
import DeleteNoteButton from './DeleteNoteButton.vue'

export default {
  data() {
    return {
      drawer: true,
      overlay: true,
      noteId: null,
      noteTitle: null,
      initData: {}
    };
  },
  computed: {
    notes() {
      return this.$store.getters.notes
    },
    userName() {
      return this.$store.getters.userName
    }
  },
  methods: {
    save() {
      console.log(this.$refs.editor.editor)
    },
    onReady() {
      console.log("ready");
    },
    onChange() {
      this.$refs.editor.editor.save()
        .then(body => {
          const note = {
            body: JSON.stringify(body),
            id: this.noteId,
            title: this.noteTitle
          }
          this.$store.dispatch('saveNote', note)
        })
    },
    noteShow(id) {
      const noteById = this.$store.getters.noteById(id)
      this.initData = JSON.parse(noteById.body)
      this.noteId = noteById.id
      this.noteTitle = noteById.title
      this.overlay = false
      this.drawer = false
    },
    createNote() {
      const note = {
        title: '',
        body: JSON.stringify({time: 1554508385558, blocks: [],version: "2.12.3"})
      }
      this.$store.dispatch('createNote', note)
    },
    deletedNote(deletedId) {
      if(deletedId === this.noteId) {
        this.overlay = true
        this.drawer = true
        this.initData = {time: 1554508385558, blocks: [], version: "2.12.3"}
        this.noteTitle = 'Please select a note.'
        this.noteId = null
      }
    },
    showNoteTitle(title){
      if(title){
        return title
      } else {
        return 'Untitled'
      }
    },
    logout() {
      this.$store.dispatch('logoutUser')
        .then(() => {
          this.$router.push('/login')
      })
    }
  },
  components: {
    'delete-note-button': DeleteNoteButton
  },
  created() {
    this.$store.dispatch('viewNotes')
  },
};
</script>

<style scoped>
.btn-group{
  z-index: 10;
}
.menu{
  z-index: 11;
}
.col-in{
  margin: auto;
}
v-text-field{
  font-size: 12.2em;
}
.note-title{
  font-size: 2.2em;
}
.crud-btn{
  border-radius: 4px;
  margin-top: 2px;
}
.delete-btn{
  border-radius: 4px;
}
.v-list-item{
  max-height: 40px;
}
button, 
button:active, 
button:focus {
    outline: none;
}
.link-note{
  cursor:	pointer;
}
.link-note:hover{
  background:#f0f5f8;
}
</style>