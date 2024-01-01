#!/usr/bin/env python3

import os, sys, re
import fs, shutil

class File:

	def __init__(self, file:str, name:str, type:str=None, location:str=os.getcwd(self.name)):
		self.name = file.__name__
		self.type = type # This will be the letters removed from the end of the file obj.
		# (.py, .txt, .js, .css, .jsx, .cpp, .md)
		self.location = location
		