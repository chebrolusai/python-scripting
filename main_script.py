import os
import json
from subprocess import PIPE, run
import sys
import os_filesystem

PATTERN = 'game'
GO_EXTENTION = '.go'
GO_COMPILE_COMMAND = ["go","build"]

def create_json_metadata(filePath, directories):

    metadata = {
        "dirNames" : directories,
        "totalGames" : len(directories)
    }

    with open(filePath,"w") as file:
        json.dump(metadata,file)

def run_go_compile_command(path, goFile):
    
    command = GO_COMPILE_COMMAND + [goFile]

    currentWorkingDirectory = os.getcwd()

    os.chdir(path)

    commandRunResult = run(command, stdout=PIPE, stdin=PIPE, universal_newlines=True)

    os.chdir(currentWorkingDirectory)

    print(commandRunResult)

def compile_go_code(directoryPath):

    currentDirectory = os.getcwd()

    for root, directories, files in os.walk(directoryPath):
        
        for file in files :
            if file.endswith(GO_EXTENTION):
                run_go_compile_command(root,file)
                

    os.chdir(currentDirectory)  


if __name__ == "__main__":
    # relative to the current path, grab the source and working dir from cmd line
    argumentsList = sys.argv
    if len(argumentsList) != 3:
        raise Exception("Only source directory and target directory should be passed")
    
    sourceDir, targetDir = argumentsList[1:]

    if not os.path.exists(sourceDir):
        raise Exception("please enter an existing source directory")

    # create an absolute path from the given directories
    source = os_filesystem.create_absolute_path(path=sourceDir)
    target = os_filesystem.create_absolute_path(path=targetDir)

    matchedDirectoresList = os_filesystem.get_first_level_matching_directories(source=source,pattern=PATTERN, caseInsensitive=True)

    os_filesystem.copy_dirs_to_target_directory(matchedDirectoresList,target)

    jsonFilePath = os.path.join(target,'metadata.json')

    create_json_metadata(jsonFilePath,matchedDirectoresList)

    compile_go_code(target)