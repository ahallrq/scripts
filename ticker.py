# MIT License
# 
# ticker.py - A simple ticker script
# Copyright (c) 2016 Andrew Hall (iownall555)
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
