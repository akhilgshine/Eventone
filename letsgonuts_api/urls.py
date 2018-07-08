from django.conf.urls import include, url
from rest_framework import routers

from .views import (CouponSuccessViewSet, EventDocumentViewSet,
                    FilterNameViewSet, FridayLunchBookingCheckViewset,
                    HotelNameViewSet, LoginApiView, NameDetailsViewSet,
                    NfcCouponViewSet, NfcDetailsViewSet, OtpPostViewSet,
                    PaymentDetailsViewSet, RegisteredUsersViewSet,
                    RegisterEventViewSet, RoomTypeListViewSet,
                    TableListViewSet, UserLoginViewSet)

router = routers.DefaultRouter()
router.register(r'tablelist', TableListViewSet, base_name='table-list')
router.register(r'filtername/(?P<table_id>(\d+))/(?P<input_char>[\w\+]+)', FilterNameViewSet, base_name='filter-name')
router.register(r'namedetails', NameDetailsViewSet, base_name='name-details')
router.register(r'myregistration', RegisterEventViewSet, base_name='register-event')
router.register(r'registeredusers', RegisteredUsersViewSet, base_name='register-users')
router.register(r'roomtype', RoomTypeListViewSet, base_name='room-type')
router.register(r'user-registration', UserLoginViewSet, base_name='user_registration')
router.register(r'otp-post', OtpPostViewSet, base_name='otp_post')
router.register(r'hotel-name', HotelNameViewSet, base_name='hotel_name')
router.register(r'payment-details', PaymentDetailsViewSet, base_name='payment_details')
router.register(r'coupon-success', CouponSuccessViewSet, base_name='coupon_success')
router.register(r'event_documents', EventDocumentViewSet, base_name='event_documents')
router.register(r'nfc-coupon', NfcCouponViewSet, base_name='nfc_coupon')
router.register(r'check-nfc', NfcDetailsViewSet, base_name='nfc_list')
router.register(r'friday-lunch-check', FridayLunchBookingCheckViewset, base_name='friday_lunch_check')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^registration/', LoginApiView.as_view(), name='registration'),

]
