import Vue from "vue";
import VueRouter from "vue-router";

// views
import Home from "../views/Home.vue";
import RecipeDetail from "../views/RecipeDetail.vue";
import CreateRecipe from '../views/CreateRecipe.vue';


Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: '/recipe/:id',
    name: "RecipeDetail",
    component: RecipeDetail,
    props: true
  },
  {
    path: '/add-recipe',
    name: 'CreateRecipe',
    component: CreateRecipe
  }
  
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
