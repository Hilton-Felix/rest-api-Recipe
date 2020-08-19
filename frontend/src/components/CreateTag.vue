<template>
    <div class="col-md-3">
      <form @submit.prevent="createNewTag">
          <div class="input-group">
            <input type="text" placeholder="Add an tag" class="form-control" v-model="tagInput">
            <div class="input-group-append">
              <button type="submit" class="btn btn-warning">Add</button>
            </div>  
          </div>
      </form>
      <div class="row mt-5">
        <div class="col">
          <div class="card">
            <div class="card-header">
              <small>Your tags</small>
            </div>
            <div class="card-body data">

             <h4 v-for="(tag, key) in tags" :key="key"   class="text-light float-right"><span class="badge badge-pill bg-dark">
               {{ tag.name }} 
               <span>
                 <i class="fas fa-times-circle text-light delete-icon" @click="revemoveTag(tag.id)"></i></span>
                 </span>
              </h4>
              
            </div>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import Vue from "vue";
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

import { CSRF_TOKEN } from '../store/csrf.js';
import { mapGetters } from 'vuex';


export default {
  data() {
    return {
      tagInput: ''
    }
  },
  computed: {
    ...mapGetters([
      'tags'
    ])
  },
  methods: {
    createNewTag() {
      axios({
        url: 'api/recipe/tags/',
        method: 'POST',
        headers: {
          "content-type": "application/json",
          "X-CSRFTOKEN": CSRF_TOKEN
        },
        data: {
          user: window.localStorage.getItem('username'),
          name: this.tagInput
        }
      })
    },
    revemoveTag(id) {
      axios({
        url: `api/recipe/tags/${id}/`,
        method: 'DELETE',
        headers: {
          "content-type": "application/json",
          "X-CSRFTOKEN": CSRF_TOKEN
        },
      })
      console.log('clicked', id)
    }
  }
}
</script>

<style scoped>
  .delete-icon {
    cursor: pointer;
  }

  .form-control:focus {
      color: #495057;
      background-color: #fff;
      border-color: #777;
      outline: 0;
      box-shadow: 0 0 0 0.01rem #777;
    }

</style>