"""verifier URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from rest_framework import routers
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from applications.api.v1.routes import api_router
from applications.cpf.views import QueryViewSet, StatusViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('consulta', QueryViewSet)
router.register('status', StatusViewSet, base_name='status')

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='index'),

    # API:V1
    url(r'^api/v1/', include(api_router.urls)),

    # SingleQuery
    # Server status
    url(r'^', include(router.urls)),
]