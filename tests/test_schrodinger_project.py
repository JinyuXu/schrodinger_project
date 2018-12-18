#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `schrodinger_project` package."""
import unittest
import pytest
import tensorflow as tf
import math
from schrodinger_project import schrodinger_project as sp

def checkEqual(a, b):
    # This function check if two given value are equal
    # input: a, b
    # output: T/F
    difference = abs(a - b)
    if difference <0.00001:
        return True
    return False

class Test(unittest.TestCase):
    
    def input_test(self):
        testinput = sp.getinput()
        self.assertEqual(testinput.c, 1)
        self.assertEqual(testinput.basis_size, 3)
        self.assertEqual(testinput.data_table[0][0],0)
    
    def LHSScalar_test(self):
        testdata1 = [[0, 0]]
        self.assertEqual(sp.calculateLHSValue(testdata1, 0, 0), 1)
    
    def v0_test(self):
        sess = tf.Session()
        testdata = sp.getinput()
        V = sp.calculateV0(testdata.data_table, testdata.size)
        with sess.as_default():
            v0 = V.numpy()
        self.assertTrue(checkEqual(v0[0,0], 6))

    def hhat_test(self):
        sess = tf.Session()
        testdata = sp.getinput()
        V = sp.calculateV0(testdata.data_table, testdata.size)
        hHat = sp.buildHHat(V, testdata.basis_size, testdata.c)
        with sess.as_default():
            h = hHat.numpy()
        self.assertTrue(checkEqual(h[1][1], 1))




'''
@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
'''
