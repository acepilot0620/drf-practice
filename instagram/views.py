from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# # Create your views here.
# def post_list(request):
#     # 2가지 분기
#     pass

# def post_detail(request, pk):
#     # 3가지 분기
#     pass