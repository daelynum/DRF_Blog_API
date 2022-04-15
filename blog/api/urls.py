from django.urls import path
from django.conf.urls.static import static
from blog import settings
from .views import Posts, ViewPost, Comments, ViewComments

urlpatterns = [
    path('api/posts/', Posts.as_view(), name='posts'),
    path('api/post/<int:post_id>/', ViewPost.as_view(), name='post'),
    path('api/post/<int:post_id>/comments/', Comments.as_view(), name='comments'),
    path('api/post/<int:post_id>/comments/<int:comment_id>/', ViewComments.as_view(), name='comment'),
]