import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

// recipe module
import recipes from './modules/recipes.js';

export default new Vuex.Store({
  modules: {
    recipes
  }
});
