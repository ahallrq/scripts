#!/usr/bin/python

# fluxbox-menugen.py - A menu generator for fluxbox
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

import os, glob, argparse
from operator import itemgetter

class MenuGenerator:
    def generate(self, verbose=False, quiet=False, nofbsubmenu=False, writefile=None, submenu=None):
        apps = {
                   "Multimedia" : [],
                   "Development" : [],
                   "Education" : [],
                   "Games" : [],
                   "Graphics" : [],
                   "Network" : [],
                   "Office" : [],
                   "Science" : [],
                   "Settings" : [],
                   "System" : [],
                   "Utility" : []
               }

        desktopfiledir = "/usr/share/applications"
        #rawlist = open("rawlist.txt", "w")

        for filename in glob.glob(os.path.join(desktopfiledir, "*.desktop")):
          f = open(filename, "r")
          name = ""
          execpath = ""
          cat = ""
          comm = ""

          for i in f.read().splitlines():
              string = i.split("=",1)

              if (string[0] == "Name") and (name == ""):
                name = string[1].replace("(", "[").replace(")", "]")
              elif ((string[0] == "Exec") or (string[0] == "TryExec")) and (execpath == ""):
                execpath = string[1].replace(" %u", "").replace(" %U", "").replace(" %f", "").replace(" %F", "")
              elif (string[0] == "Categories") and (cat == ""):
                cat = string[1]
              elif (string[0] == "Comment") and (comm == ""):
                comm = string[1]

          #  print("{}\n\tDescription: {}\n\tCategories: {}\n\tExec: {}\n".format(name, comm, cat, exec))
          #  print("[exec] ({}) {{{}}}".format(name, exec))

          if cat == "":
            f.close()
            continue

          #rawlist.write(name + " | " + cat + " | " + execpath + "\n")

          maincats = ["AudioVideo", "Development", "Education",
                      "Game", "Graphics", "Network", "Office", "Science", "Settings",
                      "System", "Utility"]

          for i in maincats:
              if i in cat:
                  if i == "AudioVideo":
                      i = "Multimedia"
                  elif i == "Game":
                      i = "Games"
                  apps[i].append((name, execpath))
                  if verbose == True:
                      print("Found application: {} [{}] ({})".format(name, i, execpath))

          f.close()

        #rawlist.close()

        writefile.write("[begin] (FluxBox)\n")

        for key in sorted(apps.keys()):
            if len(apps[key]) > 0:
                writefile.write("\t[submenu] ({})\n".format(key))
                for i in sorted(apps[key], key=lambda t: tuple(t[0].lower())):
                  writefile.write("\t\t[exec] ({}) {{{}}}\n".format(i[0], i[1]))
                writefile.write("\t[end]\n\n")

        count = len(apps["Multimedia"]) + len(apps["Development"]) + len(apps["Education"]) +\
                len(apps["Games"]) + len(apps["Graphics"]) + len(apps["Network"]) +\
                len(apps["Office"]) + len(apps["Science"]) + len(apps["Settings"]) +\
                len(apps["System"]) + len(apps["Utility"])

        if (quiet == False):
            print(count, "applications found.")

        if (nofbsubmenu == False):
            if submenu is None:
                writefile.write("""\
		    [separator]

		    [submenu] (FluxBox)
		    	[workspaces] (Workspaces)
			[submenu] (Styles)
		    	    [stylesdir] (~/.fluxbox/styles)
			[end]
			[config] (Configure)
			[reconfig] (Reconfig)
			[restart] (Restart)
			[separator]
			[exit] (Exit)
		    [end]""")
            else:
                writefile.write(submenu.read())

        writefile.write("\n[end]\n")

        print("Saved to", writefile.name)
        writefile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a menu file for FluxBox")

    parser.add_argument("-o", "--out",
                        metavar="file",
                        type=str,
                        help="location to save the menu file to. Default: ~/.fluxbox/menu")

    parser.add_argument("-f", "--force",
                        action="store_true",
                        help="forcefully overwrite file.")

    verbositygrp = parser.add_mutually_exclusive_group()

    verbositygrp.add_argument("-v", "--verbose",
                        action="store_true",
                        help="produce detailed output.")
    
    verbositygrp.add_argument("-q", "--quiet",
                        action="store_true",
                        help="produce no output.")    

    submenugrp = parser.add_mutually_exclusive_group()

    submenugrp.add_argument("-s", "--submenu",
                              metavar="file",
                              type=str, 
                              help="file to use as the fluxbox submenu")

    submenugrp.add_argument("-n", "--no-submenu",
                        action="store_true",
                        help="don't generate fluxbox settings submenu")

    args = parser.parse_args()

    if args.out is None:
        home = os.path.expanduser("~")
        f = home + "/.fluxbox/menu"
    else:
        f = args.out
        if os.path.isdir(f):
            if f[-1] != "/":
                f = f + "/"
            f = f + "menu"

    if os.path.isfile(f) and args.force == False:
        parser.error("The file exists and --force (-f) is not specified: " + f)

    f = open(f, "w")

    smf = None

    if args.submenu is not None:
        if os.path.isfile(args.submenu):
            smf = open(args.submenu, "r")
        else:
            parser.error("The specified submenu file doesn't exist.")

    MenuGenerator().generate(verbose=args.verbose, quiet=args.quiet, nofbsubmenu=args.no_submenu, writefile=f, submenu=smf)

