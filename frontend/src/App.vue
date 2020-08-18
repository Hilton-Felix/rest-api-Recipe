<template>
  <div id="app">
    <div id="nav">
      <Header />
    </div>
    <router-view />
  </div>
</template>

<script>
import Header from './views/Header.vue';
export default {
  components: {
    Header
  },
  created() {
    this.$store.dispatch('loadRecipes')
    this.$store.dispatch('getIngredients')
    this.$store.dispatch('getTags')
  }
}
</script>