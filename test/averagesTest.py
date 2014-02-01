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

import sys
sys.path.append("..")
import unittest
from averages import Averages

class averagesTest (unittest.TestCase):

  def __init__(self, testCaseNames):
    unittest.TestCase.__init__(self, testCaseNames)

  def test_ma (self):
    serie = [2, 6, 5, 7, 10, 9, 12, 5]
    expected = [5, 7, 7.75, 9.5, 9]
    movingAvg = Averages.ma (serie, 4)
    print "Length MA == length(serie) - ma order + 1 ..."
    self.assertEqual (len(movingAvg), len(serie) - 4 +1)
    print "Example values match ..."
    self.assertEqual (expected, movingAvg)
    print "MA of an empty list is another empty list ..."
    self.assertEqual (Averages.ma([], 2), [])

if __name__ == "__main__":
  unittest.main()
