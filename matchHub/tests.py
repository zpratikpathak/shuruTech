from django.test import TestCase
from rest_framework.test import APIClient
from .models import Match, Team
from django.urls import reverse
from rest_framework import status
from matchHub.models import Player, Venue, Match, Team


class MatchViewSetTestCase(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        self.client = APIClient()
        self.team1 = Team.objects.create(name="Team 1")
        self.team2 = Team.objects.create(name="Team 2")
        self.venue = Venue.objects.create(name="Venue 1", location="Location 1")
        self.match = Match.objects.create(date="2022-12-31", venue=self.venue)
        self.match.teams.add(self.team1, self.team2)

    # Test for getting all matches
    def test_get_all_matches(self):
        response = self.client.get(reverse("match-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test for getting a single match
    def test_get_single_match(self):
        response = self.client.get(
            reverse("match-detail", kwargs={"pk": self.match.id})
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Create test case

    # Update test case

    # Delete test case
    def test_delete_match(self):
        response = self.client.delete(
            reverse("match-detail", kwargs={"pk": self.match.id})
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TeamViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name="Team 1")

    # Test for getting all teams
    def test_get_all_teams(self):
        response = self.client.get(reverse("team-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Test for getting a single team
    def test_get_single_team(self):
        response = self.client.get(reverse("team-detail", kwargs={"pk": self.team.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
