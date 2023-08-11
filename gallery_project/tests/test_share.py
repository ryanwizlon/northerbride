import unittest
from gallery_project import app, db
from gallery_project.models import Artwork, User, Share

class TestShare(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

        self.user = User(username='testuser', email='testuser@test.com')
        self.artwork = Artwork(title='Test Artwork', description='This is a test artwork', community='Test Community')
        self.share = Share(user_id=self.user.id, artwork_id=self.artwork.id)

        self.db.session.add(self.user)
        self.db.session.add(self.artwork)
        self.db.session.add(self.share)
        self.db.session.commit()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def test_artwork_share(self):
        response = self.app.get('/share', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Artwork', response.data)

if __name__ == "__main__":
    unittest.main()