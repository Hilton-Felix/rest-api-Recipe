<template>
<div>
    <div class="header-section">
        <div class="container">
            <div class="row">
                <div class="col info-box">
                    <h1 class="title display-3">Welcome to Mapishi</h1>
                    <h5>find any recipe for your next delicious meal</h5>
                </div>
            </div>
        </div>
    </div>
    <hr>
    <div class="container">
        <div class="row my-5 text-center">
            <div class="col text-center">
                <h5>Browse recipes</h5>
                <hr style="width: 10%; background: #ffc107; height: 2px;">
            </div>
        </div>
        <div class="row my-5">

            <div class="col-md-3" v-for="(recipe, index) in recipes" :key="index">
                <div class="card mb-3" @click="getRecipe(recipe.id)">
                    <div class="card-img-top">
                        <img :src="recipe.image.url" class="img-fluid">                       
                    </div>  
                    <div class="card-header">
                        <h5 class="text-muted mb-0">{{ recipe.title }}</h5>
                        <small><span><i class="fas fa-user text-muted"></i></span> {{ recipe.user }} &mdash; <span><i class="fas fa-heart text-danger"></i></span> {{ recipe.likes }} <span><i class="far fa-comments text-info"></i></span> {{ recipe.comments_count }}</small>
                    </div>
                    <div class="card-body p-4">
                        <div class="row mb-2">
                            <h6><span><i class="far fa-clock text-muted"></i></span> {{ recipe.time_minutes }} minutes</h6>
                        </div>
                        <div class="row mb-2">
                            <h6><span><i class="fas fa-pepper-hot text-danger"></i></span> {{ recipe.ingredients.length }} ingredients</h6>
                        </div>
                    </div>
                     <div class="card-footer">
                         <small>{{ recipe.created_at }}</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
</template>


<style scoped>
    .title {
        font-weight: bold;
    }

    .header-section {
        background-image: url('../assets/review-bg.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        height: 550px;
        color: #f9fafb;
        
    }
    .info-box {
        margin-top: 150px;
    }

    .card {
        border-radius: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0, .3);
        cursor: pointer;
    }
</style>

<script>
import { mapGetters } from 'vuex';
export default {
    computed: {
        ...mapGetters([
            'recipes'
        ])
    },
    methods: {
        getRecipe(id) {
            this.$router.push({name: 'RecipeDetail', params: {id: id}})
        }
    },
}
</script>