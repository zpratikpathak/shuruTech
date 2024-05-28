from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import MatchViewSet, TeamViewSet, PlayerViewSet

# Create a router and register our viewsets to make the proper routing.
router = DefaultRouter()

# register routers with matches it contains api like /matches/ /matches/{id}/
router.register(r"matches", MatchViewSet, basename="match")

# register routers with teams it contains api like /teams/ /teams/{id}/
router.register(r"teams", TeamViewSet, basename="team")

# register routers with players it contains api like /players/ /players/{id}/
router.register(r"players", PlayerViewSet, basename="player")

urlpatterns = [
    path("", include(router.urls)),
]
