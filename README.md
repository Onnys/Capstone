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


## Authors
Onnys Anild Lopes Menete

## Acknowledgements
I would like to thank Udacity for the well organized content of this course and mentor help, the peer chat and alumni for all help, and to my friend Doilio Matsinhe who sugested me udacity. 
