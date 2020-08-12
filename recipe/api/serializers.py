from rest_framework import serializers

from recipe.models import Tag, Ingredient, Recipe

from recipe.models import Tag, Ingredient



class TagSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Tag
        fields = ('id', 'user', 'name')




class IngredientSerializer(serializers.ModelSerializer):

class IngrediantSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Ingredient
        fields = ('id', 'user', 'name')




class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = (
            'id',
            'user',
            'title',
            'time_minutes',
            'ingredients',
            'tags',
            'created_at',
            'updated_at'
        )

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
    
    def get_updated_at(self, instance):
        return instance.updated_at.strftime('%B %d, %Y')


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)
