"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from .views import UserDetails
from .views import UsersList
from .views import UserAuthToken
from tasks.views import TaskList
from . import settings

schema_view = get_swagger_view(title='My Project API')

urlpatterns = [
    url(r'^$', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    # url(r'^api/users/$', Users1.as_view()),
    url(r'^users/$', UsersList.as_view()),
    url(r'^task/$', TaskList.as_view()),
    # url(r'^taskview/$', TaskListView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserDetails.as_view()),
    url(r'^users/get_auth_token/$', UserAuthToken.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
