import unittest
from gallery_project.main import app
from gallery_project.models.Artwork import Artwork
from gallery_project.models.Community import Community

class TestGallery(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_gallery_load(self):
        result = self.app.get('/gallery')
        self.assertEqual(result.status_code, 200)

    def test_artwork_display(self):
        artwork = Artwork.query.first()
        result = self.app.get(f'/artwork/{artwork.id}')
        self.assertEqual(result.status_code, 200)
        self.assertIn(artwork.title, result.data.decode())

    def test_community_artwork(self):
        community = Community.query.filter_by(name='Churchill, Manitoba').first()
        artwork = Artwork.query.filter_by(community_id=community.id, event='Woodstock 1969').first()
        self.assertIsNotNone(artwork)

if __name__ == "__main__":
    unittest.main()