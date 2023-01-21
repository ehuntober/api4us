from django.urls import path

from .views import BookAPIViews

urlpatterns = [
    path('',BookAPIViews.as_view(),name="book_list")
]
