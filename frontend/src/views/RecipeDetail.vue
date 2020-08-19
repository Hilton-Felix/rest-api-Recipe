<template>
 <div class="container">
     <div class="row mt-5">
         <div class="col-lg-8 offset-lg-2">
             <div class="card mb-3" @click="getRecipe(recipe.id)">
                    <div class="card-img-top">
                        <img src="https://source.unsplash.com/random/1920x400/?food" class="img-fluid rounded">                       
                    </div>  
                    <div class="card-header text-center">
                        <h2 class="text-muted mb-0">{{ recipe.title }}</h2>
                        <small><span><i class="fas fa-user text-muted"></i></span> {{ recipe.user }} &mdash; <span><i class="fas fa-heart text-danger"></i></span> {{ recipe.likes }} <span><i class="far fa-comments text-info"></i></span> {{ recipe.comments_count }}</small>
                        <p>
                            <span v-for="(tag, index) in recipe.tags" :key="index"  class="badge bg-warning mr-2">{{ tag.name }}</span>
                        </p>
                      
                    </div>
                    <div class="card-body p-4">
                        <div class="row mb-5">
                            <a v-show="recipe.link" :href="recipe.link" target="_blank">
                                 <h4><span class="badge bg-dark badge-pill text-light"><i class="fas fa-link text-light"></i> Visit link</span></h4>
                            </a>
                            {{ recipe.description }}
                        </div>
                        <div class="row">
                            <h6 class="text-muted">Ingredients</h6>
                        </div>
                       <div class="row">
                           <ul>
                               <li v-for="(ingredient, index) in recipe.ingredients" :key="index">{{ ingredient.name }}</li>
                           </ul>
                       </div>
                       <div class="row">
                         <h6 class="text-muted">Ready in</h6>
                       </div>
                       <div class="row">
                             <p><i class="far fa-clock text-muted"></i> {{ recipe.time_minutes }} minutes</p>
                       </div>
                    </div>
                     <div class="card-footer">
                         <small>{{ recipe.created_at }}</small>
                    </div>
                </div>
         </div>
     </div>
     <div class="row">
         <div class="col-lg-8 offset-lg-2">
            <small v-show="recipe.comments_count > 0">Comments</small><br>
            <div class="card mb-3" v-for="(comment, key) in recipeComments" :key="key">
                <div class="card-body">
                    <small class="text-muted mb-2">{{ comment.user }} | {{ comment.created_at }}</small>
                    <div class="card-header">
                        <small>{{ comment.text }}</small>
                    </div>
                </div>
            </div>
         </div>
     </div>
 </div>
</template>

<script>
import { mapGetters } from 'vuex';
import { mapActions } from 'vuex';


export default {
    name: 'RecipeDetail',
    props: ['id'],
    computed: {
        ...mapGetters([
            'recipe',
            'recipeComments'
        ])
    },
    methods: {
        ...mapActions([
            'getRecipeData',
            'getRecipeComments'
        ])
    },
    created() {
        this.getRecipeData({id: this.id})
        this.getRecipeComments({id: this.id})

    }
}
</script>

<style scoped>
    .card {
        border-radius: 30px !important;
        box-shadow: 0 2px 10px rgba(0,0,0, .3);
    }
</style>