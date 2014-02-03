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

from vectors import Vectors
from windowOp import WindowOp

class Averages:

  # This auxiliary function is used in MA
  @staticmethod
  def sumWindow (series):
    return Vectors.avgVector (series)

  @staticmethod
  def ma (series, order):
    return WindowOp.windowOp (series, order, Averages.sumWindow)

  @staticmethod
  def ema (serie, period):
    result = []
    for i in range(period-1):
      result.append(0)
    k = (2.0/(period+1))
    initSlice = serie[0:period]
    previousDay = Vectors.avgVector(initSlice)
    result.append(previousDay)
    emaSlice = serie[period:]
    for i in emaSlice:
      previousDay = i * float(k) + previousDay * float((1-k))
      result.append(previousDay)
    return result
