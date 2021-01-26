from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post',views.PostViewSet) # 2개의 url을 만들어줌


urlpatterns = [
    path('',include(router.urls)),
]
