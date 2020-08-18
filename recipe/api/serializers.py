from rest_framework import serializers

from recipe.models import Tag, Ingredient, Recipe, Comment


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
    comments_count = serializers.SerializerMethodField(read_only=True)
    user_has_liked = serializers.SerializerMethodField()

    ingredients = serializers.PrimaryKeyRelatedField(many=True, queryset=Ingredient.objects.all())
    tags = serializers.PrimaryKeyRelatedField(many=True, queryset=Tag.objects.all())

    class Meta:
        model = Recipe
        fields = (
            'id',
            'user',
            'title',
            'description',
            'price',
            'time_minutes',
            'likes',
            'user_has_liked',
            'comments_count',
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

    def get_comments_count(self, instance):
        return instance.comments.count()

    def get_user_has_liked(self, instance):
        request = self.context.get('request')
        return instance.likes.filter(pk=request.user.pk).exists()


class RecipeDetailSerializer(RecipeSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True) 


class RecipeImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Recipe
        fields = ('id', 'image') 




# new
class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    comments = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ('reply', 'recipe')
    

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')
    
    def get_updated_at(self, instance):
        return instance.updated_at.strftime('%B %d, %Y')