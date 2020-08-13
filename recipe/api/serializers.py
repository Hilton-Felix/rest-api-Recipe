from rest_framework import serializers

from recipe.models import Tag, Ingredient, Recipe


class TagSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Tag
        fields = ('id', 'user', 'name')




class IngredientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Ingredient
        fields = ('id', 'user', 'name')


class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = (
            'id',
            'user',
            'title',
            'price',
            'time_minutes',
            'likes',
            'ingredients',
            'tags',
            'image',
            'created_at',
            'updated_at'
        )

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
    
    def get_updated_at(self, instance):
        return instance.updated_at.strftime('%B %d, %Y')

    def get_likes(self, instance):
        return instance.likes.count()


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True) 


class RecipeImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id', 'image') 
