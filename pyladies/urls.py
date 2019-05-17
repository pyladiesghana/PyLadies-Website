"""pyladies URL Configuration

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

# Django Imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

# Third-party app imports
from machina import urls as machina_urls

urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('contact/', include('contact.urls', namespace='contact')),
    path('about/', include('about.urls', namespace='about')),
    path('forum/', include(machina_urls)),
    path('admin/', admin.site.urls),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "PyLadies Admin"
admin.site.site_title = "PyLadies Admin Portal"
admin.site.index_title = "Welcome to PyLadies Portal"
