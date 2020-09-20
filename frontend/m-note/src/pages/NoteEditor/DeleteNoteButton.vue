<template>
    <div>
        <v-btn 
            tile 
            icon 
            color="indigo" 
            :class="isActive ? 'red' : 'default'" 
            class="btn-del" 
            @click="deleteNote()"
        >
            <v-icon>mdi-delete-forever</v-icon>
        </v-btn>
    </div>
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
    background-color:#e9e9e9;
    transition: color 0.2s;
    transition: background-color 0.2s;
}
.btn-del{
    border-radius: 4px;
}
</style>