import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.api import urlfetch

import webapp2
# import urllib.parse as up
# import urllib.request


class MainPage(webapp2.RequestHandler):

    def get(self):



        sentence = self.request.get("sentence")   # get the sentence from the text field

        if sentence:
            argument = [("q", sentence)]         # formats it as a proper url argument
            encoded_args = urllib.urlencode(argument)
            finalUrl = "http://ec2-54-191-21-155.us-west-2.compute.amazonaws.com/cgi-bin/sentiment.cgi?" + encoded_args
            data = urlfetch.fetch(finalUrl)
            value = float(data.content)

            color = self.getColor(value)

        else:
            # empty sentence - no need to analyze it
            #value = 0.0
            color = "#DECE2F"

        self.response.out.write(color)


        # if self.request.get("usernameInput") == "admin" and self.request.get("passwordInput") == "admin":
        #     self.redirect("https://www.maharsh.net", True)
        #
        # else:
        #     self.response.write("<html><body><h1>Invalid Password</h1><br></body></html>")

    def getColor(self, value):
        sections = [(-0.9,"#CF0F02"), (-0.8,"#D02706"), (-0.7,"#D23E0B"), (-0.6,"#D45410"), (-0.5,"#D56A15"), (-0.4,"#D77F1A"), (-0.3,"#D9941F"), (-0.2,"#DBA823"), (-0.1,"#DCBB29"), (0,"#DECE2F"), (0.1,"#E0E034"), (0.2,"#D2E23A"), (0.3,"#C5E33F"), (0.4,"#B8E545"), (0.5,"#ADE74B"), (0.6,"#A2E950"), (0.7,"#98EA56"), (0.8,"#8EEC5C"), (0.9,"#86EE62"), (1,"#7FEF68")]

        for item in sections:
            if value <= item[0]:
                color = item[1]
                break   # found the matching section - exit out of loop

        return(color)

app = webapp2.WSGIApplication([
    ('/sentiment', MainPage),
], debug=True)
