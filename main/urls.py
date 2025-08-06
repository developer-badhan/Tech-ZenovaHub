from django.urls import include, path

urlpatterns = [
    path('tech-zenovahub.com/', include('user.urls')),
    path('',include('shop.urls')),
    path('admin/', include(('user.urls', 'admin'), namespace='admin')),
]

