from rest_framework import viewsets, mixins


from recipe.models import Tag, Ingredient, Recipe

from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication


class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin):
    permission_classes = [ IsAuthenticated ]
    authentication_classes = [ TokenAuthentication ] 
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class TagViewSet(BaseRecipeAttrViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(BaseRecipeAttrViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer



class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [ IsAuthenticated ]
    authentication_classes = [ TokenAuthentication ]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeDetailSerializer
        return self.serializer_class

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)