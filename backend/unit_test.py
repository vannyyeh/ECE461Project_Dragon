import unittest
from database import Database
import app


class MyTestCase(unittest.TestCase):
    def test_add_user_to_database(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            username = 'Abhay Samant'
            password = 'Temp123'
            userID = 'asamant'
            response = db.add_user(username, password, userID)
            assert response.status_code == 204

    def test_get_user_project(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            userID = 'vy'
            response = db.get_user_projects(userID)
            assert response.status_code == 200

    def test_add_hardware_set(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            hwID = 'hw123'
            name = 'sampleHW'
            capacity = 100
            availability = 100
            response = db.add_hardware_set(hwID, name, capacity, availability)
            assert response.status_code == 200

    def test_db(self):
        db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
        yield db
        db.__mongodbClient.close()

    def test_hardware_set_existence(test_db):
        with app.app.app_context():
            assert test_db.hardware_set_existence("hw123") == True
            assert test_db.hardware_set_existence("hw456") == False


    def test_delete_hardware_set(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            hwID = 'hw123'
            name = 'sampleHW'
            capacity = 100
            availability = 100
            db.add_hardware_set(hwID, name, capacity, availability)
            response = db.delete_hardware_set(hwID)
            assert response.status == 201
            response = db.delete_hardware_set(hwID)
            assert response.status == 204
            
    def test_authorize_user(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            projectID = 'project12'
            userID = 'cord123'
            response = db.authorize_user(projectID, userID)
            assert response.status_code == 204

    def test_unauthorize_user_nonexistant(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            projectID = 'project12'
            userID = '7tgyubh12g763t8y1ubbhu12buy123g8671ygu2bbh12318gy7u2ibbhiu23iuygasd'
            response = db.unauthorize_user(projectID, userID)
            assert response.status_code == 204
    
    def test_login_user(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            userID = 'cord123'
            password = 'gloober400'
            response = db.login_user(userID, password)
            assert response.status_code == 200

    def test_login_user_incorrect_password(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            userID = 'cord123'
            password = 'easysqueasylemonpeasy'
            response = db.login_user(userID, password)
            assert response.status_code == 204
    
    def test_login_user_nonexistant_user(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            userID = 'cord1238y123ghb31u278ug312g3uyi1hiu123uyhuy'
            password = 'gloober400'
            response = db.login_user(userID, password)
            assert response.status_code == 400

    def test_user_join_leave_project(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            projectID='123454'
            userID = 'cord123'
            response = db.user_join_project(projectID, userID)
            assert response.status_code == 200
            response = db.user_leave_project(projectID, userID)
            assert response.status_code == 200

    def test_add_delete_project(self):
        with app.app.app_context():
            db = Database("mongodb+srv://ProjectDragonUser:Z62xa7Vhmw3kHSkd@cluster0.bpaif8q.mongodb.net/?retryWrites=true&w=majority")
            projectID='81tg827380gvbvy12387gyb1u238yvbi1u32gb'
            name='Temp Project'
            desc='This is a temporary project'
            response = db.add_project(name, desc, projectID)
            assert response.status_code == 201
            response = db.delete_project(projectID)
            assert response.status_code == 200

if __name__ == '__main__':
    unittest.main()
