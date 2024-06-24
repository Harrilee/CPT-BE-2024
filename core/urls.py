from django.urls import path

from . import views

urlpatterns = [
    path('info', views.info, name="info"),
    path('writing/<int:day>', views.writing, name="writing"),
    path('game', views.game, name="game")
]