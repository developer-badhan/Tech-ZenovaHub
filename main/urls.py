from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('tech-zenovahub.com/', include('user.urls')),
    path('',include('shop.urls')),
    path('admin/', include(('user.urls', 'admin'), namespace='admin')),
]




urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


