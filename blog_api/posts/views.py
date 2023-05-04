from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer


class Post_List(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class Post_Detail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer
