# Create your tests here.

from django.test import TestCase

from app.tags import tags


class TestTrendTemplateTags(TestCase):
    def test_color_tag(self):
        self.assertEqual("text-danger", tags.color("deaths", 20))
        self.assertEqual("text-success", tags.color("deaths", -20))

        self.assertEqual("text-danger", tags.color("confirmed", 20))
        self.assertEqual("text-success", tags.color("confirmed", -20))

        self.assertEqual("text-danger", tags.color("recovered", -20))
        self.assertEqual("text-success", tags.color("recovered", 20))

        self.assertEqual("text-danger", tags.color("death_rate", 20))
        self.assertEqual("text-success", tags.color("death_rate", -20))

    def test_arrow_tag(self):
        self.assertEqual("fa fa-angle-up", tags.arrow("deaths", 20))
        self.assertEqual("fa fa-angle-down", tags.arrow("deaths", -20))

        self.assertEqual("fa fa-angle-up", tags.arrow("confirmed", 20))
        self.assertEqual("fa fa-angle-down", tags.arrow("confirmed", -20))

        self.assertEqual("fa fa-angle-down", tags.arrow("recovered", -20))
        self.assertEqual("fa fa-angle-up", tags.arrow("recovered", 20))

        self.assertEqual("fa fa-angle-up", tags.arrow("death_rate", 20))
        self.assertEqual("fa fa-angle-down", tags.arrow("death_rate", -20))
