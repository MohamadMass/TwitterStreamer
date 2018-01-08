# TwitterStreamer
Dockerized Python app that listens to twitter tweets, check if the tweets contain a keyword that you choose, then saves it inside mongodb collections.

The app is fully created using docker-compose file that contains the build flow.
it creates three containers:

  1. Mongodb Container
  2. Flask Web server Container
  3. Python Container 

**) The MongoDb container will build and run mongodb on port 27017

**) Flask web server container will build and run the flask application which listens to port: 5000 (check the docker-compose.yml file)
It will also connect to mongodb collection, and retrieve all the items fron that collection, then it will display it inside the todo.html file.

**) The Python container will build and run the myapp.py script, which uses tweepy library to listen to the twitter stream, then it will save the tweets to mongodb.

## In inrder to run this app, clone the repo, then run "docker-compose up"
it will automatically build and run the app.

