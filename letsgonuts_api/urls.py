from django.conf.urls import url, include
from .views import LoginApiView, TableListViewSet, FilterNameViewSet, NameDetailsViewSet, RegisterEventViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'tablelist', TableListViewSet, base_name='table-list')
router.register(r'filtername/(?P<table_id>(\d+))/(?P<input_char>[a-zA-Z])', FilterNameViewSet, base_name='filter-name')
router.register(r'namedetails', NameDetailsViewSet, base_name='name-details')
router.register(r'myregistration/(?P<table_id>(\d+))', RegisterEventViewSet, base_name='register-event')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^registration/', LoginApiView.as_view(), name='registration'),

]
