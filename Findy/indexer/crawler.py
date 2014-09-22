import mechanize
from BeautifulSoup import BeautifulSoup


def launch_crawler(url):
	
	request = mechanize.Request(url)
	response = mechanize.urlopen(request)
	
	soup = BeautifulSoup(response.read())
	title = soup.find('title').contents[0]

	description = None
	keywords = None
	author = None

	try:
		description = soup.findAll('meta', {'name':'description'})[0]['content']
	except Exception, e:
		description = None
	try:
		keywords = soup.findAll('meta', {'name':'keywords'})[0]['content']
	except Exception, e:
		keywords = None
	try:
		author = soup.findAll('meta', {'name':'author'})[0]['content']
	except Exception, e:
		author = None

	return {'title':title, 'description':description, 'keywords':keywords.split(","), 'author':author} 