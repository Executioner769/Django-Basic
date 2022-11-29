from django.contrib import admin
from django.urls import path, include

from mysite.core import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('secret/edit', views.edit),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/core/item/add',views.item),
    path('admin/', admin.site.urls),
    
]
