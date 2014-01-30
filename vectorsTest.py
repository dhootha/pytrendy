#!/usr/bin/env python
# Copyright 2014 Ruben Afonso, http://www.figurebelow.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from vectors import Vectors

class vectorsTest(unittest.TestCase):

  def __init__(self, testCaseNames):
    unittest.TestCase.__init__(self,testCaseNames)

  def test_diffVectors (self):
    s1 = [1.5, 1, 56, 45, -4.5]
    s2 = [2, 4, 5, 45, -1]
    expected = [-0.5, -3, 51, 0, -3.5]
    result = Vectors.diffVectors (s1, s2)
    self.assertEqual (result, expected)

  def test_powVectors (self):
    serie = [2,5,6,7.6]
    expected = [4, 25, 36, 57.76]
    result = Vectors.powVector(serie)
    self.assertEqual(result, expected)

  def test_avgVector (self):
    serie = [4,5,6,0]
    expected = 3.75
    self.assertEqual (Vectors.avgVector(serie), 3.75)
    self.assertEqual (Vectors.avgVector([]), 0)

  def test_absVector (self):
    serie = [-1, -1.4, 0, 5, 5e29, -5e4]
    expected = [1, 1.4, 0, 5, 5e29, 5e4]
    self.assertEqual (Vectors.absVector(serie), expected)
    self.assertEqual (Vectors.absVector([]), [])


  def test_divVectors (self):
    serie1 = [4.5, 4, 10, -5]
    serie2 = [2, 2, 5, -1]
    expected = [2.25, 2, 2, 5]
    self.assertEqual (Vectors.divVectors (serie1, serie2), expected)

  # This function is used in the combineVectors test
  def sumFunct(self, s1, s2):
    return s1+s2

  def test_combineVectors (self):
    serie1 = [2,3,-5,90.4]
    serie2 = [1,2,3,4]
    expected = [3,5,-2, 94.4]
    self.assertEqual (Vectors.combineVectors(serie1, serie2, self.sumFunct), expected)

if __name__ == "__main__":
  unittest.main()
