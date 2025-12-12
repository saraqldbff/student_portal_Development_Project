from django.contrib import admin
from django.urls import path, include

# Main URL configuration for the entire project
urlpatterns = [

    # Admin dashboard
    path('admin/', admin.site.urls),

    # Djoser authentication endpoints (register, reset password, etc.)
    path('api/auth/', include('djoser.urls')),

    # JWT authentication endpoints (login, refresh, verify)
    path('api/auth/jwt/', include('djoser.urls.jwt')),

    # Service request API endpoints (student requests)
    path('api/requests/', include('requestsapp.urls')),
]
#name:sara
#pass:123456