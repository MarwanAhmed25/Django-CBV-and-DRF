from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('types/', include('product_types.urls', namespace='types')),
    path('models/', include('product_models.urls', namespace='models')),
    path('api/v1/products/', include('products.api.urls')),
    path('api/v1/types/', include('product_types.api.urls')),
    path('api/v1/models/', include('product_models.api.urls')),
    path('api-auth', include('rest_framework.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# super user marwan , password: 111