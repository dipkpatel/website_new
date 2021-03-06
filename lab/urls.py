from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^play/$', views.play, name='play'),
    url(r'^learn/$', views.learn, name='learn'),
    url(r'^live/$', views.live, name='live'),
    url(r'^design/$', views.design, name='design'),
    url(r'^friends/$', views.friends, name='friends'),

    url(r'^reserve/?$', views.reserve, name='reserve'),
    url(r'^reserve/existing', views.reserve_existing, name='reserve_existing'),

    url(r'^register/?$', views.account_register, name='account_register'),
    url(r'^sign-in/?$', views.account_sign_in, name='account_sign_in'),
    url(r'^sign-out/?$', views.account_sign_out, name='account_sign_out')

]
