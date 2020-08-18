import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

// bootstrap vue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


// axios
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

// axios baseURL
axios.defaults.baseURL = 'http://127.0.0.1:8000/'


Vue.use(BootstrapVue)
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
