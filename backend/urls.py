from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Movie Booking API",
        default_version='v1',
        description="API documentation for Movie Booking System",
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Include app URLs
    path('', include('movies.urls')),   # optional if you have it
    path('', include('booking.urls')),

    # Swagger docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
]
