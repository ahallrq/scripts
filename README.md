# scripts
Random scripts I've made. Most of which will end up being in either Python or Bash.

Unless noted below or in the files themselves, all of the scripts listed are licenced under the Apache 2.0 license, so you can do pretty much whatever you want with them so long as you give proper credit.

-----

### ticker.py

This a simple ticker I made for use in i3. It's pretty janky but it works.

It basically "ticks" forward or backware by a single character every time you call `step()` returning a number of characters until it reaches the end.

See `musicticker.py` for an example script for a proper music ticker I made.

### musicticker.py

A simple script that utilises the above-mentioned `ticker.py`. It calls `cmus-remote` and fetches the play state and song path.

I haven't gotten around to improving this yet but eventually I'll get around to supporting multiple players I guess.
