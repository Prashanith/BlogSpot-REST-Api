"""blog_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from super_user import views
from django.conf.urls import url,include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Post/', views.PostList.as_view(), name='home'),
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   # url(r'^api/v1/', include('project.api', namespace='apiv1')),

]


"""
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^Post/", views.PostList.as_view()),
    path('',views.home,name="Blog-Home"),
    path('login/', include('rest_framework.urls')),
    url(r'^auth/obtain_token/', obtain_jwt_token),
    url(r'^auth/refresh_token/', refresh_jwt_token),
]"""
