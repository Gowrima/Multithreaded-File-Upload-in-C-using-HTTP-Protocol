# This script is a multithreaded model of client
# that sends in 'GET' and 'POST' requests concurrently
# Author: Gowrima Kikkeri Jayaramu

import threading
import httplib, urllib
import time


# Test case 1: GET request for a large file.
# Expected res: 200 OK
class ThreadClass1(threading.Thread):
    def run(httpget1):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        conn.request("GET", "/diwali.mp4")
        print "\nGET request sent at ", time.asctime(time.localtime(time.time()))
        r1 = conn.getresponse()
        print "\nServer responded at ", time.asctime(time.localtime(time.time())), r1.status, r1.reason
        #print r1.status, r1.reason
        data1 = r1.read()
        #print "read data1 %d", data1
        conn.close()
        #print "diwali.mp4 -> class 1", httpget1.getName()

for i in range(2):
    t = ThreadClass1()
    t.start()


# Test case 2: GET request for a small non existant file.
# Expected res: 404 NOT FOUND
class ThreadClass2(threading.Thread):
    def run(httpget2):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        conn.request("GET", "/foo.py")
        print "\nGET foo.py-> Class 2-> sent at ", time.asctime(time.localtime(time.time())), httpget2.getName()
        r1 = conn.getresponse()
        print "\nServer responded to foo.py->Class 2-> at ", time.asctime(time.localtime(time.time())), httpget2.getName(), r1.status, r1.reason
        #print r1.status, r1.reason
        data1 = r1.read()
        #print "foo.py->class 2", httpget2.getName()
        conn.close()

for i in range(3):
    t = ThreadClass2()
    t.start()


# Test case 3: POST request for a large file,
# Expected output: 200 OK for the first thread
# for the succeeding threads: 406 Not Acceptable (or file already exists)
class ThreadClass3(threading.Thread):
    def run(httppost1):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        file1 = open("diwali.mp4")
        x = file1.read()
        conn.request("POST", "diwali.mp4", str(x))
        print "\nPOST diwali.mp4->Class 3 sent at ", time.asctime(time.localtime(time.time())), httppost1.getName()
        r1 = conn.getresponse()
        print "\nServer responded to POST diwali.mp4->Class 3-> at ", time.asctime(time.localtime(time.time())), httppost1.getName(), r1.status, r1.reason
        #print "g1.txt->class 3 HTTP POST", httppost1.getName()
        conn.close()

for i in range(1):
    t = ThreadClass3()
    t.start()


# Test case 4: POST request for a small non-existent file
# Expected Output: 404 File Not Found
# get the file name and contents, sleep for 60 seconds, delete moon.txt and result must be '404'
class ThreadClass4(threading.Thread):
    def run(httppost2):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        file1 = open("moon.txt")
        x = file1.read()
        print "Delete moon.txt file now"
        time.sleep(30)
        conn.request("POST", "moon.txt", str(x))
        print "\nPOST moon.txt->Class 4 sent at ", time.asctime(time.localtime(time.time())), httppost2.getName()
        r1 = conn.getresponse()
       #print response.status, response.reason
        print "\nServer responded to POST moon.txt->Class 4-> at ", time.asctime(time.localtime(time.time())), httppost2.getName(), r1.status, r1.reason
      #print "moon.txt-> class 4 HTTP POST", httppost2.getName()
        conn.close()

for i in range(2):
    t = ThreadClass4()
    t.start()

# Test case 5: POST request for a small file,
# Expected output: 200 OK for the first thread
# for the succeeding threads: 406 Not Acceptable (or file already exists)
class ThreadClass5(threading.Thread):
    def run(httppost3):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        file1 = open("g1.txt")
        x = file1.read()
        conn.request("POST", "g1.txt", str(x))
        print "POST g1.txt->Class 5 sent at ", time.asctime(time.localtime(time.time())), httppost3.getName()
        r1 = conn.getresponse()
        print "Server responded to POST g1.txt->Class 5-> at ", time.asctime(time.localtime(time.time())), httppost3.getName(), r1.status, r1.reason
        #print "g1.txt->class 3 HTTP POST", httppost1.getName()
        conn.close()

for i in range(2):
    t = ThreadClass5()
    t.start()

# Test case 6: PUT request for a small file,
# Expected output: 501 Method Not Impelented for all the threads
class ThreadClass6(threading.Thread):
    def run(httpput):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        file1 = open("g1.txt")
        x = file1.read()
        conn.request("PUT", "g1.txt", str(x))
        print "PUT g1.txt->Class 6 sent at ", time.asctime(time.localtime(time.time())), httpput.getName()
        r1 = conn.getresponse()
        print "Server responded to PUT g1.txt->Class 6-> at ", time.asctime(time.localtime(time.time())), httpput.getName(), r1.status, r1.reason
        conn.close()

for i in range(3):
    t = ThreadClass6()
    t.start()


# Test case 7: POST request with 0 content length
# Expected output: 400 Bad Request for all the threads
# script fails to change the content length and generate bad request error
class ThreadClass7(threading.Thread):
    def run(httppost4):
        conn = httplib.HTTPConnection("10.0.0.2:10000")
        conn.putheader('Content-Length: 1')
        conn.endheaders()
        file1 = open("g1.txt")
        x = file1.read()    # actual content length of file g1.txt
        conn.request("POST", "g1.txt", str(x))
        print "POST g1.txt->Class 7 sent at ", time.asctime(time.localtime(time.time())), httppost4.getName()
        r1 = conn.getresponse()
        print "Server responded to POST g1.txt->Class 7-> at ", time.asctime(time.localtime(time.time())), httppost4.getName(), r1.status, r1.reason
        conn.close()

#for i in range(1):
#    t = ThreadClass7()
#    t.start()
