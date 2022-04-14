#prints basic instructions
print("Welcome to the Snyk Vulnerability DB API Search Tool")
print("To use this tool, type in which package or vulnerability you are looking for")

#pulls dependancies into the script
import requests
import json

#user input to query which package/vuln they want to look for
query = input("Enter which vuln/package you are looking for: ")
type = input("What package manager do you want to search by? [use 'any' by default for all results]: ")

#calling out to the api and putting it as a variable of 'response'
response = requests.get("https://security.snyk.io/api/listing?q=" + query +"&type=" + type + "&pageNumber=1")

#formatting json objects to be more pleasing on the eye
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=3)
    print(text)

#prints results of our json    
jprint(response.json())

#prints end of query
print("Query complete. Results found above!")

#testcommit