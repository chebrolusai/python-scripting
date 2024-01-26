import os
import shutil

def create_absolute_path(path): 

    presentWorkingDirectory = os.getcwd()

    # if the absolute path was already given, ignore this step
    if presentWorkingDirectory not in path:

        absoluteSourcePath = os.path.join(presentWorkingDirectory,path)

        return absoluteSourcePath

# takes the source and pattern to match with along with a boolean to determine if case insensitive match has to be done
def get_first_level_matching_directories(source, pattern, caseInsensitive):

    matchedDirectoresList = []

    for dirPath, directories, files in os.walk(source):

        for directory in directories:

            if pattern in directory:

                matchedDirectoresList.append(os.path.join(dirPath,directory))

            elif caseInsensitive and pattern.lower() in directory.lower():

                matchedDirectoresList.append(os.path.join(dirPath,directory))
        
        # first level search complete
        break
    
    return matchedDirectoresList 

def create_directory(directory):
    os.mkdir(directory)

# copies the directories and the contents to target, overwrites target if present already
def copy_dirs_to_target_directory( directoriesPath, target ):

    if not os.path.exists(target):

        create_directory(directory=target)

    elif len(directoriesPath) and os.path.exists(target):

        shutil.rmtree(target)
    
    for directory in directoriesPath:
        
        _,dirName      = os.path.split(directory)
        destinationDir = os.path.join(target,dirName)
        shutil.copytree(directory,destinationDir)
    
