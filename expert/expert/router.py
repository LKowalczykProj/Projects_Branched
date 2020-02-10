from genie.viewset import ActorViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Actor',ActorViewSet,basename='Actor')