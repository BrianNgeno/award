from django.test import TestCase
from .models import Profile,Project,Rate
import datetime as dt
# Create your tests here.
class ProjectTestCLass(TestCase):
    '''
    setup self instance of project
    '''
    def setUp(self):
        self.post = Project(project_name='awward',project_url='www.awards.com',location='kenya')
    
    ''' 
    test instance of project
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Project))


    '''
    test save project
    '''

    def test_save_image(self):
        self.post.save_project()
        project = Project.objects.all()
        self.assertTrue(len(project)>0)

class profileTestCLass(TestCase):
    '''
    setup self instance of profile
    '''
    def setUp(self):
        self.prof = Profile(Bio='Live the moment')
    
    ''' 
    test instance of profile
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_profile(self):
        self.prof.save_profile()
        bio = Profile.objects.all()
        self.assertTrue(len(bio)>0)

class RateTestCase(TestCase):
    '''
    setup
    '''
    def setUp(self):
        self.rate = Rate(design='2',usability='4',content='8',average='4.56',project='2')
    '''
    test instance of rate
    '''
    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rate))
        '''
        test for save instance of rate
        '''
    def test_save_rate(self):
        self.rate.save_rate()
        name = Rate.objects.all()
        self.assertTrue(len(name)>0)
    
