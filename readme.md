# Installation

## PreRequisite
Python >=3.10

## Install via Poetry
Run the below command
```python
poetry install
```
Note: make sure you have installed poetry. `pip install poetry`

OR

## install via requirements.txt
Run the below commands
```python
pip install -r requirements.txt
```

## How to run
```python
python manage.py runserver
```


# API Endpoints

## Api Docs available at
- [http://127.0.0.1:8000/api/docs/](http://127.0.0.1:8000/api/docs/)

## Read Only docs available at
- [http://127.0.0.1:8000/api/redocs/](http://127.0.0.1:8000/api/redocs/)

## Schema
- `GET /api/schema/`: Retrieve the schema of the API.

## Matches
**Note** Make sure you create team and then playerfirst and then create matches
**Pro Tip**: Use django admin to add some player and team data

If you have any trouble with data check out admin page once
- `GET /matches/`: Retrieve a list of all matches.
- `POST /matches/`: Create a new match.
- `GET /matches/{id}/`: Retrieve the details of a match with the given ID.
- `PUT /matches/{id}/`: Update the details of a match with the given ID.
- `PATCH /matches/{id}/`: Partially update the details of a match with the given ID.
- `DELETE /matches/{id}/`: Delete a match with the given ID.
<!-- - `POST /matches/add/`: Add a new match.  removed since same can done by sendin post request on /matches-->
- `GET /matches/past_matches/`: Retrieve a list of all past matches.

## Players
- `GET /players/`: Retrieve a list of all players.
- `POST /players/`: Create a new player.
- `GET /players/{id}/`: Retrieve the details of a player with the given ID.
- `PUT /players/{id}/`: Update the details of a player with the given ID.
- `PATCH /players/{id}/`: Partially update the details of a player with the given ID.
- `DELETE /players/{id}/`: Delete a player with the given ID.

## Teams
- `GET /teams/`: Retrieve a list of all teams.
- `POST /teams/`: Create a new team.
- `GET /teams/{id}/`: Retrieve the details of a team with the given ID.
- `GET /teams/{id}/team_performance/`: Retrieve the performance of a team with the given ID.


## Admin Login
URL = [http://127.0.0.1:8000/admin/)](http://127.0.0.1:8000/admin/)
Username = admin
Password = 123456