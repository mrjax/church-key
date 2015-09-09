# church-key
Opens relative and absolute files and URLs in Sublime Text 2


Given the following folder/file structure:
C:/Users/user/Desktop/TestFolder
...../subFolder
..........file.txt
..........2nd file.txt
...../2nd subFolder
..........myJam.mp3
.....siblingFile.txt
.....photo.jpg
.....youAreHere.txt

Where you have youAreHere.txt open,..

: Click in this:...	:		| : and [ctrl + u] will:...	:		| :	Because it is.. :
-------- | ------- | -----
C:/Users/User/Desktop		| Open folder in Explorer			| 	Absolute path to directory
siblingFile.jpg 			| Open file in notepad/Sublime		| Relative path to Within containing folder of current file
/photo.jpg 					| Open image in Photo Viewer		| 	Link works with/without extra "/"s
/subFolder					| Open folder in Explorer			| 	Relative path to directory within containing folder of current file
/subFolder/file.txt 		| Open file in notepad/Sublime 		| Relative path works
/subFolder/2nd file.txt 	| Open file in notepad/Sublime		| Folder name will accept 2 following spaces, see Config Section




explain spaces work after cursor
explain from noacad/open-url



