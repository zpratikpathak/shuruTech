from rest_framework import viewsets
from rest_framework.response import Response
from .models import Match, Team, Player
from .serializers import MatchSerializer, TeamSerializer, PlayerSerializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import datetime
from rest_framework import status

# Create your models here.
# 1. Develop RESTful apis that could support the below functionalities
# a. Ability to store upcoming matches
# b. Ability to retrieve list of matches to be played on a particular date
# c. Ability to retrieve details about a particular match. It should return information
# about
# i. Teams involved
# ii. Team composition
# iii. Venue
# iv. Player of the match
# d. Ability to update information after match completion
# i. Player of Match
# ii. Match result

# 2. Detailed documentation about the project. What to add can be found in the section
# below
# 3. Add the below functionalities
# a. Ability to retrieve a team’s performance till now (Number of wins & losses).
# b. Ability to retrieve all the past matches with all details
# 4. Add unit tests for the functionalities built till now.


class MatchViewSet(viewsets.ModelViewSet):
    """Match viewset to perform Databse operations on Match model"""

    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    def retrieve(self, request, *args, **kwargs):
        """get a single match instance"""
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """list all matches filter by date"""
        date = self.request.query_params.get("date", None)
        if date:
            queryset = Match.objects.filter(date=date)
        else:
            # if no date is provided return all matches
            queryset = Match.objects.all()
        serializer = MatchSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        """update match instance"""
        instance = self.get_object()
        instance.player_of_match = request.data.get("player_of_match")
        instance.result = request.data.get("result")
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    # Added this, just to have /matches/add endpoint for adding matches
    # It can also work directly sending post request to /matches/ endpoint
    # @action(detail=False, methods=["post"], url_path="add")
    # def add_match(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(
    #         serializer.data, status=status.HTTP_201_CREATED, headers=headers
    #     )
    # no longer needed as we can directly send post request to /matches/ endpoint

    @action(detail=False, methods=["get"])
    def past_matches(self, request):
        """get all past matches"""
        matches = Match.past_matches()
        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ViewSet):
    """Team viewset to perform Databse operations on Team model"""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def create(self, request):
        """create a new team"""
        serializer = TeamSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # get all teams
        queryset = Team.objects.all()
        serializer = TeamSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        # get a single team
        queryset = Team.objects.all()
        team = get_object_or_404(queryset, pk=pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)

    # adding action to make drf_specatcular to generate endpoints
    @action(detail=True, methods=["get"])
    def team_performance(self, request, pk=None):
        # get a team's performance
        team = Team.objects.get(pk=pk)
        performance = Match.team_performance(team)
        return Response(performance)

    # def past_matches(self, request):
    #     # get all past matches
    #     matches = Match.past_matches()
    #     serializer = MatchSerializer(matches, many=True)
    #     return Response(serializer.data)


# Api to create Player data
class PlayerViewSet(viewsets.ModelViewSet):
    """Player viewset to perform Databse operations on Player model"""

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def create(self, request):
        """create a new player"""
        serializer = PlayerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request):
        # get all players
        queryset = Player.objects.all()
        serializer = PlayerSerializer(queryset, many=True)
        return Response(serializer.data)
