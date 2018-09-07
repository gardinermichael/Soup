import sys
from bs4 import BeautifulSoup
sys.path.append('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents/util/hellpaz')
from logg import *
from stax import *


import os,glob
base_dir = os.getcwd()
base_dir += "/data/"

#os.path.isfile("bob.txt") # Does bob.txt exist?  Is it a file, or a directory?
#os.path.isdir("bob")

with LoggingPrinter(appendModeFileName=None):
	csv_dictionary = dict()
	for folder_name in os.listdir(base_dir):
		folder_path = base_dir + folder_name
		if os.path.isdir(folder_path):
			csv_dictionary[folder_name] = {
				"folder_path": str(folder_path + "/"),
				"header": list(),
				"rows": list()
			}
		
	#print(csv_dictionary)
			
	
	
	
	if "travis_clerk_civil" in csv_dictionary:
		print(csv_dictionary["travis_clerk_civil"])
		folder = csv_dictionary["travis_clerk_civil"]
		folder_path = folder['folder_path']
		print(folder_path)
		
		for filename in os.listdir(str(folder_path)):
			file_path = folder_path + filename
			print(file_path)
			html = open(file_path, 'r', encoding='utf-8')
			html_soup = BeautifulSoup(html, "html5lib")
			#rows = html_soup.select("div.results")
			print(html_soup)
			break
		
		
		

	


# you tell the csv parser what columns to look for and it finds them and figures out automatically how to parse it based on the columns you're asking for
