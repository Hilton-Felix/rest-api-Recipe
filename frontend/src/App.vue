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
  }
}
</script>
