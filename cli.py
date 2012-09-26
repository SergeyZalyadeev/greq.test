import grequests
import sys, datetime

def main(*args):
	urls = [
		'http://localhost:8000/test?timeout=10&name=req1',
		'http://localhost:8001/test?timeout=9&name=req2',
		'http://localhost:8002/test?timeout=8&name=req3',
		'http://localhost:8003/test?timeout=7&name=req4',
		'http://localhost:8004/test?timeout=6&name=req5',
		'http://localhost:8004/test?timeout=5&name=req6',
		'http://localhost:8003/test?timeout=4&name=req7',
		'http://localhost:8002/test?timeout=3&name=req8',
		'http://localhost:8001/test?timeout=2&name=req9',
		'http://localhost:8000/test?timeout=1&name=req0',
	]
	
	print datetime.datetime.now()
	
	rs = (grequests.get(u) for u in urls)
	for res in grequests.imap(rs, size=10):
		print datetime.datetime.now()
		print res.text
		
	print datetime.datetime.now()

if __name__ == '__main__':
	main(*sys.argv[1:])
