"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from main import views
from app import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moderation/approval/', views.admin_approval_list, name='admin_approval_list'),
    path('moderation/delete_photo/<int:catalog_id>/<int:photo_id>/', views.delete_photo, name='delete_photo'),
    path('moderation/approve/<int:catalog_id>/', views.approve_catalog, name='approve_catalog'),
    path('moderation/delete/<int:catalog_id>/', views.delete_catalog, name='delete_catalog'),
    path('moderation/edit/<int:catalog_id>/', views.edit_gos_number, name='edit_gos_number'),

    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('download/', views.download, name='download'),
    path('catalog/', views.catalog, name='catalog'),
    path('history_car/<str:number>/', views.history_car, name='history_car'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
