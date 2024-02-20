from django.test import TestCase, Client
from django.urls import reverse

import json
from cv_app.models import *


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.view_url = reverse('home')

    def test_base_view(self):
        response = self.client.get(self.view_url)
        self.assertTemplateUsed(response, 'cv_app/base.html')

    def test_index_view(self):
        response = self.client.get(self.view_url)
        self.assertTemplateUsed(response, 'cv_app/index.html')

