from django.urls import path
from . import views

urlpatterns = [
    path('add_comment/<int:event_id>/', views.add_comment, name='add_comment'),
    path('event/<int:event_id>/comment/',
         views.add_comment, name='add_comment'),
    path('comment/like/', views.like_comment, name='like_comment'),
    path('comment/reply/<int:comment_id>/', views.add_reply, name='add_reply'),
]
