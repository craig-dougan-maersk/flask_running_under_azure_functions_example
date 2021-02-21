import logging
import os
import sys
import azure.functions as func
#from azf_wsgi import AzureFunctionsWsgi
from __app__.myflaskapp.wsgi import application

#main = func.WsgiMiddleware(application).main
def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return func.WsgiMiddleware(application).main(req, context)
