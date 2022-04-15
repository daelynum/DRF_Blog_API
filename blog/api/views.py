from rest_framework.views import APIView
from rest_framework.response import Response

from .funcs import nesting_comments
from .serializers import APIPostSerializer, APICommentSerializer
from .models import Post, Comment

'''url api/posts/'''
class Posts(APIView):
    def get(self, request):
        all_posts = Post.objects.all()
        serialized_posts = APIPostSerializer(all_posts, many=True)

        return Response({"posts": serialized_posts.data})

    def post(self, request):
        post = request.data.get("post")

        post_data = APIPostSerializer(data=post)
        if post_data.is_valid(raise_exception=True):
            post_data.save()

        return Response({"success": f"Post {post} created successfully"})


'''url api/post/<int:post_id>/'''
class ViewPost(APIView):
    def get(self, request, post_id):
        post = Post.objects.filter(id=post_id)[0]
        serialized_post = APIPostSerializer(post)

        return Response({"post": serialized_post.data})


'''url api/post/<int:post_id>/comments/'''
class Comments(APIView):
    def get(self, request, post_id):
        default_nesting_level = 3
        nesting_level = int(self.request.GET.get("nesting-level", default_nesting_level))

        comments = Comment.objects.filter(post=post_id, parent=None)
        comments_tree = nesting_comments(comments, nesting_level)

        return Response({
            "comments": comments_tree,
        })

    def post(self, request, post_id):
        comment = {
            "post": post_id,
            "parent": request.data.get("parent"),
            "author": request.data.get("author"),
            "content": request.data.get("content"),
        }

        comment_data = APICommentSerializer(data=comment)
        if comment_data.is_valid(raise_exception=True):
            comment_data.save()

        return Response({"success": f"Comment {comment} created successfully"})


'''url api/post/<int:post_id>/comments/<int:comment_id>/'''
'''url api/post/<int:post_id>/comments/<int:comment_id>/?nesting-level=3'''
class ViewComments(APIView):
    def get(self, request, post_id, comment_id):
        default_nesting_level = 3
        nesting_level = int(self.request.GET.get("nesting-level", default_nesting_level))

        comment = Comment.objects.filter(id=comment_id)[0]

        return Response({
            "comment": nesting_comments([comment], nesting_level),
        })