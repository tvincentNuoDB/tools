import requests

r = requests.get('https://api.github.com/orgs/nuodb/repos?per_page=100', auth=('GitHub_Username', 'GitHub_Password'))
data = r.json()

csv = "Repo name|Repo description|Language|URL|Private|Last Updated\n"

for repo in data:

	desc = repo['description']
	desc = desc if desc != None  else "None"

	lang = repo['language']
	lang = lang if lang != None else "None"

	time = repo['pushed_at'].replace("T", " ").replace("Z", "")

	csv += repo['name'] + '|' + desc +  '|' + lang + '|' + repo['url'] + '|' + str(repo['private']) + '|' + time + "\n"

f = open('data.csv', 'w')
f.write(csv.encode('utf8'))
f.close()
