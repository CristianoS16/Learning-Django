from rental import api_views as rental_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'friends', rental_views.FriendViewset)
router.register(r'belongings', rental_views.BelongingViewset)
router.register(r'borrowings', rental_views.BorrowedViewset)
