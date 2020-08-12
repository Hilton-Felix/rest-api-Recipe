from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('list', views.RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


