from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('CustomUser.urls')),
    path("learn/", include('Myapp.urls')),
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # CKEditor 5 URLs
]

if settings.DEBUG:  # Serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
