import Vue from "vue";
import Vuex from "vuex";

// recipe module
import recipes from './modules/recipes.js';
Vue.use(Vuex);

export default new Vuex.Store({
  modules: {
    recipes
  }
});
