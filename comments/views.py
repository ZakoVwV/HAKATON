from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from post.permissions import IsOwner

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=False, methods=['GET'])
    def get_user_comments(self, request):
        user_comments = Comment.objects.filter(owner=request.user)
        serializer = CommentSerializer(user_comments, many=True)
        return Response(serializer.data)
    
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated(), IsOwner()]
        return [permissions.AllowAny()]
    