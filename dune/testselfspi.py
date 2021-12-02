#!/usr/bin/python3
# Lab 36, Challenge 02


import requests

## Define URL
URL= 'http://172.17.0.2:5000/'

def main():

    """runtime code"""
    ## Call the URL
    resp= requests.get(URL).text
    print(resp)


if __name__ == "__main__":
    main()
