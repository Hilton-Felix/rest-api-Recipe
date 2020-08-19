from rest_framework import viewsets, mixins, status, generics

from rest_framework.filters import SearchFilter

from rest_framework.authentication import TokenAuthentication

from rest_framework.decorators import action

from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from recipe.models import Tag, Ingredient, Recipe, Comment

from .serializers import TagSerializer, IngredientSerializer, RecipeSerializer, RecipeDetailSerializer, RecipeImageSerializer, CommentSerializer

from .permissions import isAuthorOrReadOnly

from rest_framework.views import APIView

from rest_framework.generics import get_object_or_404

from rest_framework.exceptions import ValidationError




class BaseRecipeAttrViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    permission_classes = [ IsAuthenticated ]
        
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-id')

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

        






class CreateCommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [ IsAuthenticated ]



    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        recipe = get_object_or_404(Recipe, pk=pk)
        serializer.save(user=self.request.user, recipe=recipe)



class SingleRecipeCommentListAPIView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [ IsAuthenticated ]

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Comment.objects.filter(recipe__id=pk).order_by('-created_at')



class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [ IsAuthenticated, isAuthorOrReadOnly ]
    lookup_field = 'id'

