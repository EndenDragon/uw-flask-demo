#!/usr/bin/env python3

## This script contains the CGI configuration required to serve up your Flask
## web application from itself. Used with the provided .htaccess file,
## you can serve up your site from a directory.
## It works by making your installed PIP packages avaliable from
## a given folder and then importing your project so that it may be executed.

## Making installed PIP packages avaliable to be imported in Python
# PIP Packages directory; ./pypackages means the folder called pypackages located at
# the current directory as application.cgi
PIP_PACKAGES_DIR = "./pypackages"
import sys
sys.path.insert(0, PIP_PACKAGES_DIR)

## Sets the directory so urls all match up. 
# Auto-generated urls using url_for() method would correctly remove application.cgi from
# the path. Flask reads SCRIPT_NAME environment variable to determine how to build urls.
import os
os.environ['SCRIPT_NAME'] = os.environ['SCRIPT_NAME'][:-1 * len(os.path.basename(__file__))]

## cgitb handles displaying tracebacks
#  Sometimes errors happen which prevents the site from being
#  imported and executed. cgitb collects error messages and
#  formats for the browser to display the errors.
import cgitb
cgitb.enable(format="text")
try:
    ## Import your Flask site
    # Change this line to point to the Flask's app object.
    # from flaskapp import app -> means read flaskapp.py
    # and get the app object. Keep the "as application" part
    # intact so later parts of the code will be able to refer by
    # this variable.
    from flaskapp import app as application ### CHANGE THIS!

    ## Import CGIHandler object that will run your Flask site.
    #  Flask is written so that it follows Python Web Server
    #  Gateway Interface (WSGI). Because of this, many server
    #  software that can interpret Python may run any Flask site.
    #  Python's built in wsgiref package allow running WSGI web applications
    #  in a CGI environment. (i.e. UW student web publishing can run CGI scripts)
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(application)
except:
    ## Handle any error when importing Flask app in a useful traceback
    ## back to the browser.
    print("Status: 500 Internal Server Error\n")
    print(cgitb.text(sys.exc_info()))
