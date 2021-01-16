from rest_framework import routers
from friends import api_views as friend_views

router=routers.DefaultRouter()
router.register(r'friends',friend_views.FriendViewset)
router.register(r'beloging',friend_views.BelongingViewset)
router.register(r'borrowing',friend_views.BorrowedViewset)