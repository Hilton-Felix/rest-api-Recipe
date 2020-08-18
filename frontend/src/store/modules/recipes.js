import Vue from "vue";
import axios from 'axios'
import VueAxios from 'vue-axios'
Vue.use(VueAxios, axios)

const state ={
    recipes: [],
    recipe: {},
    recipeComments: [],
    ingredients: [],
    tags: []
}

const mutations = {
    LOAD_RECIPES(state, data) {
        state.recipes = data
    },
    GET_RECIPE_DATA(state, data) {
        state.recipe = data
    },
    GET_RECIPE_COMMENTS(state, data) {
        state.recipeComments = data
    },
    GET_INGREDIENTS(state, data) {
        state.ingredients = data
    },
    GET_TAGS(state, data) {
        state.tags = data
        console.log('tags', data)
    }
}

const actions = {
    // load all recipes from the api endpoint
    loadRecipes: ({ commit }) => {
        axios
            .get('api/recipe/list/')
            .then(res => {
                commit('LOAD_RECIPES', res.data.results)
            })
            .catch(err => console.log(err.response))
    },

    // Retrive recipe detail
    getRecipeData: ({ commit }, {id: id}) => {
        axios
            .get(`api/recipe/list/${id}/`)
            .then(res => {
                commit('GET_RECIPE_DATA', res.data)
            })
            .catch(err => console.log(err.response))
    },

    // Retrieve single-recipe comments
    getRecipeComments: ({ commit }, {id: id}) => {
        axios
            .get(`api/recipe/list/${id}/comments/`)
            .then(res => {
                commit('GET_RECIPE_COMMENTS', res.data.results)
            })
            .catch(err => console.log(err.response))
    },

    // Retrieve a user's ingredients
    getIngredients: ({ commit }) => {
        axios
            .get('api/recipe/ingredients/')
            .then(res => {
                commit('GET_INGREDIENTS', res.data.results)
            })
            .catch(err => console.log(err.response))
    },

    // Retrieve a user's tags
    getTags: ({ commit }) => {
        axios
            .get('api/recipe/tags/')
            .then(res => {
                commit('GET_TAGS', res.data.results)
            })
            .catch(err => console.log(err.response))
    },
}

const getters = {
    recipes: state => {
        return state.recipes
    },
    recipe: state => {
        return state.recipe
    },
    recipeComments: state => {
        return state.recipeComments
    },
    ingredients: state => {
        return state.ingredients
    },
    tags: state => {
        return state.tags
    }

}

export default {
    state,
    mutations,
    actions,
    getters
}