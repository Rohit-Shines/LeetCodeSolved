# Imagine I am a customer and you are implementing an API for me.
# My first requirement is to implement an API (or command line utility)
# that will give me a list of files in the given directory whose name contain the given string.
# Design the API and internal objects, including the file system API,
# if you want to use your own or you do not remember the one in your programming language.
# Once this is done, additional criteria will be introduced and
# I will see how you can deal with change and how extensible your code is.
# List<MyFile> find(MyDirectory directory, String str) { /* ... */ }
# https://www.w3schools.com/python/python_ref_string.asp

# import OS module
import os

# Get the list of all files and directories
path = "/Users/rohitkumargundu/Downloads/W3 Project"
print("Directories in path===",os.listdir(path)) # this function gives the list

# to get specific file extension
for x in os.listdir(path):
	if x.endswith(".html"):
		print("Extension in path=====",x)

# search for specific files
for k in os.listdir(path):
	if "800" in k:
		print(k)



