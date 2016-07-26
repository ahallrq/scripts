#!/bin/python

# MIT License
# 
# musicticker.py - A simple music ticker script
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

import time, os
from datetime import datetime as dt
from ticker import Ticker

print('[{"full_text":"  Idle"}],')

pausecount = 0

t = Ticker("", 25)

icon = {
           "stopped": "  ",
           "playing": "  ",
           "paused": "  ",
           "idle": "  "
       }

def push_i3_msg(state, msg):
  print('[{"full_text":"%s%s"}],' % (icon[state], msg))

def get_cmus_status():
  s = os.popen("cmus-remote -Q").read()
  if s == "":
    return None
  else:
    s = s.splitlines()
    d = {}
    d["set"] = {}
    for i in s:
      j = i.split(" ", 1)
      if j[0] == "set":
        j = i.split(" ", 2)
        d["set"][j[0]] = j[1]
      else:
        d[j[0]] = j[1]
    return d

while True:
  status = get_cmus_status()
  if status is None:
    push_i3_msg("idle", "Idle")
    time.sleep(1)
  elif status["status"] == "stopped":
    push_i3_msg("stopped", "Stopped")
    time.sleep(1)
  elif status["status"] == "playing" or status["status"] == "paused":
    if status["file"] != t.string:
      t.set_string(status["file"])
    if pausecount < 2 and status["status"] == "paused":
      pausecount += 1
    elif pausecount == 2 and status["status"] == "paused":
      push_i3_msg(status["status"], "----------Paused----------")
      pausecount = 0
      t.step(); t.step()
      time.sleep(1)
    msg = t.step()
    if msg is False:
      #t.reverse = not t.reverse
      time.sleep(1)
      t.start()	
    else:
      push_i3_msg(status["status"], msg)
      time.sleep(0.5)
