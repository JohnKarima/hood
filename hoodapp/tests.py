from django.test import TestCase
from .models import Profile, Neighbourhood, Business

class ProfileTestClass(TestCase):

    def setUp(self):
        self.new_profile = Profile(user = 'montez', bio='intricacies', profile_photo = 'selfie.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def update_profile(self):
        self.new_profile.save_profile()
        profile_id = self.new_profile.id
        Profile.update_profile(id,"test_update")
        self.assertEqual(self.caption.caption,"test_update")

    def test_delete_profile(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

   
class NeighbourhoodTestClass(TestCase):
    def setUp(self):
        self.new_neighbourhood = Neighbourhood(hood_name = 'kasarani',hood_location = 'Nairobi',family_size=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_neighbourhood, Neighbourhood))

    def test_update_neighbourhood(self):
        self.new_neighbourhood.save_neighbourhood()
        neighbourhood_id = self.new_neighbourhood.id
        Neighbourhood.update_neighbourhood(id, "test")
        self.assertEqual(self.neighbourhood.neighbourhood,"test")

    def test_delete_neighbourhood(self):
        self.neighbourhood.save_neighbourhood()
        self.neighbourhood.delete_neighbourhood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) == 0)

