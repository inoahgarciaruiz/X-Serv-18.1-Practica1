#!/usr/bin/python3

"""
    Practica 1.

"""

import webapp

class URL_short(webapp.webApp):


    def readCSV(self):
        """ Read CSV file containing shortened URLs."""
        URLdic = {}
        shortURLdic = {}
        try:
            csvFile = open("URLs.csv", "r")
            for line in csvFile:
                URLdic[line.split(",")[1]] = line.split(",")[0]
                shortURLdic[line.split(",")[0]] = line.split(",")[1]
            csvFile.close()
        except IOError:
            pass
        return (URLdic, shortURLdic)

    def addURL(URLdic, shortURLdic, URL):
        """ Add URLs to both dictionaries and updates CSV files."""
        idx = str(len(URLdic)) # Size of dictionaries
        URLdic[URL] = idx
        shortURLdic[idx] = URL
        line = idx + "," + URL
        csvFile = open("URLs.csv", "a")
        csvFile.append(line)
        csvFile.close()
        return (URLdic, shortURLdic)

    def GETanswer(self, resource, shortURLdic):
        """ Build an answer to a GET Request."""
        if resource != "favicon.ico":
            # Search URL in already-shortened URLs dictionary
            if resource in shortURLdic.keys():
                # HTTP Redirect
                url = shortURLdic(resource)
                return("302 Found", "<html><head><title>URL-shorter App"\
                       "</title><meta http-equiv='Refresh' content='3;"\
                       "url=" + url + "'></head><body><p>Redirecting..."\
                       "If you are not authomatically redirected, please "\
                       "click <a href='" + url + "'>here</a></p></body></html>")     
            elif resource == "":
                # Gives a form and the list of shortened URLs
                URLlist = "<ul style='list-style-type:none'>"
                for i in shortURLdic:
                    URLlist = URLlist + "<li>" + i + ": " + shortURLdic[i] + "</li>"
                URLlist = URLlist + "</ul>"
                return("200 OK", "<html><head><title>URL-shorter App</title>"\
                       "</head><body><h3>This app shorts URLs "\
                       "</h3><form action='http://localhost:1234?url=1'method='POST'>"\
                       "URL:<input type='text' name='url' value=''"\
                       " /><br/><input type='submit' value='Send' /></form>"\
                       "<h2>" + URLlist + "</h2></body></html>")
            else:
                # HTTP Not Found
                return("404 Not Found", "<html><head><title>URL-shorter App"\
                       "</title></head><body><h3>Error: Resource not "\
                       "available</h3></body></html>")                
        else:
            return None

    

    def parse(self, request):
        """Parse the received request, extracting the relevant information."""
        method = request.split()[0]
        resource = request.split()[1].split("/")[1]
        return (method, resource)

    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        method = parsedRequest[0]
        resource = parsedRequest[1]
        print("Method:", method)
        print("Resource:", resource)
        (URLdic, shortURLdic) = self.readCSV()
        if method == "GET":
            (code, answer) = self.GETanswer(resource, shortURLdic)
            return(code,answer)

        elif parsedRequest[0] == "POST":
            return("200 OK", "<html><head><title> URL-shorter App</title>"\
                   "</head><body><h3>This is the answer to a POST"\
                   "</h3>"\
                   "</body></html>")
        else:
            return ("200 OK", "<html><body><h1>Not a GET!</h1></body></html>")


if __name__ == "__main__":
    testWebApp = URL_short("localhost", 1234)
