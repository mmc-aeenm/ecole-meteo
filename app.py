#!/usr/bin/python3
#coding: utf-8


import mimetypes
import os


import controller


def application(env, start_response):

    website = ''

    ### ETAPE 1 : Parsing url
    url = env['REQUEST_URI']
    if len(url) > 1:
    	actions = url.strip('/').split('?')[0]
    	actions = actions.split('/')
    else:
    	actions = None
    if '?' in url:
    	li_parameters = (url.strip('/').split('?')[1]).split('&')
    	parameters = {}
    	for parameter in li_parameters:
    		name = parameter.split('=')[0]
    		value = parameter.split('=')[1]
    		parameters[name] = value
    else:
    	parameters = None

    ### ETAPE 2 : Rooting
    # 2 possibilités : afficher un fichier/afficher une page web
    app_controller = controller.Controller()
    if actions == None:
    	content = app_controller.index()
    elif hasattr(app_controller, "_".join(actions).replace('-', '_')):
    	content = getattr(app_controller, "_".join(actions).replace('-', '_'))()
    elif os.path.exists('view/' + "/".join(actions) + '.html'):
        content = app_controller._view("/".join(actions))
    elif os.path.exists('view/' + "/".join(actions) + '/index.html'):
        content = app_controller._view("/".join(actions) + '/index')
    elif actions != None and '.' in actions[-1]:
        mmtype, charset = mimetypes.guess_type(url[1:])

        if mmtype != "" :
            if mmtype == "video/mp4":
                code = "206"
            else:
                code = "200"
            start_response(code + ' OK', [('Content-Type', mmtype)])
            with open(url[1:], 'rb') as f:
        	    website = f.read()
        elif (actions[-1].split('.'))[-1] == "heif":
            from PIL import Image
            import pyheif

            heif_file = pyheif.read(url[1:])
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data,
                "raw",
                heif_file.mode,
                heif_file.stride,
                )
            buf = io.BytesIO()
            image.save(buf, format='PNG')
            start_response('200 OK', [('Content-Type', 'text/html; charset="utf-8"')])
            website = "aa".encode('utf-8')
        return website
    else:
    	content = app_controller._error('404')


    ### ETAPE 3 : Creating title
    if actions is not None:
        title = content[content.find('<h1>')+4:content.find('</h1>')]
    else: 
        title = 'accueil'

    title = title.capitalize()[0] + title[1:]


    ### ETAPE 4 : Loading file
    start_response('200 OK', [('Content-Type','text/html; charset="utf-8"')])
    # website += str(env['wsgi.input'].readline())
    website += app_controller._view('layout/default', **{"title": title, "content": content})
    return website.encode('utf-8')