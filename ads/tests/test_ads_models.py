from django.test import TestCase
from ads.models import Type, Ad
from datetime import datetime

class AdTestCase(TestCase):
    def setUp(self):
        Type.objects.create(ad_type_text='Rent')
        Ad.objects.create (
            title='Apartment', description='Somewhere nice',
            pub_date=datetime.now(), phone='22222', price='350',
            ad_type=Type.objects.get(id=1)
        )


    def test_ad_str(self):
        ad = Ad.objects.get(id=1)
        self.assertEqual(str(ad), 'Apartment')
