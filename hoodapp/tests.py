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

   
