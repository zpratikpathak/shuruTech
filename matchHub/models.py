from django.db import models
import datetime

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

# Based on the above detail generate the models


class Team(models.Model):
    """Model to store team details"""

    name = models.CharField(max_length=100)

    def __str__(self):
        """Method to return the string representation of the team object."""
        return self.name


class Player(models.Model):
    """Model to store player details"""

    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        """Method to return the string representation of the player object."""
        return self.name


class Venue(models.Model):
    """Model to store venue details"""

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


class Match(models.Model):
    """Model to store match details"""

    date = models.DateField()
    teams = models.ManyToManyField(Team)
    players = models.ManyToManyField(Player)
    """Venue -> Match is a one to many relationship. A venue can have multiple matches but a match can only have one venue"""
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    """Player -> Match is a many to many relationship. A player can play in multiple matches and a match can have multiple players"""
    player_of_match = models.ForeignKey(
        Player, on_delete=models.SET_NULL, null=True, related_name="player_of_match"
    )
    """Result can be win, loss or draw. Hence, we use a char field to store the result of the match."""
    result = models.CharField(max_length=100, null=True)

    def team_performance(self, team):
        """Method to calculate the performance of a team in terms of wins and losses."""
        # needed to add draw also
        wins = Match.objects.filter(teams=team, result="win").count()
        losses = Match.objects.filter(teams=team, result="loss").count()
        return {"wins": wins, "losses": losses}

    # static method since it doesn't depend on the instance of match objects
    @staticmethod
    def past_matches():
        """Method to retrieve all the past matches."""
        return Match.objects.filter(date__lt=datetime.date.today())

    def __str__(self):
        """Method to return the string representation of the match object."""
        # return self.venus + " " + self.date
        return f"{self.teams.first().name} vs {self.teams.last().name} on {self.date}"
