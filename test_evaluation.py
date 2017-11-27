# -*- coding: utf-8 -*-
#####
#Lamparski Jakub, 11.11.2017
#v1.5
#Unit tests
#####

import unittest
from evaluation import csv_dict_loader, compute_total_price, sort_groups, generate_output

class EvaluationTest(unittest.TestCase):

    def test_load_data(self):
        test_loaded_dict = {'Col1': ['1','2','3'], 'Col2': ['a','b','c'], 'Col3': ['a1','b2','c3']}
        loaded = csv_dict_loader('test_dict.csv')

        self.assertEqual(loaded,test_loaded_dict) # check if the function result matches the manually rewritten result

    def test_total(self):
        test_products_dict = {'id': ['1', '2', '3'], 'price': ['10', '20', '30'], 'currency': ['PLN', 'PLN', 'nonPLN'], 'quantity': ['5','10','15']}
        test_currence_dict = {'code': ['nonPLN','PLN'], 'ratio': ['2','1']}
        test_total_list = compute_total_price(test_products_dict,test_currence_dict)
        test_member1 = (10/1.0)*5
        test_member3 = (30/2.0)*15

        self.assertEqual(test_member1,test_total_list[0]) # check if the function result matches the manually computed result
        self.assertEqual(test_member3,test_total_list[2]) # another check for full certainty

    def test_sort(self):
        test_products_dict = {'id': ['1', '2', '3', '4', '5', '6'], 'price': ['10', '20', '30', '40', '10', '10'], 'currency': ['PLN', 'PLN', 'nonPLN', 'PLN', 'nonPLN', 'nonPLN'],
                              'quantity': ['5', '10', '15', '7', '10', '12'], 'corresponding_id': ['1','2','2','1','2','1']}
        test_currence_dict = {'code': ['nonPLN', 'PLN'], 'ratio': ['2', '1']}
        test_total_list = compute_total_price(test_products_dict,test_currence_dict)
        test_match_dict = {'corresponding_id': ['1','2']}
        test_sorted = sort_groups(test_products_dict, test_total_list, test_match_dict)
        sum_total = sum(test_total_list)
        sum_sorted = sum(test_sorted[0]) + sum(test_sorted[1])

        self.assertEqual(sum_total,sum_sorted) # is the sum of list of all elements equal the sum of the two sorted sub-lists?

    def test_generate(self):
        test_sorted = [[280.0, 60.0, 50.0], [225.0, 200.0, 50.0]]
        test_match_dict = {'corresponding_id': ['1', '2'], 'limit': ['2','3']}
        test_generated = {'id': ['1','2'], 'in_total': ['340.00', '475.00'], 'average': ['170.00','158.33'], 'currency': ['PLN','PLN'], 'ignored': ['1','0']}
        generate_output(test_sorted, test_match_dict, '_test')

        self.assertTrue(csv_dict_loader('finest_test.csv')) # is it exisiting (is it loadable)?
        self.assertEqual(test_generated,csv_dict_loader('finest_test.csv')) # does it match with the example?

        
if __name__ == '__main__':
    unittest.main()
