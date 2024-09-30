from os.path import basename

from django.urls import path, include
from profiles_api import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename="views")
router.register('profiles', views.BuiltInUserProfileViewSet, basename="user-profile")
router.register('feed', views.ProfileFeedItemViewSet, basename='user-feed')

urlpatterns = [
    path("hello-view/", views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls))
]

#register, getAllUsers, updateUser.