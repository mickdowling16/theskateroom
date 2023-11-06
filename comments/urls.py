from django.urls import path
from . import views

app_name = 'comments'
urlpatterns = [
    path('add_comment/<int:event_id>/', views.add_comment, name='add_comment'),
    path('like_comment/<int:comment_id>/',
         views.like_comment, name='like_comment'),
]
