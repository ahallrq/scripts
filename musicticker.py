#!/bin/python

# musicticker.py - A simple music ticker script
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
