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
        self.new_neighbourhood.save_hood()
        neighbourhood_id = self.new_neighbourhood.id
        Neighbourhood.update_hood(id, "kisumu")
        self.assertEqual(self.neighbourhood.neighbourhood,"kisumu")

    def test_delete_neighbourhood(self):
        self.new_neighbourhood.save_hood()
        self.neighbourhood.delete_hood()
        hoods = Neighbourhood.objects.all()
        self.assertTrue(len(hoods) == 0)

class BusinessTestClass(TestCase):
    def setUp(self):
        self.new_business = Business(biz_name ='Zaimet',biz_email = 'zaimet@food.com', biz_description='Eat good Live good', biz_digits='0791122323')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_update_business(self):
        self.new_business.save_business()
        business_id = self.new_business.id
        Business.update_business(id, "ZaimetKiller")
        self.assertEqual(self.business.business, "ZaimetKiller")

    def test_delete_business(self):
        self.business.save_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)