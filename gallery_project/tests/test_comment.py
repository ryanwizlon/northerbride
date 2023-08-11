import unittest
from gallery_project import app, db
from gallery_project.models.Comment import Comment
from gallery_project.models.User import User
from gallery_project.models.Artwork import Artwork

class TestComment(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db

        self.user = User(username='testuser', email='testuser@test.com')
        self.db.session.add(self.user)
        self.db.session.commit()

        self.artwork = Artwork(title='testartwork', description='test description', community='test community', image_url='test_url')
        self.db.session.add(self.artwork)
        self.db.session.commit()

    def test_comment_post(self):
        response = self.app.post('/comment', data=dict(
            user_id=self.user.id,
            artwork_id=self.artwork.id,
            content='test comment'
        ), follow_redirects=True)

        comment = Comment.query.filter_by(content='test comment').first()
        self.assertIsNotNone(comment)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

if __name__ == "__main__":
    unittest.main()