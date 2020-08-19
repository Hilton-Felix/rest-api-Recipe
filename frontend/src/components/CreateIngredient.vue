<template>
  <div class="col-md-3">
      <form  @submit.prevent="createNewIngredient">
          <div class="input-group">
            <input type="text" placeholder="Add an ingredient" class="form-control" v-model="ingInput">
            <div class="input-group-append">
              <button type="submit" class="btn btn-warning">Add</button>
            </div>  
          </div>
      </form>
      <div class="row mt-5">
        <div class="col">
          <div class="card">
            <div class="card-header">
              <small>Your ingredients</small>
            </div>
            <div class="card-body">

             <h4 v-for="(ingredient, key) in ingredients" :key="key"   class="text-light"><span class="badge badge-pill bg-dark">{{ ingredient.name }} 
               <span>
                 <i class="fas fa-times-circle text-light delete-icon" @click="removeIngredient(ingredient.id)"></i></span>
                 </span>
              </h4>

            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';


import Vue from "vue";
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { CSRF_TOKEN } from '../store/csrf.js';


export default {
  data() {
    return {
      ingInput: ''
    }
  },
  computed: {
    ...mapGetters([
      'ingredients'
    ])
  },
  methods: {
    createNewIngredient() {
     axios({
       url: "api/recipe/ingredients/",
       method: "POST",
       headers: {
          "content-type": "application/json",
          "X-CSRFTOKEN": CSRF_TOKEN
      },
      data: {
        user: window.localStorage.getItem('username'),
        name: this.ingInput
      }
     })
    },
    removeIngredient(id) {
		axios({
			url: `api/recipe/ingredients/${id}/`,
			method: 'DELETE',
			 headers: {
				"content-type": "application/json",
				"X-CSRFTOKEN": CSRF_TOKEN
			}
		})
    }
  }

}
</script>

<style scoped>
  .delete-icon {
    cursor: pointer !important;
  }

  .form-control:focus {
      color: #495057;
      background-color: #fff;
      border-color: #777;
      outline: 0;
      box-shadow: 0 0 0 0.01rem #777;
  }
</style>