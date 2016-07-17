# ticker.py - A simple ticker script
# Copyright 2016 Andrew Hall (iownall555)
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class Ticker(object):
  def __init__(self, string, tickersize):
    self.string = ""
    self.tickersize = 0
    self.position = 0
    self.steps = 0
    self.set_string(string)
    self.set_tickersize(tickersize)
    self.reverse = False

  def set_string(self, string):
    self.string = string
    self.steps = len(string)-self.tickersize
    self.position = 0
    self.reverse = False

  def set_tickersize(self, size):
    self.tickersize = size
    self.steps = len(self.string)-size

  def start(self):
    self.position = 0

  def end(self):
    self.position = self.steps

  def step(self):
    if len(self.string) <= self.tickersize:
     return self.string

    pos = self.position
    #print("step:", pos, "of", self.steps)
    if (self.steps > pos) and not self.reverse:
      self.position += 1
      return self.string[pos:pos+1+self.tickersize]
    elif (pos > 0) and self.reverse:
      self.position -=1
      return self.string[pos-1:pos+self.tickersize]
    else:
      return False
