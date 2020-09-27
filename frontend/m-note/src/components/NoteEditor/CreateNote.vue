<template>
    <v-list-item 
        class="link-note"
        v-click-outside="onClickOutside"
    >
        <v-list-item-content>
            <v-list-item-title>
                <v-expand-x-transition>
                    <v-text-field v-model="titleNote" v-show="isActive"></v-text-field>
                </v-expand-x-transition>
            </v-list-item-title>
        </v-list-item-content>
        <v-list-item-action>
            <button 
                class="btn-create"
                @click="createNote()"
            >
                <v-icon :class="isActive ? 'green' : 'default'">mdi-plus</v-icon>
            </button>
        </v-list-item-action>
    </v-list-item>
</template>

<script>
export default {
    data() {
        return {
            isActive: false,
            titleNote: '',
        }
    },
    methods: {
        createNote() {
            if (this.isActive === true) {
                const note = {
                    title: this.titleNote,
                    body: JSON.stringify({time: 1554508385558, blocks: [],version: "2.12.3"})
                }
                this.$store.dispatch('createNote', note)
                    .then(() => {
                        this.isActive = false
                        this.titleNote = ''
                    })
                    .catch(() => {
                        setTimeout(() => {
                            this.$store.dispatch('clearError')
                        }, 4000)
                    })
            } else {
                this.isActive = true
            }
        },
        onClickOutside() {
            this.isActive = false
            this.titleNote = ''
        }
    }
}
</script>

<style scoped>
.default{
    color: rgba(0, 0, 0, 0.54) !important;
}
.green{
    color: green !important;
}
.btn-create{
    border-radius: 4px;
    height: 35px;
    width: 35px;
}
.btn-create:hover{
    background-color:#e9e9e9;
}
button, 
button:active, 
button:focus {
    outline: none;
}
</style>