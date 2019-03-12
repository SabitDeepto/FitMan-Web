"""myProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from Fitness_Basic import views
# from Calorie_Chart import views
# from django.conf.urls.static import static
from myProject import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = 'home'),
    path('single-post/<post_id>/', views.single_post, name='single-post'),
    path('bmr/', views.bmr, name = 'bmr'),
    path('bmi/', views.bmi, name = 'bmi'),
    path('tdee/', views.tdee, name = 'tdee'),
    path('calorie_chart/', views.calorie_chart, name = 'calorie_chart'),
    path('diet_chart/', views.diet_chart, name = 'diet_chart'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+staticfiles_urlpatterns()



