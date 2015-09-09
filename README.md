# church-key
Opens relative and absolute files and URLs in Sublime Text 2


|Given the following folder/file structure:|
|---------|
|C:/Users/user/Desktop/TestFolder|
|...../subFolder|
|..........file.txt|
|..........2nd file.txt|
|...../2nd subFolder|
|..........myJam.mp3|
|.....siblingFile.txt|
|.....photo.jpg|
|.....youAreHere.txt|
|
Where you have youAreHere.txt open,..

Click in this:...			|  and [ctrl + u] will:...			| 	Because it is.. 
-------- | ------- | -----
C:/Users/User/Desktop		| Open folder in Explorer			| 	Absolute path to directory
C:/Users/User/Desktop/someFile.txt | Open file in notepad/Sublime | Absolute path to file opens in default application
siblingFile.jpg 			| Open file in notepad/Sublime		| Relative path to Within containing folder of current file
/photo.jpg 					| Open image in Photo Viewer		| 	Link works with/without extra "/"s
/subFolder					| Open folder in Explorer			| 	Relative path to directory within containing folder of current file
/subFolder/file.txt 		| Open file in notepad/Sublime 		| Relative path works
/subFolder/2nd file.txt 	| Open file in notepad/Sublime		| Folder name will accept 2 following spaces, see Config Section
"querulously" 				| Google this word 					|



explain spaces work after cursor


Config Settings:
Default configurations are stored in Preferences > Package Settings > Church Key > Settings - Default
	(default config file items will be restored on package update)
User configurations are stored in Preferences > Package Settings > Church Key > Settings - User
	(user config file items will override defaults)

If you want to change a configuration, copy/paste from the default configuration file into the user configuration file and change the values as follows

{
	"homeDirectory": "",
	"spaceLimit": "2",
	"domainList": [".com", ".net", ".gov"]
}

Home directory is where a relative filepath will "start" from regardless of which file you're [ctrl+u]'ing from

Examples
if "homeDirectory": "C:/Users/User/Desktop"
then Churchkey will interpret myFile.txt as  C:/Users/User/Desktop/myFile.txt and save you some typing
	(even if you are using the shortcut from a file that is stored elsewhere)

if "homeDirectory": ""
then Churchkey will try to interpret myFile.txt in the directory of the file that you're using the shortcut from
	(but if the file isn't actually a sibling file, then it won't be there to find)


Space Limit is a costly operation that will essentially loop through the program, where if it fails to find a file with one "word", then it will try to find it with the next "word" as well, and then the next two "words"...
	so looking for /my awesome file.txt won't work at first try because the program will try to find the file "/my" which doesn't exist.
	it will then try "/my awesome", and fail of course
	finally it will try "/my awesome file.txt", and succeed.  (this is with spaceLimit set to 2)

Examples
if "spaceLimit": "0"
then "/myFile.txt" will work and "/space file.txt" will not

if "spaceLimit": "1"
then "/space file.txt" will work and "/spacey space file.txt" will not

Domain List is just the list of accepted domains to check for when defaulting to opening a tab of a URL.
	It is known that URLS will not contain spaces, thus this is the first check.  If the single "word" contains one of these domains, it will be interpretted as a URL.

Examples
if "domainList": [".com"] 
then program will just check for the text to contain ".com"

if "domainList": [".com", ".awsm", ".sweet"] 
then program will check for the text to contain ".com" or ".awsm" or ".sweet"


Configural note
Sublime configs are in JSON, so there must be a comma between items, like between [".com", ".net"] and also between lines

Behavioral notes:
I mean this plugin mostly for the case where you put the cursor between two characters of text (as opposed to selecting multiple characters), but if you highlight entire strings, it will work the same (in most cases).  
Highlighting subsegments of text will likely fail/revert to googling, as it will explicitly search for that highlighted text

Note:
I had this idea and started working on it, and then from googling around found that this guy:
https://github.com/noahcoad/open-url/
already has a pretty clean plugin for it already.  Not to be denied my first Sublime Text Plugin, I continued anyway.
(I also had a few different ideas that I wanted to implement for myself anyway)
Some of my code is similar, because I looked at his code as reference when I got stuck in a few spots on the Python

Todo:
Test "http" presence vs "https" presence

