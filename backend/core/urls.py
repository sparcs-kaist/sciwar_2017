"""sciwar URL Configuration

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
from django.conf.urls import url
from . import views

urlpatterns = [
    # GET
    url(r'^events/$', views.events),
    url(r'^events/(?P<event_id>\d+)/players-k/$', views.event_players_k),
    url(r'^events/(?P<event_id>\d+)/players-p/$', views.event_players_p),
    url(r'^events/(?P<event_id>\d+)/messages/$', views.event_messages),
    url(r'^cheermessage/$', views.messages),
    url(r'^toto/(?P<pk>\d+)/$', views.totoView),
    url(r'^toto/complete/(?P<pk>\d+)/$', views.totoViewComplete),
    url(r'^toto-content/$', views.totoContent),
    url(r'^supporters/(?P<pk>\d+)/', views.supportersView),
    url(r'^supporters/complete/(?P<pk>\d+)/', views.SupportersViewComplete),
    url(r'^locations/$', views.locations),

    # PUT
    url(r'^toto/$', views.toto),
    #url(r'^events/(?P<event_id>\d+/message/$', views.message),

    # GET + POST
    url(r'^events/(?P<event_id>\d+)/$', views.event),

    # GET + PUT
    url(r'^videos/$', views.videos),

    # GET + POST + DELETE
    url(r'^videos/(?P<pk>\d+)/$', views.video),

    # GET + POST + PUT
    url(r'^supporters/$', views.supporters),

    # POST
    url(r'^shrhksrP/$', views.rescore_toto),
    url(r'^cheermessage/(?P<pk>\d+)/$', views.messageLike),
]
