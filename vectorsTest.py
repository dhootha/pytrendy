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
    s1 = [1.5, 1, 56, 45, -4.5];
    s2 = [2, 4, 5, 45, -1];
    expected = [-0.5, -3, 51, 0, -3.5];
    result = Vectors.diffVectors (s1, s2)
    for i in range(len(result)):
      self.assertEqual (result[i], expected[i])

if __name__ == "__main__":
  unittest.main()
