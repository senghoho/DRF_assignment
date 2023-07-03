from django.urls import path
from .views import *
from . import views

app_name="music_app"
urlpatterns = [
    path('album/', views.album_list_create),
    path('track/', views.track_list_create),
    path('<int:album_id>',views.album_detail_update_delete),
    path('<int:track_id>',views.track_detail_update_delete),
]