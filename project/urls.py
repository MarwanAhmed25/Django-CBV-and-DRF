from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('products/', include('products.urls', namespace='products')), # cbv 
    path('types/', include('product_types.urls', namespace='types')), #cbv
    path('models/', include('product_models.urls', namespace='models')), #cbv
    path('api/v1/products/', include('products.api.urls')), # rest_framework.generic
    path('api/v1/types/', include('product_types.api.urls')), # rest_framework.generic
    path('api/v1/models/', include('product_models.api.urls')), # rest_framework.generic
    path('api-auth/', include('rest_framework.urls')),  # rest_framework [ login & logout ]
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')), # all auth api except registration
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')), # api registration
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# super user marwan , password: 111