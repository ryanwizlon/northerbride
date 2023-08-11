import unittest
from gallery_project import app, db
from gallery_project.models.User import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

    def test_user_profile(self):
        response = self.app.get('/user', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_user_creation(self):
        user = User(username="testuser", email="testuser@example.com")
        self.db.session.add(user)
        self.db.session.commit()

        added_user = User.query.filter_by(username="testuser").first()
        self.assertIsNotNone(added_user)
        self.assertEqual(added_user.username, "testuser")
        self.assertEqual(added_user.email, "testuser@example.com")

    def tearDown(self):
        User.query.filter_by(username="testuser").delete()
        self.db.session.commit()

if __name__ == "__main__":
    unittest.main()