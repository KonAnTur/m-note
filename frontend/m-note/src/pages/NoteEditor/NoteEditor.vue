<template>
  <div id="app">
    <v-navigation-drawer v-model="drawer" class="menu" app>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <!--Konstantin Turov-->
          </v-list-item-title>
          <v-list-item-subtitle>
            <button @click="logout">logout</button>
          </v-list-item-subtitle>
          
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list dense>
        <v-list-item 
          link
          v-for="note in notes"
          :key="note.id"
          @click="noteShow(note.id)"
        >
          <v-list-item-content>
            <v-list-item-title>{{ showNoteTitle(note.title) }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <div class="menu-btn" fixed>
        <v-speed-dial fixed class="btn-group">
          <template v-slot:activator>
            <v-btn icon color="pink" @click="drawer = !drawer">
              <v-icon>mdi-menu</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon color="indigo" @click="createNote">
              <v-icon>mdi-plus</v-icon>
            </v-btn>
            <v-spacer></v-spacer>
            <v-btn icon color="indigo" @click="deliteNote">
              <v-icon>mdi-delete-forever</v-icon>
            </v-btn>
          </template>
        </v-speed-dial>
      </div>
      <v-col cols="12" sm="6" class="col-in">
        <v-text-field
          class="note-title"
          v-model="noteTitle"
          label="Untitled"
          @change="onChange"
          single-line
        ></v-text-field>
      </v-col>
      <editor autofocus header list code inlineCode embed marker table raw delimiter quote paragraph checklist ref="editor" holder-id="codex-editor" :init-data="initData" @save="save" @ready="onReady" @change="onChange" />
      <div class="text-center">
        <v-overlay :value="overlay" z-index="5">
        </v-overlay>
      </div>
    </v-main>
  </div>
</template>

<script>
export default {
  data() {
    return {
      drawer: true,
      overlay: true,
      noteId: null,
      noteTitle: 'Please select a note.',
      initData: {
        time: 1554508385558,
        blocks: [],
        version: "2.12.3"
      }
    };
  },
  computed: {
    notes() {
      return this.$store.getters.notes
    },
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
      this.noteId = id
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
    deliteNote() {
      this.$store.dispatch('deleteNote', this.noteId)
      this.overlay = true
      this.drawer = true
      this.initData = {time: 1554508385558, blocks: [], version: "2.12.3"}
      this.noteTitle = 'Please select a note.'
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
  created() {
    this.$store.dispatch('viewNotes')
  }
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
</style>