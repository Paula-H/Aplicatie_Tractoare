from unittest import TestCase
from domain.tractor import Tractor
from infrastructure.repository_tractor import RepositoryTractor


class TestRepositoryTractor(TestCase):
    def setUp(self):
        access_way = "test_repository.txt"
        self.repository_tractor = RepositoryTractor(access_way)

    def test_get_all_tractoare(self):
        self.assertEqual(self.repository_tractor.get_all_tractoare()==[])

    def test_add_tractor(self):
        tractor = Tractor(2,"tractor2",1900,"model1","01:10:2008")
        self.repository_tractor.add_tractor(tractor)
        self.assertEqual(len(self.repository_tractor.get_all_tractoare()),1)
        self.assertNotEqual(len(self.repository_tractor.get_all_tractoare()), 0)

    def test_search_tractor(self):
        tractor = Tractor(2, "tractor2", 1900, "model1", "01:10:2008")
        another_tractor = Tractor(3, "tractor1", 1900, "model2", "01:10:2008")
        searched_tractor = self.repository_tractor.search_tractor(2)
        self.assertEqual(searched_tractor,tractor)
        self.assertNotEqual(searched_tractor,another_tractor)

    def test_delete_tractor(self):
        self.repository_tractor.delete_tractor(2)
        self.assertEqual(len(self.repository_tractor.get_all_tractoare()),0)
        self.assertNotEqual(len(self.repository_tractor.get_all_tractoare()), 1)
