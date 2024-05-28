from django.contrib import admin
from matchHub.models import Team, Player, Venue, Match

# Register your models here.
# Register the models in the admin panel to view and manage the data

#  Register the Team, Player, Venue, and Match models in the admin panel
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Venue)
admin.site.register(Match)
