<template>
  <div class="container">
      <div class="row mt-5">
          <create-ingredient></create-ingredient>
          <div class="col-lg-6">
              <div class="card">
                  <div class="card-body">
                    <form action="">
                       <div class="form-group">
                        <input type="text" class="form-control" aria-describedby="titleField" placeholder="Enter recipe title" required>
                      </div>
                       <div class="form-group">
                         <textarea class="form-control mb-2" rows="5" aria-describedby="descriptionField" placeholder="about the recipe..."></textarea>
                      </div>
                       <div class="form-group">
                          <input type="number" class="form-control" aria-describedby="minutesField" placeholder="40" required>
                        <small id="minutesField" class="form-text text-muted">How long until ready? (minutes)</small>
                      </div>
                    <div class="card mb-3">
                        <div class="card-body">
                        <small class="font-weight-bold mb-2">Choose ingredients for this recipe</small>
                             <div class="form-check" v-for="(ingredient, key) in ingredients" :key="key">
                                <input class="form-check-input" type="checkbox" :value="ingredient.name" id="defaultCheck1" v-model="ingList" required>
                                <label class="form-check-label" for="defaultCheck1">
                                    {{ ingredient.name }}
                                </label>
                            </div>
                        </div>
                    </div>
                     <div class="card mb-3">
                        <div class="card-body">
                        <small class="font-weight-bold mb-2">Add tags</small>
                             <div class="form-check" v-for="(tag, key) in tags" :key="key">
                                <input class="form-check-input" type="checkbox" :value="tag.name" id="defaultCheck1" v-model="tagList" required>
                                <label class="form-check-label" for="defaultCheck1">
                                    {{ tag.name }}
                                </label>
                            </div>
                        </div>
                    </div>
                    <button type="submit" class="btn btn-dark btn-block">Add Recipe</button>
                    </form>
                  </div>
              </div>
          </div>
          <create-tag></create-tag>
      </div>
  </div>
</template>

<script>
import CreateIngredient from '../components/CreateIngredient.vue';

import CreateTag from '../components/CreateTag.vue';

import { mapGetters } from 'vuex';


export default {
    data() {
        return {
            ingList: [],
            tagList: []
        }
    },
    computed: {
        ...mapGetters([
            'ingredients',
            'tags'
        ])
    },
    components: {
        'create-ingredient': CreateIngredient,
        'create-tag': CreateTag
    }

}
</script>

<style scoped>
    .card {
        border-radius: 30px !important;
        box-shadow: 0 2px 10px rgba(0,0,0, .3);
    }

    .form-control:focus {
        color: #495057;
        background-color: #fff;
        border-color: #777;
        outline: 0;
        box-shadow: 0 0 0 0.01rem #777;
    }
</style>