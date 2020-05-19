# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. I am an Executive Producer within the company and am creating a system to simplify and streamline your process.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.
## Password Ax2$g55mEBZCT$H
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.


- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

From within the  directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

## Roles and Permissions:
- Casting Assistant
    - Can view actors and movies

- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies

- Executive Producer
   - All permissions a Casting Director has and…
   - Add or delete a movie from the database


## Endpoints
- GET '/movies'
- GET '/actors'
- POST '/movies'
- POST '/actors'
- PATCH '/movies/<int:movie_id>'
- PATCH '/actors/<int:actor_id>'
- DELETE '/movies/<int:movie_id>'
- DELETE '/actors/<int:actor_id>'


GET '/movies'
- Fetches a dictionary of movies 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A list of movies objects, success value.

GET '/actors'
- Fetches a dictionary of actors 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A list of actors objects, success value.


POST '/movies'
- Post a movie and persist it to the database
- Request Arguments: A JSON with title, release_date  eg:{ "title":"X-Man", "release_date": "12-21-23 12:00 pm"}
- Authentication: Only the executive Executive Producer
- Returns : A success value and the id of the posted movie

POST '/actors'
- Post actor and persist it to the database
- Request Arguments: A JSON with name, age and gender  eg:{"name":"Onnys Anild Lopes Menete","age": 21,
"gender":"M"}
- Authentication: Casting Director and  Executive Producer 
- Returns : A success value and the id of the posted actor

PATCH '/movies/<int:movie_id>'
- Updates a movie data based on the id 
- Request Arguments: A JSON with title and a release_date eg: { "title":"The Movie", "release_date": "12-21-25 12:00 pm"}
- Authentication: Casting Director and  Executive Producer 
- Returns : A success value and the id of the updated movie

PATCH '/actors/<int:actor_id>'
- Updates an actor data based on the id 
- Request Arguments: A JSON with name, age and gender eg:{"name":"Alex Jordan","age": 21,
"gender":"Female"}
- Authentication: Casting Director and  Executive Producer 
- Returns : A success value and the id of the updated actor

DELETE '/movies/<int:movie_id>'
- Remove persistentle a movie from the database based on id 
- Request Arguments: id of the movie eg:'/movies/1'
- Returns: A success value and the id of the deleted movie

DELETE '/actors/<int:actor_id>'
- Remove persistentle an actor from the database based on id 
- Request Arguments: id of the actor eg:'/actors/1'
- Returns: A success value and the id of the deleted actror 

## Deploying to Heroku
Create Heroku app
In order to create the Heroku app run heroku create name_of_your_app. The output will include a git url for your Heroku application. Copy this as, we'll use it in a moment.

Now if you check your Heroku Dashboard in the browser, you'll see an application by that name. But it doesn't have our code or anything yet - it's completely empty. Let's get our code up there.

Add git remote for Heroku to local repository
Using the git url obtained from the last step, in terminal run: git remote add heroku heroku_git_url.

Add postgresql add on for our database
Heroku has an addon for apps for a postgresql database instance. Run this code in order to create your database and connect it to your application: heroku addons:create heroku-postgresql:hobby-dev --app name_of_your_application

Breaking down the heroku-postgresql:hobby-dev section of this command, heroku-postgresql is the name of the addon. hobby-dev on the other hand specifies the tier of the addon, in this case the free version which has a limit on the amount of data it will store, albeit fairly high.

Run heroku config --app name_of_your_application in order to check your configuration variables in Heroku. You will see DATABASE_URL and the URL of the database you just created. That's excellent, but there were a lot more environment variables our apps use.

Go fix our configurations in Heroku
In the browser, go to your Heroku Dashboard and access your application's settings. Reveal your config variables and start adding all the required environment variables for your project. For the purposes of the sample project, just add one additional one - ‘EXCITED’ and set it to true or false in all lowercase.

Push it!
Push it up! git push heroku master

Run migrations
Once your app is deployed, run migrations by running: heroku run python manage.py db upgrade --app name_of_your_application

That's it!
And now you have a live application! Open the application from your Heroku Dashboard and see it work live! Make additional requests using curl or Postman as you build your application and make more complex endpoints.


## Authors
Onnys Anild Lopes Menete

## Acknowledgements
I would like to thank Udacity for the well organized content of this course and mentor help, the peer chat and alumni for all help, and to my friend Doilio Matsinhe who sugested me udacity. 
