# Casting Agency
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. I am an Executive Producer within the company and am creating a system to simplify and streamline my process.

frontend comming soon....
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

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.


- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 


## Running the server

From within the  directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
source setup.sh
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
or just:
```bash
source setup.sh 
python app.py
```

## Roles and Permissions:
- Casting Assistant
    - Can view actors and movies
        - 'get:movies'
        - 'get:actors'    
 
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
        - 'post:actors'
        - 'delete: actors'
    - Modify actors or movies
        - 'patch:actors'
        - 'patch:movies'


- Executive Producer
   - All permissions a Casting Director has and…
   - Add or delete a movie from the database
        - 'post:movies'
        - 'delete:movie'

- Note: Inssed ```setup.sh``` file we have a token for each role, you can copy and Decoded at [jwt](https://jwt.io/) to see permission for each token. 

## Deployment
The API is deployed on Heroku [project link](https://castingagencyfsnd.herokuapp.com/).

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
- Returns: A JSON with list of movies objects, success value.

```bash
curl --location --request GET 'https://castingagencyfsnd.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGQ0NmQwNDdjOTBjYzU3MjZiNGIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE2NTgzLCJleHAiOjE1OTAwMDI5ODIsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.gkuByEJFJPO8_8DoRukebvaislj1fpf0--nbmGz6SIQkilOh5UzjSsCoTMUz1w2C6jVOgVZrIqraHQyvWyVorhmiG5EKLpBsm2R3UEzlDs84hjoyYT0-AFAqb2Q2uXpqjPUpsl2-DljPxSeeQkG6Jntn8kTfAwwhqWtBNXeV9-sF4-32nu5zXtsh8CQepDWVv-CBlQ3Cv8A8yBrAd1JX3TiZS3AX5_iHg5XPaZQ2gX5sRBQMLtLsFMWVTkxBUvjQfDNjmzDYfFGzfmQB1xKNJ0wVMwhJyoFXy84XgqZVr5rv4AfPcFw8Jh5bzBh3YmVODVIyyJJYlJFeRnWJN5vayw'
```
```bash
{
    "movies": [
        {
            "id": 8,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "The Last Man Standing"
        },
        {
            "id": 9,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "My ex wife"
        },
        {
            "id": 12,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "The last ship"
        }
    ],
    "success": true
}
```

GET '/actors'
- Fetches a dictionary of actors 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A JSON with list of actors objects, success value.
```bash
curl --location --request GET 'https://castingagencyfsnd.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGQ0NmQwNDdjOTBjYzU3MjZiNGIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE2NTgzLCJleHAiOjE1OTAwMDI5ODIsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.gkuByEJFJPO8_8DoRukebvaislj1fpf0--nbmGz6SIQkilOh5UzjSsCoTMUz1w2C6jVOgVZrIqraHQyvWyVorhmiG5EKLpBsm2R3UEzlDs84hjoyYT0-AFAqb2Q2uXpqjPUpsl2-DljPxSeeQkG6Jntn8kTfAwwhqWtBNXeV9-sF4-32nu5zXtsh8CQepDWVv-CBlQ3Cv8A8yBrAd1JX3TiZS3AX5_iHg5XPaZQ2gX5sRBQMLtLsFMWVTkxBUvjQfDNjmzDYfFGzfmQB1xKNJ0wVMwhJyoFXy84XgqZVr5rv4AfPcFw8Jh5bzBh3YmVODVIyyJJYlJFeRnWJN5vayw'
```
```bash
{
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "id": 6,
            "name": "Elsa Montanha"
        },
        {
            "age": 21,
            "gender": "Male",
            "id": 12,
            "name": "Onnys Menete"
        }
    ],
    "success": true
}
```

POST '/movies'
- Post a movie and persist it to the database
- Request Arguments: A JSON with title, release_date  ```eg:{ "title":"X-Man", "release_date": "12-21-23 12:00 pm"}```
- Authentication: Only the executive Executive Producer
- Returns : A JSON with success value and the id of the posted movie
```bash
curl --location --request POST 'https://castingagencyfsnd.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"X-Man", "release_date": "12-21-23 12:00 pm"}'
```
```bash
{
    "movie id": 13,
    "success": true
}
```
POST '/actors'
- Post actor and persist it to the database
- Request Arguments: A JSON with name, age and gender  ```eg:{"name":"Lazaro Neto","age": 21,
"gender":"M"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the posted actor
```bash
curl --location --request POST 'https://castingagencyfsnd.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGUxYzZhMzA1NDBjZDk4NGRiNmIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5NzIwLCJleHAiOjE1OTAwMDYxMTksImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.IopxGPMinZW1r_cjsmGIoTNxKXjUUwHpyU5VdOwRhsVYShULI7LufJfIB1AwdXPdZZsmKQG1-sHbLIRf3Tx3BngI90wiYX6lF34hbi75IXAd7VwKnbqpe-nfY08YNtxwpflNnblLSw3EKhdB-Lngjzx04NwO8LfK8bLJIP8GaHj2NJW8z8umuif9CJgdzSFgUpCKZq2bXnMM36dQpyBdr6Jast7lBED_7cMRRslli8vZCc3W4cplDtqVZIWDQOcrW73ZDppJplIOa__Ju_diOFhvcMqb3xGzNdB0PqUAd7WGYwnr01LvLHqPGGXiz_NPZ9YaU5gqm4puceSSDf3IDg' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Lazaro Neto","age": 21,
"gender":"Male"}'
```
```
{
    "actor id": 13,
    "success": true
}
```
PATCH '/movies/<int:movie_id>'
- Updates a movie data based on the id 
- Request Arguments: A JSON with title and a release_date ```eg: { "title":"The Movie", "release_date": "12-21-25 12:00 pm"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated movie
```bash
curl --location --request PATCH 'https://castingagencyfsnd.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"The Movie", "release_date": "12-21-25 12:00 pm"}'
```
```
{
    "movie_id": 2,
    "success": true
}
```
PATCH '/actors/<int:actor_id>'
- Updates an actor data based on the id 
- Request Arguments: A JSON with name, age and gender ```eg:{"name":"Alex Jordan","age": 21,
 "gender":"Female"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated actor
```bash
curl --location --request PATCH 'https://castingagencyfsnd.herokuapp.com/actors/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Alex Jordan","age": 21,
 "gender":"Female"}'
```
```
{
    "actor id": 2,
    "success": true
}
```

DELETE '/movies/<int:movie_id>'
- Remove persistentle a movie from the database based on id 
- Request Arguments: id of the movie eg:'/movies/1'
- Returns: A JSON with success value and the id of the deleted movie
```bash
curl --location --request DELETE 'https://castingagencyfsnd.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--data-raw ''
```
```
{
    "id": 2,
    "success": true
}
```
DELETE '/actors/<int:actor_id>'
- Remove persistentle an actor from the database based on id 
- Request Arguments: id of the actor eg:'/actors/1'
- Returns: A JSON with success value and the id of the deleted actror 
```bash
curl --location --request DELETE 'https://castingagencyfsnd.herokuapp.com/actors/12' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--data-raw ''
```
```
{
    "id": 12,
    "success": true
}
```

## API Testing
To create the database for test, run
```bash
dropdb agency_test && createdb agency_test
```
Note: the above command runs on postgres, if have not installed yet [link](https://www.postgresql.org/download/)

To run the tests, run
```bash
python test_app.py
``` 
## Authors
Onnys Anild Lopes Menete

## Acknowledgements
I would like to thank Udacity for the well organized content of this course and mentor help, the peer chat and alumni for all help, and to my friend Doilio Matsinhe who sugested me udacity. 
