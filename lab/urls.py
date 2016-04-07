from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^aboutus/$', views.aboutus, name='aboutus'),
    url(r'^contactus/$', views.contactus, name='contactus'),
    url(r'^play/$', views.play, name='play'),
    url(r'^learn/$', views.learn, name='learn'),
    url(r'^live/$', views.live, name='live'),
    url(r'^reduce/$', views.reduce, name='reduce'),
    url(r'^makeit/$', views.makeit, name='makeit'),
    url(r'^yorkland/$', views.yorkland, name='yorkland'),

    url(r'^reserve/?$', views.reserve, name='reserve'),

    url(r'^register/?$', views.account_register, name='account_register'),
    url(r'^sign-in/?$', views.account_sign_in, name='account_sign_in'),
    url(r'^sign-out/?$', views.account_sign_out, name='account_sign_out')

]
