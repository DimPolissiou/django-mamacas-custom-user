from generate_secret_key import generate
from shutil import copyfile
import fileinput
import os
import sys

def get_script_dir():
	return os.path.dirname(os.path.realpath(sys.argv[0]))
	
def replaceAll(file,searchExp,replaceExp):
	for line in fileinput.input(file, inplace=1):
		if searchExp in line:
			line = line.replace(searchExp,replaceExp)
		sys.stdout.write(line)
		

dir_name = get_script_dir()
example_filename = "example_settings.py"
example_path = os.path.join(dir_name, example_filename)
settings_filename = "settings.py"
settings_path = os.path.join(dir_name, settings_filename)
copyfile(example_path, settings_path)

key = generate()
replace_string = 'Enter your secret key here!'
replaceAll(settings_path, replace_string,key)

