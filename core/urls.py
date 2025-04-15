from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf.urls.static import static

app_name = 'core'
urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', include('userautentication.urls')),
]
             # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

