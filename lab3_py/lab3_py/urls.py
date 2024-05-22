"""
URL configuration for lab3_py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from stocks import views
from django.urls import include, path
from rest_framework import routers

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path(r'stocks/', views.StockList.as_view(), name='stocks-list'),
    path(r'stocks/<int:pk>/', views.StockDetail.as_view(), name='stocks-detail'),
    path(r'stocks/<int:pk>/put/', views.put_detail, name='stocks-put'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path(r'users/', views.UsersList.as_view(), name='users-list'),
    path(r'teachers/', views.TeachersList.as_view(), name='teachers-list'),
    path(r'teachers/<int:pk>/', views.TeacherDetail.as_view(), name='teacher-detail'),
    path(r'subjects/', views.SubjectsList.as_view(), name='subjects-list'),
    path(r'uslugi/', views.UslugiList.as_view(), name='uslugi-list'),
    path(r'uslugi/<int:pk>/', views.UslugiDetail.as_view(), name='uslugi-detail'),
    path(r'uslugi/post/', views.PostStock.as_view(), name='uslugi-list'),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),







    

]
