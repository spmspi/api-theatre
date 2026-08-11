from django.urls import path, include
from rest_framework import routers
from theatre.views import (
    GenreViewSet,
    ActorViewSet,
    TheatreHallViewSet,
    PlayViewSet,
    ReservationViewSet,
    PerformanceViewSet,
    TicketsViewSet,
)

router = routers.DefaultRouter()

router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("theatre_hall", TheatreHallViewSet)
router.register("play", PlayViewSet)
router.register("reservation", ReservationViewSet)
router.register("performance", PerformanceViewSet)
router.register("tickets", TicketsViewSet)

urlpatterns = [
    path("", include(router.urls)),
]


app_name = "theatre"
