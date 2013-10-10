from django.test import TestCase
from django.core.urlresolvers import reverse
from testproj.core.models import Contact


class ContactTestCase(TestCase):

    def test_fixture_loading(self):
        """All data are in"""
        #self.skipTest("Not implemented. `YET!")
        url = reverse("index")
        response = self.client.get(url)
        self.assertContains(response, "antisocial@slavutich.kiev.ua")
        self.assertContains(response, "Ihor")
        self.assertEqual(Contact.objects.count(), 1)

