#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

import requests

## Define URL
URL= 'http://10.6.35.235:2224/'

def main():

    """runtime code"""
    ## Call the URL
    resp= requests.get(URL).txt
    print(resp)

    ## strip the json off the 200 that was returned by our API
    ## translate the json into python lists and dictionaries
    #respinjson= resp.json()
    #print(respinjson)


if __name__ == "__main__":
    main()
