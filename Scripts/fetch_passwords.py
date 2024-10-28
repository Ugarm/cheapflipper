import sys
import os

def fetchPasswordList(passwordlistFileName):
    data_folder_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../Data'))
    passwordlistFilePath = os.path.join(data_folder_path, passwordlistFileName)

    with open(passwordlistFilePath, 'r') as file:
        passwordlist = [line.strip() for line in file]
    return passwordlist
