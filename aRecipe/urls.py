"""aRecipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from django_registration.backends.one_step.views import RegistrationView
from django_registration.backends.activation.views import RegistrationView
from profiles.forms import CustomUserForm

urlpatterns = [
    path('admin/', admin.site.urls),

    # profiles api
    path('api/user/', include('profiles.api.urls')),

    # recipe api
    path('api/recipe/', include('recipe.api.urls')),

    # Login via rest
    path('api/rest-auth/', include('rest_auth.urls')),

    # Login via browsable api
    path('api-auth/', include('rest_framework.urls')),


    # registation via rest
    path('api/rest_auth/registration/', include('rest_auth.registration.urls')),


    # login/logout/password reset via browser
    path('accounts/', include('django.contrib.auth.urls')),


    # registration via browser
    path('accounts/register/', RegistrationView.as_view(
        form_class = CustomUserForm,
        template_name="registration/register.html"
    ), name='django_registration_register'),

    # path('accounts/', include('django_registration.backends.on_step.urls'))
    path('accounts/', include('django_registration.backends.activation.urls'))

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
