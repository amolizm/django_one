from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hiragana", views.hiragana_index, name='hiragana'),
    path("katakana", views.katakana_index, name='katakana')
]