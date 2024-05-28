"""Serializers for the MatchHub app."""

"""Serializers are used to convert complex data types to Python datatypes that can then be easily rendered into JSON. """
from rest_framework import serializers
from .models import Match, Team, Player, Venue


class PlayerSerializer(serializers.ModelSerializer):
    """Player serializer to serialize Player model data to JSON format."""

    class Meta:
        """Meta class to define the model and fields to serialize."""

        model = Player
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    """Team serializer to serialize Team model data to JSON format."""

    class Meta:
        model = Team
        fields = "__all__"


class VenueSerializer(serializers.ModelSerializer):
    """Venue serializer to serialize Venue model data to JSON format."""

    class Meta:
        model = Venue
        fields = "__all__"


class MatchSerializer(serializers.ModelSerializer):
    """Match serializer to serialize Match model data to JSON format."""

    teams = TeamSerializer(many=True)
    players = PlayerSerializer(many=True)
    venue = VenueSerializer()

    class Meta:
        """Meta class to define the model and fields to serialize."""

        model = Match
        fields = "__all__"
