<h1 align="center">
🐍 Python Golang Compiler
</h1>

## Introduction

The Game Directory Compiler is a Python script designed to search for directories containing the keyword "game" within a specified source directory. It then copies these directories to a target directory, compiles any Go files (.go) found within them, and generates metadata in the form of a JSON file.

## Requirements

- Python (3.x recommended)
- Go (for compiling Go files)

## Usage

- To use the script, run it from the command line with the source directory and target directory as arguments:

  ```sh
  python3 <path_to_main_script.py> source_directory target_directory
  ```

## Project Structure

1. <b>main_script.py : </b> The main script handling the search, copy, and compilation processes.
2. <b>os_filesystem.py : </b> The module for generic file system operations
3. <b>data : </b> The parent directory with go code

## How to run

1. Clone the repo
2. Navigate to the repo

```sh
 cd repo
```

3. Run the script:

```sh
python3 <path_to_main_script.py> source_directory target_directory
```

## Configuration

- <b>PATTERN</b>: The keyword used to match directories (currently set to "game").
- <b>GO_EXTENTION</b>: The file extension for Go files (currently set to ".go").
- <b>GO_COMPILE_COMMAND</b>: The command used to compile Go files (currently set to ["go", "build"]).
