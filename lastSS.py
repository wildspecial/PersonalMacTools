from shutil import copy2
import glob
import os
import io
import subprocess

def write_to_clipboard(output):
    process = subprocess.Popen(
        'pbcopy', env={'LANG': 'en_US.UTF-8'}, stdin=subprocess.PIPE)
    process.communicate(output.encode('utf-8'))

#print(os.path.dirname(os.path.realpath(__file__)))
#list_of_files = glob.glob(os.path.dirname(os.path.realpath(__file__))+'/*') # * means all if need specific format then *.csv

list_of_files = glob.glob("/Users/I548535/Pictures/Screenshots/*")

latest_file = max(list_of_files, key=os.path.getctime)
latest_file_name = os.path.basename(latest_file)
latest_file_name_lowered = latest_file_name.replace('.JPG', '.jpg')
obsidian_reference = "![[" + latest_file_name_lowered +"]]"
print(obsidian_reference)

#write_to_clipboard(obsidian_reference)

list_of_files_obsidian = glob.glob('/Users/I548535/Library/Mobile Documents/iCloud~md~obsidian/Documents/TechKnowledge/*.md')
latest_file_obsidian = max(list_of_files_obsidian, key=os.path.getctime)

print(latest_file_obsidian)


copy2(latest_file, '/Users/I548535/Library/Mobile Documents/iCloud~md~obsidian/Documents/TechKnowledge/')


with open(latest_file_obsidian, "a") as myfile:
	myfile.write("\n---\n")
	myfile.write(obsidian_reference)
	myfile.write("\n")


print("hello")

