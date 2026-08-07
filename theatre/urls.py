from django.urls import path, include
from rest_framework import routers
from theatre.views import GenreViesSet, ActorViewSet, TheatreHallViewSet, PlayViewSet, ReservationViewSet, \
    PerformanceViewSet

router = routers.DefaultRouter()

router.register("genres", GenreViesSet)
router.register("actors", ActorViewSet)
router.register("theatre_hall", TheatreHallViewSet)
router.register("play", PlayViewSet)
router.register("reservation", ReservationViewSet)
router.register("performance", PerformanceViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


app_name = "theatre"