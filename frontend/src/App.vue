<template>
  <div id="app">
    <div id="nav">
      <Header />
    </div>
    <router-view />
  </div>
</template>

<script>
import Vue from "vue";
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)


import Header from './views/Header.vue';

export default {
  components: {
    Header
  },
  methods: {
    getLoggedInUser() {
      axios
        .get('api/user/me/')
        .then(res => {
          window.localStorage.setItem('username', res.data.email)
        })
        .catch(err => console.log(err.response))
    }
  },
  created() {
    setInterval(() => {
      this.$store.dispatch('getIngredients')
      this.$store.dispatch('getTags')
    }, 500);
    this.$store.dispatch('loadRecipes')
    this.getLoggedInUser()
    console.log(window.localStorage.getItem('username'))
  }
}
</script>