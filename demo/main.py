## import
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv() #take environment variables from .env

"""
Directory structure:
.
|-- .env
|-- main.py
"""

def add(a:int, b:int)->int:
    return a+b


def write_db(data:int)->None:
    print(f"Atttempting to write to db:{os.environ.get('DATABASE_URL')} wiht \n \t user {os.environ.get('DATABASE_USER')}")
    sleep(2)
    return 

def main():
    nums1=input("Enter a number: ")
    nums2=input("Enter another number: ")
    result=add(nums1, nums2)
    write_db(result)

if __name__=="__main__":
    main()