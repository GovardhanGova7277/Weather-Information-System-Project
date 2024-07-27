from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('demo/', include('demo.urls')),
]
# http://127.0.0.1:8000/demo/
