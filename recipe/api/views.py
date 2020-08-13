from rest_framework import viewsets, mixins, status

from rest_framework.filters import SearchFilter

from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from recipe.models import Tag, Ingredient, Recipe

from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer, RecipeImageSerializer

from .permissions import isAuthorOrReadOnly

from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404




class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    permission_classes = [ IsAuthenticated ]
    authentication_classes = [ TokenAuthentication ] 
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




class TagViewSet(BaseRecipeAttrViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filterset_fields = {
        'name': ['startswith']
    }


class IngredientViewSet(BaseRecipeAttrViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filterset_fields = {
        'name': ['startswith', 'lte']
    }
    
    

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [ IsAuthenticated, isAuthorOrReadOnly ]
    authentication_classes = [ TokenAuthentication ]
    filterset_fields = {
        'title': ['startswith'],
    }


    def get_serializer_class(self):
        if self.action == 'retrieve':
            return RecipeDetailSerializer

        elif self.action == "upload_image":
            return RecipeImageSerializer
        return self.serializer_class


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    @action(methods=['POST'], detail=True, url_path='upload-image')
    def upload_image(self, request, pk=None):
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class LikeRecipeAPIView(APIView):
    serializer_class = RecipeSerializer
    permission_classes = [ IsAuthenticated ]

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        recipe.likes.add(user)
        recipe.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(recipe, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk)
        user = request.user
        recipe.likes.remove(user)
        recipe.save()

        serializer_context = {'request': request}
        serializer = self.serializer_class(recipe, context=serializer_context)
        return Response(serializer.data, status=status.HTTP_200_OK)

        



