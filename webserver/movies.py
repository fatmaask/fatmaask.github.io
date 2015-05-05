# -*- coding: utf-8 -*-

import web
import json
import codecs
import time

urls=(
    '/', 'index',
    '/chart1', 'chart1',
    '/chart1_query', 'chart1_query'
)

input_file = file("sinemalar.json", "r")

data = json.loads(input_file.read())

render = web.template.render("templates" , base="base")

class index:
    def GET(self):
        
        return render.index()


class chart1:
    def GET(self):
        return render.chart1()


class chart1_query:
    def GET(self):
        result = { u'ABD':0, u'Türkiye':0, u'İngiltere':0,
                  u'Fransa':0, u'Almanya':0, 'Others': 0}
        for i in data:
            print i
            for j in i[u'production']:
                if j in [u'ABD', u'Türkiye', u'İngiltere', u'Fransa', u'Almanya' ]:
                    result[j] +=1
                else:
                    result['Others'] +=1
        return json.dumps(result)


if __name__ == "__main__":
    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ("127.0.0.1", 1234))
