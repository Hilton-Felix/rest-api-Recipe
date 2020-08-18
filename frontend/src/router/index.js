import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import RecipeDetail from "../views/RecipeDetail.vue";

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
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
