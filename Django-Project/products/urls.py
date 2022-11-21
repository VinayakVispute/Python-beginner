from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index),
    path('new', views.new_product)

]

urlpatterns += staticfiles_urlpatterns()