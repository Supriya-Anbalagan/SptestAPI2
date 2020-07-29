
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Login/',views.Loginviewset.as_view({'get':'list','post':'create'})),
    path('Login/',<int:pk>/'views.Loginviewset.as_view({'delete':'destroy'})),
    path('api-auth/', include('rest-framework.urls', names-space='rest_framework'))
]
