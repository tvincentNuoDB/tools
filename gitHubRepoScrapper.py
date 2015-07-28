import requests, getpass

print("GitHub Username: ")
username = raw_input()

print("GitHub Password: ")
password = getpass.getpass()

r = requests.get('https://api.github.com/orgs/nuodb/repos?per_page=100', auth=(username, password))
data = r.json()

csv = "Repo name|Repo description|Language|URL|Private|Last Updated|Created\n"

for repo in data:

	desc = repo['description']
	desc = desc if desc != None  else "None"

	lang = repo['language']
	lang = lang if lang != None else "None"

	lastUpdate = repo['pushed_at'].replace("T", " ").replace("Z", "")

	created = repo['created_at'].replace("T", " ").replace("Z", "")

	csv += repo['name'] + '|' + desc +  '|' + lang + '|' + repo['html_url'] + '|' + str(repo['private']) + '|' + lastUpdate + '|' + created + "\n"

f = open('data.csv', 'w')
f.write(csv.encode('utf8'))
f.close()
