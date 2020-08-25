import requests
import json
import wikipediaapi

file_url = 'https://raw.githubusercontent.com/mledoze/countries/master/countries.json'
country_list = []

class Country:
	def __init__(self, url=file_url):
		r = requests.get(file_url)
		with open('countries_new.json', 'w', encoding='UTF-8') as f:
			f.write(r.text)
		with open('countries_new.json', encoding='UTF-8') as f:
			json_data = json.load(f)
		for country in range(len(json_data)):
			country_list.append(json_data[country]['name']['common'])

	def __iter__(self):
		return self

	def __next__(self):
		with open('Text_1.txt', 'w', encoding='UTF-8') as t:
			for country in country_list:
				result = t.write(country_name + ' - ' + wikipediaapi.Wikipedia('en').page(country_name).fullurl + '\n')
		return result

