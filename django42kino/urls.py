
from django.contrib import admin
from django.urls import path, include
from kino42 import views
import captcha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('kino/', views.Kinolist.as_view(), name='allkino'),
    path('artist/', views.artistlist.as_view(), name='allartists'),
    path('kino/<str:title>/<int:pk>/', views.KinoDetail.as_view(), name='oneKino'),
    #path('<str:title>/<int:pk>/', views.kinoDetail.as_view(), name='oneKino'),
    #path('kino/<str:num>', views.index, name='oneKino'),
    path('auth/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.index),
    path('auth/registration/', views.registration, name='reg'),
    path('captcha/', include('captcha.urls')),
    path('accounts/login/', views.index),
    path('kabinet/', views.profile, name='kabinet'),
    path('kabinet/change/', views.profileChange, name='kabinetChange'),
    path('otziv/<int:pk>/', views.funcOtziv, name='otziv')

]
