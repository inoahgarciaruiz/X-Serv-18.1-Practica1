#!/usr/bin/python3

"""
    Practica 1.

"""

import webapp

class URL_short(webapp.webApp):

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""
        method = request.split()[0]
        resource = request.split()[1].split("/")[1]
        print("Method:", method)
        print("Resource:", resource)
        return (method, resource)

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        if parsedRequest[0] == "GET":
            return("200 OK", "<html><head><title>Ejemplo de formulario "\
                   "sencillo</title></head><body><h3>This app shorts URLs "\
                   "</h3><form action='http://localhost:1234'method='POST'>"\
                   "URL:<input type='text' name='url' value=''"\
                   " /><br/><input type='submit' value='Send' /></form>"\
                   "</body></html>")
        else:
            return ("200 OK", "<html><body><h1>Not a GET!</h1></body></html>")


if __name__ == "__main__":
    testWebApp = URL_short("localhost", 1234)
