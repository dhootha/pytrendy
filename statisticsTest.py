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

from statistics import Statistics
import unittest

class statisticsTest (unittest.TestCase):

  def __init__(self, testCaseNames):
    unittest.TestCase.__init__(self, testCaseNames)

  def test_mean (self):
    self.assertEqual (Statistics.mean([]), 0)
    self.assertEqual (Statistics.mean([0]), 0)
    self.assertEqual (Statistics.mean([2,6,5,7,10,9,12,5]), 7)

  def test_sd (self):
    self.assertEqual (Statistics.sd([]), 0)
    self.assertEqual (Statistics.sd([0]), 0)
    self.assertEqual (Statistics.sd([2,4,4,4,5,5,7,9]), 2)

if __name__ == "__main__":
  unittest.main()
