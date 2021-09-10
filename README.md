# DjangoGame
DjangoGame is my very basic web app built in Django+SQlite.

## Features
1. Login, Log out, Register, Reset password.
2. Update Profile and password.
3. Section Play User generate a random score from 1 to 1 million.
4. Section Ranking you can see top 10 user leaderboard score.

## Usability
To run the project, you need to have Docker and Docker Compose installed.

```
docker-compose up
```
port 8000

localhost:8000

This project have initial data that you can load with this command :

```python
python manage.py loaddata initial_data/user.json 
```

