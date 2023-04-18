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

if __name__ == '__main__':
    unittest.main()
