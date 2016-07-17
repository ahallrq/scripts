# scripts
Random scripts I've made. Most of which will end up being in either Python 3 or Bash.

Unless noted below or in the files themselves, all of the scripts listed are licenced under the Apache 2.0 license, so you can do pretty much whatever you want with them so long as you give proper credit.

-----

### [ticker.py](ticker.py)

This a simple ticker I made for use in i3. It's pretty janky but it works.

It basically "ticks" forward or backware by a single character every time you call `step()` returning a number of characters until it reaches the end.

See [`musicticker.py`](#musictickerpy) for an example script for a proper music ticker I made.

### [musicticker.py](musicticker.py)

A simple script that utilises the above-mentioned [`ticker.py`](#tickerpy). It calls `cmus-remote` and fetches the play state and song path which it then passes to i3blocks.

If you haven't had guessed already, it needs cmus and i3blocks.

I haven't gotten around to improving this yet but eventually I'll get around to supporting multiple players I guess.

### [fluxbox-menugen.py](fluxbox-menugen.py)

This was a fluxbox menu generator I wrote a long time ago. It had it's own repo, but it was literally just one file so I'll put it here instead.

It's pretty messy and doesn't do proper filtering, but it works.
