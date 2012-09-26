import sys, cherrypy, time


class Root(object):

	@cherrypy.expose
	def index(self):
		return "Hello World!"
		
	@cherrypy.expose
	def test(self, timeout, name):
		time.sleep(int(timeout))
		return name
root = Root()


def main(port = 8000, *args):
	conf = {
		'global': {
			'server.socket_host': '0.0.0.0',
			'server.socket_port': int(port),
		},
	#	'/': {
	#		'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
	#	}
	}

	cherrypy.quickstart(root, '/', conf)

if __name__ == '__main__':
	main(*sys.argv[1:])