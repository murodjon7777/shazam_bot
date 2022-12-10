import requests

url = "https://shazam.p.rapidapi.com/search"

# querystring = {"term":"kiss the rain","locale":"en-US","offset":"0","limit":"5"}
querystring = {"term":"azizim","locale":"en-US","offset":"0","limit":"5"}

headers = {
	"X-RapidAPI-Key": "2d2aa9414amshf57c5c2d87a5869p1ba933jsn0fdb4c9be16e",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
edit=response


print(edit)