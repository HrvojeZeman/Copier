import os
import sys

WorkingDirectory = os.path.abspath(os.getcwd())
AuthToken = "Auth"
print(os.listdir(WorkingDirectory))
print(WorkingDirectory)
input("Press Enter to exit.")
sys.exit(1)