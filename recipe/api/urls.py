from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
<<<<<<< HEAD
router.register('list', views.RecipeViewSet)

=======
>>>>>>> 327014df862c711b0ca6f00a27b6774d6190b9fc

urlpatterns = [
    path('', include(router.urls)),
]


