from django.conf.urls import url, include
from .views import LoginApiView, TableListViewSet, FilterNameViewSet, NameDetailsViewSet, RegisterEventViewSet, \
    RegisteredUsersViewSet, RoomTypeListViewSet, UserLoginViewSet, OtpPostViewSet, HotelNameViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'tablelist', TableListViewSet, base_name='table-list')
router.register(r'filtername/(?P<table_id>(\d+))/(?P<input_char>[\w\+]+)', FilterNameViewSet, base_name='filter-name')
router.register(r'namedetails', NameDetailsViewSet, base_name='name-details')
router.register(r'myregistration/(?P<table_id>(\d+))', RegisterEventViewSet, base_name='register-event')
router.register(r'registeredusers', RegisteredUsersViewSet, base_name='register-users')
router.register(r'roomtype', RoomTypeListViewSet, base_name='room-type')
router.register(r'user-registration', UserLoginViewSet, base_name='user_registration')
router.register(r'otp-post', OtpPostViewSet, base_name='otp_post')
router.register(r'hotel-name', HotelNameViewSet, base_name='hotel_name')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^registration/', LoginApiView.as_view(), name='registration'),

]
