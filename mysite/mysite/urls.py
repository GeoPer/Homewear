from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('homewear/', include('homewear.urls')),
    path('admin/', admin.site.urls),
]