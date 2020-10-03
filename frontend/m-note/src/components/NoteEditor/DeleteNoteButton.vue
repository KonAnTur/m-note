<template>
    <button 
        class="btn-del2" 
        @click="deleteNote()"
    >
        <v-icon :class="isActive ? 'red' : 'default'">mdi-delete-forever</v-icon>
    </button>
</template>

<script>
export default {
    props: ['deleteNoteId'],
    data() {
        return {
            isActive: false
        }
    },
    methods: {
        deleteNote() {
            if (this.isActive === true) {
                this.$store.dispatch('deleteNote', this.deleteNoteId)
                this.$emit('deleted-note', this.deleteNoteId)
            } else {
                this.isActive = true
                setTimeout(() => {
                    this.isActive = false
                }, 2000)
            }
        },
    }
}
</script>

<style scoped>
.default{
    color: rgba(0, 0, 0, 0.54) !important;
}
.red{
    color: red !important;
}
.btn-del{
    border-radius: 4px;
}
.btn-del2{
    border-radius: 4px;
    height: 35px;
    width: 35px;
}
.btn-del2:hover{
    background-color:#e9e9e9;
}
button, 
button:active, 
button:focus {
    outline: none;
}
</style>