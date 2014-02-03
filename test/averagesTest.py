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

  def test_ema (self):
    series = [64.75, 63.79, 63.73, 63.73, 63.55,
              63.19, 63.91, 63.85, 62.95, 63.37,
              61.33, 61.51, 61.87, 60.25, 59.35,
              59.95, 58.93, 57.68, 58.82, 58.87]
    expected = [ 0,0,0,0,0,0,0,0,0,
                 63.682,63.254,62.937,62.743,62.290,
                 61.755,61.427,60.973,60.374,60.092,
                 59.870]
    result = Averages.ema (series, 10)
    print ("EMA-10 values match ...")
    self.assertEqual(len(result), len(expected))
    for i in range (len(result)):
      self.assertEqual (round (result[i], 3), expected[i])
    print ("EMA-1 values match (initial serie) ...")
    result = Averages.ema (series, 1)
    for i in range (len(result)):
      self.assertEqual (round(result[i], 2), series[i])

if __name__ == "__main__":
  unittest.main()
