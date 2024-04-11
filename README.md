# TextScanner
The purpose of this script is to replace a certain keyword within a text file with two
different, alternating words. For example,
"The quick brown brown brown brown brown brown brown fox jumps over the lazy dog could
receive the inputs:
> "brown"
> "a"
> "b"

and the result would be
"The quick a b a b a b a fox jumps over the lazy dog"

##Running in Python
To run this code in python, the code would need to be edited to reflect the correct path
being taken to find the target file. By default, this is a file called "targetFile.txt" 
located in the documents folder. Changing the destination will allow the script to run as 
intended.

##Running in Google Colab
To run this on Google Colab, you must connect to a python environment firstly. The file 
destinations should be removed and replaced with just the name of the text file (with 
appropriate extensions). The file you intend to change should then be uploaded to the 
environment in the files section of the contents menu. The updated file will appear here 
after refreshing this menu and can be downloaded. 