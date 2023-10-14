from unittest import TestCase
from domain.tractor import Tractor


class TestTractor(TestCase):
    def setUp(self):
        self.tractor = Tractor(3,"tractor3",2000,"model3","09:09:2009")
    def test_get_tractor_id(self):
        self.assertEqual(self.tractor.get_tractor_id(),3)
        self.assertNotEqual(self.tractor.get_tractor_id(),4)

    def test_get_tractor_denumire(self):
        self.assertEqual(self.tractor.get_tractor_denumire(),"tractor3")
        self.assertNotEqual(self.tractor.get_tractor_denumire(), "tractor4")

    def test_get_tractor_pret(self):
        self.assertEqual(self.tractor.get_tractor_pret(),2000)
        self.assertNotEqual(self.tractor.get_tractor_pret(), 2005)

    def test_get_tractor_model(self):
        self.assertEqual(self.tractor.get_tractor_model(),"model3")
        self.assertNotEqual(self.tractor.get_tractor_model(), "model4")

    def test_get_tractor_data(self):
        self.assertEqual(self.tractor.get_tractor_data(),"09:09:2009")
        self.assertNotEqual(self.tractor.get_tractor_data(),"09:10:2009")
