import requests

base_url = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All"
htmlStrings = [];
response = requests.get(base_url, headers={'User-Agent': 'SI_CLASS'})
htmlString = response.text
htmlStrings.append(htmlString)
CACHE_DICTION = {}

for i in range (1, 12):
	new_url = base_url + "&page=" + str(i)
	response = requests.get(new_url, headers={'User-Agent': 'SI_CLASS'})
	htmlString = response.text
	htmlStrings.append(htmlString)

	print(new_url)

CACHE_DICTION["umsi_directory_data"] = htmlStrings

print(type(CACHE_DICTION))
print(len(htmlStrings))