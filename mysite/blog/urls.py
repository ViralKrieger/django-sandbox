from django.conf.urls import url
from . import views


urlpatterns = [
    # Post views
    url(r'^$', views.post_list, name='post_list'),
    # Post details views
    # TODO figure this out
    # Old:
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2}/(?P<day>\d{2})/(?P<post>>[-\w]+)/$)',
    # New:
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2}/(?P<day>[0-9]{2})/(?P<post>>[-\w]+)/$)',
        views.post_detail,
        name='post_detail'),
]

