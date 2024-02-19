# os module in python : 

# The os module in Python provides a way to interact with the operating system. 
# It offers functions for performing various tasks related to file and directory management, process management, environment variables, 
# and more. Here's an overview of some common tasks that you can perform using the os module:

# File and Directory Operations:

# List directory contents: os.listdir()
# Create directories: os.mkdir(), os.makedirs()
# Remove directories: os.rmdir(), os.removedirs()
# Rename files or directories: os.rename()
# Check if a file exists: os.path.exists()
# Get information about a file: os.stat()

# Path Manipulation:

# Join paths: os.path.join()
# Split paths: os.path.split()
# Get the basename of a path: os.path.basename()
# Get the directory name of a path: os.path.dirname()
# Check if a path is a file or directory: os.path.isfile(), os.path.isdir()

# Process Management:

# Run external commands: os.system(), subprocess.run()
# Get and set environment variables: os.getenv(), os.putenv()

# Other Utilities:

# Get the current working directory:os.getcwd()
# Change the current working directory: os.chdir()
# Get the username of the current user: os.getlogin()
# Get the size of a file: os.path.getsize()

# The os module provides a portable way of interacting with the operating system, making your Python code more platform-independent.
#  It abstracts away many platform-specific details and provides a consistent interface for performing common system-related tasks across different operating systems (such as Windows, Linux, macOS).