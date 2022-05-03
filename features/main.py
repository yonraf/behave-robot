from behave.__main__ import main as behave_main

from logic.fileReader import readFile
import time
import os

def main():
    readFile()
    time.sleep(2)
    path = os.path.join(os.path.dirname(__file__))
    print(path)
    behave_main([path])

if __name__ == '__main__':
    main()