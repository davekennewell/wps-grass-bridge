from httplib import *
import urllib
from multiprocessing import Process
import time
from optparse import OptionParser


def Execute(url, postString, id):
    print "Start request " + str(id)

    # Send the request, wait for the response and read the result
    f = urllib.urlopen( str(url), unicode(postString, "latin1"))
    wpsRequestResult = f.read()
    print "########### " + str(id) + " ##########"
    print wpsRequestResult

###############################################################################
###############################################################################
###############################################################################

def main():
    """Use this script to send XML WPS execute requests to a WPS server. The XML execute request \
       as well as the url of the WPS server must be specified. Additionally the number of requests which should be send in parallel\
       can be specified."""
        
    usage = "usage: %prog [-help,--help] [--file=\"ExecuteRequests/v.voronoi.execute.xml\"] [--url=\"http://localhost/cgi-bin/wps\"] [--requests=1]"
    description = "Use %prog to send XML WPS requests to a WPS 1.0.0 server. The resulting response is printed to stdout."
    parser = OptionParser(usage=usage, description=description)
    parser.add_option("-f", "--file", dest="requestFile",
                      help="The path to the input XML execute request file", \
                      default="ExecuteRequests/v.voronoi.execute.xml", metavar="FILE")
    parser.add_option("-u", "--url", dest="url",
                      help="The url of the WPS server i.e.: http://localhost/cgi-bin/wps", \
                      default="http://localhost/cgi-bin/wps", metavar="URL")
    parser.add_option("-r", "--requests", dest="numberOfRequests", metavar="int", \
                      help="The number of WPS execute requests send to the WPS server simutaneously", \
                      default=1)

    (options, args) = parser.parse_args()

    # Open the request file and read it into the POST string
    inFile = open(options.requestFile, 'r')
    postString = inFile.read()
    inFile.close()

    # Send the requests in parallel
    for i in range(int(options.numberOfRequests)):
        Process(target=Execute, args=(options.url, postString, i)).start()
        time.sleep(0.2)


###############################################################################
if __name__ == "__main__":
    main()
