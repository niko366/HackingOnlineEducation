"""Books URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from newsletter import views
from django.contrib.auth import views as auth_views
app_name='ratings'
urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/',views.signup, name='signup'),
    url(r'^contact/',views.contact, name='contact'),
    url(r'^register/',views.register, name='register'),
    url(r'^accounts/profile/',views.profile, name='profile'),
    url(r'^courses/rating/(?P<category_name>.+)/$',views.rating_courses, name='rating_courses'),
    url(r'^login/',auth_views.auth_login, name='login'),
    url(r'^accounts/logout/',auth_views.auth_logout, name='logout'),
    url(r'^explore/',views.explore, name='explore'),
    url(r'^courses/(?P<category_name>.+)/$',views.category, name='category'),
    url(r'^challenges/',views.challenges, name='challenges'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings')),
    url(r'^search/',views.search, name='search'),
    url(r'^articles/',views.articles, name='articles'),
    url(r'^accounts/enroll/',views.enroll, name='enroll'),
    url(r'^add/',views.add, name='add'),
    url(r'^remove/',views.remove, name='remove'),
]

if settings.DEBUG:
     urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
