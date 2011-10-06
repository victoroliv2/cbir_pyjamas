import web
import json
from mimerender import mimerender

render_xml = lambda message: '<message>%s</message>'%message
render_json = lambda **args: json.dumps(args)
render_html = lambda message: '<html><body>%s</body></html>'%message
render_txt = lambda message: message

urls = (
    '/(.*)', 'Service'
)
app = web.application(urls, globals())

#http://johnpaulett.com/2008/09/20/getting-restful-with-webpy/

class Service:
    @mimerender(
        default = 'html',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
    )
    def GET(self, name):
        #http://hacks.mozilla.org/2009/07/cross-site-xmlhttprequest-with-cors/
        #http://stackoverflow.com/questions/3595515/xmlhttprequest-error-origin-null-is-not-allowed-by-access-control-allow-origin
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')

        import random
        
        return {'message': 'Hello! %d !' % random.randint(0, 1000)}

    def POST(self, name):
        web.header('Access-Control-Allow-Origin',      '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        
        data = web.data()
        images = json.loads(data)
        print images
        return {'message': "POST OK!"}

if __name__ == "__main__":
    app.run()
