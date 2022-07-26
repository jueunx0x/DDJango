"""trashcanmap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
import home.views
import map.views
import guide.views
import ai.views
import ai.models
import address.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.begin, name='begin'),
    path('home/',home.views.begin, name='home'),
    path('map/', map.views.detail, name='marker'),
    path('map/', map.views.map, name='map'),
    path('guide/', guide.views.guide, name='guide'),
    path('guide/paper/', guide.views.paper, name='paper'),
    path('guide/plastic/', guide.views.plastic, name='plastic'),
    path('guide/vinyl/', guide.views.vinyl, name='vinyl'),
    path('guide/metal/', guide.views.metal, name='metal'),
    path('guide/glass/', guide.views.glass, name='glass'),
    path('guide/styrofoam/', guide.views.styrofoam, name='styrofoam'),
    path('guide/etc/', guide.views.etc, name='etc'),
    path('guide/guidelist', guide.views.guideinfo, name='guideinfo'),
    path('map/marker', map.views.marker, name='marker'),
    # path('ai/', ai.views.AI, name='AI'),
    path('ai/', ai.views.graphinfo, name='graph'),
    path('ai/seoul', ai.views.seoul_graph, name='seoul_graph'),
    path('address/', address.views.seoul_address, name='seoul_address'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)