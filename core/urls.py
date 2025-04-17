from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from core.views import index
from django.conf.urls.static import static
from django.conf import settings

app_name = 'core'
urlpatterns = [
    path('dashboard/', index, name='dashboard'),
    path('admin/', admin.site.urls),
    path('', include('userautentication.urls')),
    path('categories/', include('category.urls')),
    path('expenses/', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('budgets/', include('budgets.urls')),
    path('recurring-expenses/', include('recurringExpenses.urls')),
    path('summernote/', include('django_summernote.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
             # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

