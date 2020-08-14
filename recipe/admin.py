from django.contrib import admin

# Register your models here.
from .models import Tag, Ingredient, Recipe, Comment

admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe)

# new
admin.site.register(Comment)
