#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        #pprint.pprint(got_dj)

        print(f"\nSelected GoT character number # {got_charToLookup} is {got_dj['name']}\n")
        
        print(f"Houses {got_dj['name']} belongs to:")
        for house in got_dj["allegiances"]:
            print(f"\t{house}")
        print("\n")

        print(f"Book {got_dj['name']} mentioned in:")
        for book in got_dj["books"]:
            print(f"\t{book}")
        for book in got_dj["povBooks"]:
            print(f"\t{book}")

        print("\n")

if __name__ == "__main__":
        main()

