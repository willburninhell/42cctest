from django.test import TestCase
from django.core.urlresolvers import reverse
from testproj.core.models import Contact, RequestLog
from django.conf import settings


class ContactTestCase(TestCase):
    def test_fixture_loading(self):
        """All data are in"""
        #self.skipTest("Not implemented. `YET!")
        url = reverse("index")
        response = self.client.get(url)
        self.assertContains(response, "antisocial@slavutich.kiev.ua")
        self.assertContains(response, "Ihor")
        self.assertEqual(Contact.objects.count(), 1)

    def test_logging_middleware(self):
        """Test middleware that stores http requests to DB"""
        # visit some urls
        self.client.get("/")
        self.client.post("/requests/", data={"abc": "1"})
        self.assertEqual(RequestLog.objects.count(), 2)
        log0 = RequestLog.objects.all()[0]
        self.assertEqual(log0.url, "/")
        self.assertEqual(log0.method, "GET")
        log1 = RequestLog.objects.all()[1]
        self.assertEqual(log1.url, "/requests/")
        self.assertEqual(log1.method, "POST")

    def test_settings_context_processor(self):
        url = reverse("/")
        response = self.client.get(url)
        self.assertEqual(response.context['settings'], settings)
