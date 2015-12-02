
import sublime, sublime_plugin
import os, sys, webbrowser, urllib

class ChurchKeyCommand(sublime_plugin.TextCommand):
	config = sublime.load_settings("Church_Key.sublime-settings")
	
	def run(self, edit): 
		dir = self.config.get("homeDirectory")
		spaces = self.config.get("spaceLimit")

		#getting input with no spaces
		input = self.selection(0)

		#Main Structure below, mostly an altered If-ifelse-else
		#if -> use single-word (no spaces) input as a url to open?
		#ifelse -> loop through number of spaces to attempt to discover a file
		#else -> use test indicator "escape" to determine that no file was opened
		#		 and thus the selection should be googled
		domains = self.config.get("domainList")
		if any(dom in input for dom in domains): 
			webbrowser.open_new_tab(input)
		else:
			index = 0
			escape = False
			while(index <= int(spaces) and escape == False):
				escape = self.openFile(self.selection(index))
				index += 1

		if escape == False:
			webbrowser.open_new_tab("http://google.com/#q=" + urllib.quote(input))

	# Pick up selection based on cursor
	# This scans left and right until it reaches an escape character, or either end of the file
	# TODO: Add more sophistication for messier input.
	# TODO: /\ poss. layered selection.  If first layer does not work, run selection() with parameter to try next layer of complexity
	def selection(self, limit):
		s = self.view.sel()[0]

		start = s.begin()
		end = s.end()
		size = self.view.size()
		count = 0

		if (start == end):
			while(start > 0 and self.view.substr(start - 1) != ' '
							and self.view.substr(start - 1) != '\n'):
				start -= 1

			while(end < size and self.view.substr(end) != '\n'):
				end += 1
				if self.view.substr(end) == ' ':
					if count == limit:
						break;
					count += 1

		return self.view.substr(sublime.Region(start, end)).strip()

	# Attempts to open file
	# This runs a series of checks in a well thought out if-elif structure to cover the file possibilities
	# TODO: Add complexity so home directory can be an array of common home directories of files
	# TODO: 
	def openFile(self, input):
		dir = self.config.get("homeDirectory")
		escape = False

		if os.path.isdir(input):
			#this is an absolute path to a directory
			os.startfile(input)
			escape = True
		elif os.path.isfile(input):
			#this is an absolute path to a file
			os.startfile(input)
			escape = True
		elif os.path.isdir(os.path.normpath(dir + "\\" + input)):
			#this is a relative dir in config.homeDirectory  /projects/ 
			os.startfile(os.path.normpath(dir + "\\" + input))
			escape = True
		elif os.path.isfile(os.path.normpath(dir + "\\" + input)):
			#this is a relative file in config.homeDirectory
			os.startfile(os.path.normpath(dir + "\\" + input))
			escape = True
		elif os.path.isdir(os.path.normpath(os.path.dirname(self.view.file_name()) + "\\" + input)):
			#this is a relative dir in directory of selection
			os.startfile(os.path.normpath(os.path.dirname(self.view.file_name()) + "\\" + input))
			escape = True
		elif os.path.isfile(os.path.normpath(os.path.dirname(self.view.file_name()) + "\\" + input)):
			#this is a relative file in directory of selection
			os.startfile(os.path.normpath(os.path.dirname(self.view.file_name()) + "\\" + input))
			escape = True

		return escape