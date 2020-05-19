import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies

#ASSISTENT_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGQ0NmQwNDdjOTBjYzU3MjZiNGIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5ODM1NTI4LCJleHAiOjE1ODk5MjE5MjcsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.dZ4L9SieMsqlbnSdEqZy5G_x5bhmKm3Br3Lwc5_o3BAaCR1FYSqBMGoxdw4Q5EXgBhVg2WHPfnvf55K4Y-AKplYvRsFZL0kFqgcmknI1TMRLGy-SV28dlZvS3aOJs6b-5QCMcNE8ZiAJsBW24ywjDudEsGZJ-dwRBbGN9uxn9owALW7DQqn8adyFMOWTICzTIsijTydJpIlznLt6y_q-3V4dcKF2sqJsR0DuaDPbGYRNCgYg71nuRsLAaklNJHuAALc3-9ud17ImN6Z3Ddj1QYdbS27tzJn02aXGL2wc3LFCvLk8Fz7xi_dWUnnNSiFsbpau_kML4TxWl5G4sd8Asg'
#DIRECTOR_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGUxYzZhMzA1NDBjZDk4NGRiNmIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5ODc1OTAzLCJleHAiOjE1ODk5NjIzMDIsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.S0acMLfF6EVPsm2yIJRxSfMbR2ZwSR5rI7Pjdc6E-LMfopnkStQRAXcHDzPeNuz0Qjhbd5HOssc1kFRGXAXAZ6M2hxjRT2vQ-0FBh-1R_X2_j4aR3d4zKYkO2Ly9Tioc9nJy_4vWM4uzKP0kEHOKFwn9SDQ2q1Y7g7LEALegeEbPZjGT4ZXyahOSy1mJPQLnfdle33qwmDavdFrGVHmBzc7LjdLp9bZpTtvTORHyG0EKw8JM9fIDQc2NTyAySWJohFzcmmKUrwc9owz4Z6U5l7MjeluEuVILC3yQJaWPMt4dp3PJbWvcqsIbW7PtDgGfqPo4WJACwA5oZOCn-VcUMQ'
#PRODUCER_TOKEN = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5ODc2MTYxLCJleHAiOjE1ODk5NjI1NjAsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.XGloWRiL01rZHcrNEeFhWhzmP5swKKy8ZBoxRl1r4qglws8qqALG8q28n6HuRxT60DbWdT_zURAxAhpDLl5XzainVzAxMEhValQ2N9WKs6yTXNlnmPz1DixGwKD1PqvHCSaSlMaFqOZQSIVm2zjfdQbim1ShT4amWFldkLlbyz7vBvEWl7xxKi7hQBn02d6zo9s0yCzpAiAzB6QeEkYoGYugxVKs7sgZIfaSIDLFTVbxptF-se3zRIANqAMpbO-NbcTpsscVkAfTJZXxDjFr5DX1gSPROyS6GIvRFn7XeiJhpK7Th8TiUjfQxIckSrLUAiWu_6IfqmBljlMfXjHhWA'

ASSISTENT_TOKEN = str('Bearer ' + os.environ['ASSISTENT_TOKEN'])
DIRECTOR_TOKEN = str('Bearer ' + os.environ['DIRECTOR_TOKEN'])
PRODUCER_TOKEN = str('Bearer ' + os.environ['PRODUCER_TOKEN'])


class CastingAgencyTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = 'agency_test'
        self.database_path = "postgres://{}:{}@{}/{}".format('onnys',
                                                             'onnys', 'localhost:5432', self.database_name)

        self.assistant = {'Content-Type': 'application/json',
                          'Authorization': ASSISTENT_TOKEN}
        self.director = {'Content-Type': 'application/json',
                         'Authorization': DIRECTOR_TOKEN}
        self.producer = {'Content-Type': 'application/json',
                         'Authorization': PRODUCER_TOKEN}
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_401_get_movies(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_404_get_movies(self):
        Movies.query.delete()
        response = self.client().get('/movies', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_movies(self):
        movie = Movies(title='The Last Man Standing',
                       release_date='12-21-23 12:00 pm')
        movie.insert()
        response = self.client().get('/movies', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_get_actors(self):
        response = self.client().get('/actors')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_404_get_actors(self):
        Actors.query.delete()
        response = self.client().get('/actors', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_get_actors(self):
        actor = Actors(name='Elsa Montanha',
                       age=21, gender='Female')
        actor.insert()
        response = self.client().get('/actors', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_delete_movie(self):
        response = self.client().delete('/movies/1', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_404_delete_movie(self):
        response = self.client().delete('/movies/100000', headers=self.producer)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_movie(self):
        movie = Movies(title='The Last Man Standing',
                       release_date='12-21-23 12:00 pm')
        movie.insert()
        movie_id = movie.id
        response = self.client().delete('/movies/'+str(movie_id)+'', headers=self.producer)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_delete_actor(self):
        response = self.client().delete('/actors/1', headers=self.assistant)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_404_delete_actor(self):
        response = self.client().delete('/actors/100000', headers=self.producer)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        actor = Actors(name='Elsa Montanha',
                       age=21, gender='Female')

        actor.insert()
        actor_id = actor.id
        response = self.client().delete('/actors/'+str(actor_id)+'', headers=self.producer)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_add_movie(self):
        response = self.client().post('/movies', headers=self.assistant,
                                      json={'title': 'My ex', 'release_date': '12-21-23 12:00 pm'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_400_add_movie(self):
        response = self.client().post('/movies', headers=self.producer,
                                      json={'title': 'My ex'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_add_movie(self):
        response = self.client().post('/movies', headers=self.producer,
                                      json={'title': 'My ex wife', 'release_date': '12-21-23 12:00 pm'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_add_actor(self):
        response = self.client().post('/actors', headers=self.assistant,
                                      json={'name': 'Elsa Montanha',
                                            'age': 21, 'gender': 'Female'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_400_add_actor(self):
        response = self.client().post('/actors', headers=self.producer,
                                      json={'age': -71, 'gender': 'Female'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_add_actor(self):
        response = self.client().post('/actors', headers=self.producer,
                                      json={'name': 'Onnys Menete',
                                            'age': 21, 'gender': 'Male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_update_movie(self):
        response = self.client().patch('/movies/1', headers=self.assistant,
                                       json={'title': 'The last ship', 'release_date': '12-21-23 12:00 pm'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_400_update_movie(self):
        movie = Movies(title='The Last Man Standing',
                       release_date='12-21-23 12:00 pm')
        movie.insert()
        movie_id = movie.id
        response = self.client().patch('/movies/'+str(movie_id)+'', headers=self.director)

        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_update_movie(self):
        movie = Movies(title='The Last Man Standing',
                       release_date='12-21-23 12:00 pm')
        movie.insert()
        movie_id = movie.id

        response = self.client().patch('/movies/'+str(movie_id) + '', headers=self.director,
                                       json={'title': 'The last ship', 'release_date': '12-21-23 12:00 pm'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_401_update_actor(self):
        response = self.client().patch('/actors/1', headers=self.assistant,
                                       json={'name': 'Onnys Menete',
                                             'age': 22, 'gender': 'Male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_400_update_actor(self):
        actor = Actors(name='Elsa Montanha', age=21, gender='Female')
        actor.insert()
        actor_id = actor.id
        response = self.client().patch('/actors/'+str(actor_id)+'', headers=self.director)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['success'], False)

    def test_update_actor(self):
        actor = Actors(name='Elsa Montanha', age=21, gender='Female')
        actor.insert()
        actor_id = actor.id
        response = self.client().patch('/actors/'+str(actor_id)+'', headers=self.director,
                                       json={'name': 'Onnys Menete',
                                             'age': 21, 'gender': 'Male'})
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    # Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
