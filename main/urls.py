from django.urls import include, path

urlpatterns = [
    path('', include('user.urls'))
]

