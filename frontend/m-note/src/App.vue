<template>
  <div id="app">
    <v-speed-dial fixed class="error-view">
      <template v-slot:activator>
        <v-expand-x-transition>
          <v-chip
            v-show="error"
            class="ma-2"
            close
            @click:close="closeError"
            color="indigo darken-3"
            outlined
          >
            {{ error }}
          </v-chip>
        </v-expand-x-transition>
      </template>
    </v-speed-dial>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      expand: false,
    }
  },
  computed: {
    error() {
      return this.$store.getters.error
    }
  },
  methods: {
    closeError() {
      this.$store.dispatch('clearError')
    }
  }
};
</script>

<style scoped>
.error-view{
  right: 10px;
  top: 10px;
}
</style>
