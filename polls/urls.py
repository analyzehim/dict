from django.conf.urls import include, url
from django.contrib import admin


from polls import views

urlpatterns = [

    url(r'^parse', views.parsing, name='parse'),
    url(r'^test', views.test_parsing, name='test'),
    url(r'^index', views.index, name='index'),
    url(r'^get_ip', views.get_ip, name='get_ip'),
    url(r'^quiz$', views.quiz, name='quiz'),
    url(r'^quiz_con$', views.quiz_con, name='quiz_con'),
    #url(r'^reboot', views.req_reboot, name='req_reboot'),
    #url(r'^shutdown', views.req_shutdown, name='req_shutdown'),
    #url(r'^0d6551d674fdb9f978c8ce74a5ad6515', views.reboot, name='reboot'),
    #url(r'^a0da740a1d472a1b5c37749ca4672db6', views.shutdown, name='shutdown'),
    url(r'^clean', views.clean, name='req_clean'),
    #url(r'^a89sa9d89d472a1b5c37749ca4672db6', views.clean, name='clean'),

]
