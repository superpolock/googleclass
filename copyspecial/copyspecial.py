#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
def getSpecialFiles(dir):
  specialFiles = []
  commandToExecute = "ls -1 "+dir
  print "About to execute: " + commandToExecute
  (status, filenames) = commands.getstatusoutput(commandToExecute)
  print "filenames",filenames
  print "status",status
  if 0 == status:
    for filename in filenames.split('\n'):
      print "Testing filename: ",filename
      match = re.search("__\w+__",filename)
      if match:
        print "Matched",match.group()
        specialFiles.append(filename)
  return specialFiles

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  # +++your code here+++
  # Call your functions
  for directory in args:
    matchingFiles = getSpecialFiles(directory) 
    if tozip:
      commandLineToExecute = "zip -j "+tozip+matchingFiles.join(" ")
      print "Gonna run: "+commandLineToExecute
    elif todir:
      # todo: Need to create the direcotry if it doesn't exist
      for filename in matchingFiles:
        commandLineToExecute = "cp "+filename +" "+todir
        print "Executing '"+commandLineToExecute+"'"
        (status, output) = commands.getstatusoutput(commandLineToExecute)
        print "Status: "+str(status)
        print "Output: "+output
        

if __name__ == "__main__":
  main()
