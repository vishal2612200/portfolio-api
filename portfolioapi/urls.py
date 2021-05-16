"""portfolioapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tradeapi/', include('trade.restapi.urls')),
   
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


if settings.REST_FRAMEWORK_GENERATE_API_DOCS:
    from django.views.generic import TemplateView
    from rest_framework.schemas import get_schema_view


    trade_schema_view = get_schema_view(
        title='Trade related API',
        description='How to play with Trade data through API',
        url='/tradeapi/',
        urlconf='trade.restapi.urls',
    )
    trade_redoc_view = TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'schema:trade'}
    )


    base_redoc_view = TemplateView.as_view(template_name='redocbase.html')

    schema_patterns = ([
        path('trade/', trade_schema_view, name='trade'),
    ], 'schema')

    redoc_patterns = ([
        path('', base_redoc_view, name='base'),
        path('trade/', trade_redoc_view, name='trade'),
    ], 'redoc')

    urlpatterns += [
        path('schema/', include(schema_patterns)),
        path('', include(redoc_patterns, namespace="api_docs"))
    ]
    