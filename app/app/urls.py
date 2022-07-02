from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.renderers import SwaggerUIRenderer,\
    OpenAPIRenderer

schema_view = get_schema_view(
    title='Data mining app',
    renderer_classes=[OpenAPIRenderer, SwaggerUIRenderer]
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data-mining/', include('core.urls')),
    url(r'^', schema_view, name="docs"),
]
