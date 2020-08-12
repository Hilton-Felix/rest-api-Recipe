from rest_framework import serializers
<<<<<<< HEAD
from recipe.models import Tag, Ingredient, Recipe

=======
from recipe.models import Tag, Ingredient
>>>>>>> 327014df862c711b0ca6f00a27b6774d6190b9fc


class TagSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Tag
        fields = ('id', 'user', 'name')



<<<<<<< HEAD
class IngredientSerializer(serializers.ModelSerializer):
=======
class IngrediantSerializer(serializers.ModelSerializer):
>>>>>>> 327014df862c711b0ca6f00a27b6774d6190b9fc
    user = serializers.StringRelatedField()

    class Meta:
        model = Ingredient
        fields = ('id', 'user', 'name')
<<<<<<< HEAD




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



=======
>>>>>>> 327014df862c711b0ca6f00a27b6774d6190b9fc
