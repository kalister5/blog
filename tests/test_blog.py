import unittest
from app.models import Blog,User
from app import db

class BloghModelTest(unittest.TestCase):
    def setUp(self):
        self.user_hazard = User(username = 'hazard',password = '1234')
        self.new_blog = Blog(name='cat',title='movie',description='moviereview',user =self.user_hazard, category='technology')

    # def tearDown(self):
    #     Pitch.query.delete()
    #     User.query.delete()

    def test_check_instance_variable(self):
        self.assertEquals(self.new_blog.name,'cat')
        self.assertEquals(self.new_blog.title,'movie')
        self.assertEquals(self.new_blog.description,'moviereview')
        self.assertEquals(self.new_blog.category, 'technology')
        # self.assertEquals(self.new_pitch.user,self.user_hazard)  

    def test_save_blog(self):
        self.new_blog.save_blog()
        self.assertTrue(len(Pitch.query.all()) >0)

    def test_get_blog_by_id(self):
        self.new_blog.save_blog()
        got_blog = Blog.get_blogs(12345)
        self.assertTrue(len(got_blog) > 0)
