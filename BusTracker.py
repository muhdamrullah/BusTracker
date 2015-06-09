"""PART I: API Extraction"""
import json
import urllib
from urlparse import urlparse
import datetime
import re
from time import gmtime, strftime
import thread, time, itertools
from datetime import timedelta

import httplib2 as http #External library

minutessince = 0

def minutesSince(busNumber,busStopNumber):
    if __name__=="__main__":
 	#Authentication parameters
 	headers = { 'AccountKey' : 'aY3606E9Kiln3+vFf7erEA==',
 	'UniqueUserID' : 'b44b64b8-5862-4341-b2d3-2ba546f8c4ce',
 	'accept' : 'application/json'} #Request results in JSON

 	#API parameters
 	uri = 'http://datamall2.mytransport.sg' #Resource URL
 	path = '/ltaodataservice/BusArrival?'
 	
 	#Query parameters
 	params = {'BusStopID':busStopNumber,
		  'ServiceNo':busNumber}; #Search at the specific busstop
		  
 	#Build query string & specify type of API call
 	target = urlparse(uri + path + urllib.urlencode( params ) )
 	method = 'GET'
 	body = ''

 	#Get handle to http
 	h = http.Http()

 	#Obtain results
 	response, content = h.request(
 		target.geturl(),
 		method,
 		body,
 		headers)
 	#Parse JSON to print
 	jsonObj = json.loads(content)

        nextbus = jsonObj['Services'][0]['NextBus']['EstimatedArrival']

	#Save result to file
 	with open("traffic_incidents.json","w") as outfile: #Saving jsonObj["d"]
	 	json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
	
	#To get difference in times
	GMtime =  strftime('%H:%M:%S', gmtime()) #Gets current time

	
	Nextbustime = datetime.datetime.strptime(nextbus, '%Y-%m-%dT%H:%M:%S+00:00').strftime('%H:%M:%S') #Gets next bus time
	FMT = '%H:%M:%S' #Set the format for subtraction
	tdelta = datetime.datetime.strptime(Nextbustime, FMT) - datetime.datetime.strptime(GMtime, FMT)

	
	#Contingency for extended hours above 12am
	if tdelta.days < 0:
		tdelta = timedelta(days=0,
				seconds=tdelta.seconds, microseconds=tdelta.microseconds)
	
	#To get minute and to make program programmable

	minutessince = int(tdelta.total_seconds() / 60)
	if minutessince <= 1:
	    minutessince = 1
	elif minutessince >= 9:
	    minutessince = 9


        global Nextbustime
        global minutessince


def extractBus(busStopNumber):
    if __name__=="__main__":
 	#Authentication parameters
 	headers = { 'AccountKey' : 'aY3606E9Kiln3+vFf7erEA==',
 	'UniqueUserID' : 'b44b64b8-5862-4341-b2d3-2ba546f8c4ce',
 	'accept' : 'application/json'} #Request results in JSON

 	#API parameters
 	uri = 'http://datamall2.mytransport.sg' #Resource URL
 	path = '/ltaodataservice/BusArrival?'
 	
 	#Query parameters
 	params = {'BusStopID':busStopNumber}; #Search at the specific busstop
		  
 	#Build query string & specify type of API call
 	target = urlparse(uri + path + urllib.urlencode( params ) )
 	method = 'GET'
 	body = ''

 	#Get handle to http
 	h = http.Http()

 	#Obtain results
 	response, content = h.request(
 		target.geturl(),
 		method,
 		body,
 		headers)
 	#Parse JSON to print
 	jsonObj = json.loads(content)
 	
 	count=0
 	List=[]   
 	
 	while True:
            nextbusNo = jsonObj['Services'][count]['ServiceNo']
            count+=1
            List.append(nextbusNo)
            List=map(int,List)     #generates a List with only int
            global List
            
            if count==10:
                break
                
	#Save result to file
 	with open("traffic_incidents.json","w") as outfile: #Saving jsonObj["d"]
	 	json.dump(jsonObj, outfile, sort_keys=True, indent=4, ensure_ascii=False)
            

"""PART II: GUI"""

import turtle
t=turtle.Turtle()
t48=turtle.Turtle()
t66=turtle.Turtle()
t67=turtle.Turtle()   
t151=turtle.Turtle()
t153=turtle.Turtle()
t154=turtle.Turtle()   
t156=turtle.Turtle()
t170=turtle.Turtle()
t171=turtle.Turtle()   
t186=turtle.Turtle() 

buses='t48', 't66', 't67','t151', 't153', 't154', 't156', 't170', 't171', 't186'

import math
t.radians()
t48.radians()
t66.radians()
t67.radians() 
t151.radians()
t153.radians()
t154.radians()
t156.radians()
t170.radians()
t171.radians()
t186.radians()

screen = turtle.Screen()
screen.setup(1000,1000)
screen.bgcolor("#006400")        # set the background color for the canvas to Dark Green

screen=turtle.Screen()
#screen.bgpic("Radar.gif")             #Adding Radar background

#Adding Bus Icon shapes
screen.addshape("Icons/BusIcon48.gif")     
t48.shape("Icons/BusIcon48.gif")
screen.addshape("Icons/BusIcon66.gif")     
t66.shape("Icons/BusIcon66.gif")
screen.addshape("Icons/BusIcon67.gif")     
t67.shape("Icons/BusIcon67.gif")
screen.addshape("Icons/BusIcon151.gif")     
t151.shape("Icons/BusIcon151.gif")
screen.addshape("Icons/BusIcon153.gif")     
t153.shape("Icons/BusIcon153.gif")
screen.addshape("Icons/BusIcon154.gif")     
t154.shape("Icons/BusIcon154.gif")
screen.addshape("Icons/BusIcon156.gif")     
t156.shape("Icons/BusIcon156.gif")
screen.addshape("Icons/BusIcon170.gif")     
t170.shape("Icons/BusIcon170.gif")
screen.addshape("Icons/BusIcon171.gif")     
t171.shape("Icons/BusIcon171.gif")
screen.addshape("Icons/BusIcon186.gif")     
t186.shape("Icons/BusIcon186.gif")

#Increasing speed of icon movement
t.speed(100) 

def drawBigCircle(a, b, r):
    """draw a circle as background. (a,b) is the origin's coordinate & r is the radius"""
    t.up()
    t.goto(a,b-r)
    t.down()
    t.color("White")
    t.circle(r)
    #t.ht()
    t.up()
    t.goto(a,b)
    
global a
a=0
global b
b=0
global r
r=225



def moveBus(n, bus, time):
    """Bus Icon will appear at a distance (in its line of movement) corresponding to
    the estimated time of arrival. 
    n is the no. of buses,  bus is the bus no. , time is the estimated time of arrival (e.g. 7)"""
    angle=(2*math.pi)/n      #arc angle
    distance=( time/float(10) )*r
    
    if bus==48:
        buses=t48
    if bus==66:
        buses=t66
    if bus==67:
        buses=t67
    if bus==151:
        buses=t151
    if bus==153:
        buses=t153
    if bus==154:
        buses=t154
    if bus==156:
        buses=t156
    if bus==170:
        buses=t170
    if bus==171:
        buses=t171
    if bus==186:
        buses=t186
   
    for i in range(n):
        if bus== ListRun[i]:
            x=i
        
            buses.up()
            buses.hideturtle()
            buses.home()
            buses.right( angle*x )    #direction
            buses.forward(distance)        #movement
            buses.showturtle()



"""PART III: INTEGRATION"""

import csv
import copy

def runInfinitely():
    
    ID= int(raw_input("Enter your bus stop ID: "))
    
    #extractBus(busStopNumber) outputs a full list of buses that go to the bus stop. E.g. List=[48,151,66]
    extractBus(ID) 
              
    ListCopy=copy.deepcopy(List)         #deepcopy of List. Changes in ListCopy do not affect List
    
    while len(ListCopy)>0:                   #loop while there're still elements in List
        raw_bus=raw_input("Enter your bus number: ")
    
        if raw_bus.isdigit()==False:                  #if   raw_bus   is not an int
            print "This is not a number. Please enter a valid bus number."
        if raw_bus.isdigit()==True:                 #if   raw_bus   is an int
            bus=int(raw_bus)                           # make raw_bus a readable int (anal syntax issue)

            if bus in List:                #if inputted bus no. is a bus that goes to bus stop. Check this with original List
                if bus not in ListCopy:      #valid bus has been inputted before. Check this with updated ListCopy
                    print "This bus number has been inputted. Please enter another bus number."
                else:
                    ListCopy.remove(bus)
            
            elif bus==0: 
                break               #User wishes to end bus list: break out of while loop 
            
            else:
                print "Bus service is unavailable at this bus stop"
    
    
    #ListRun has bus list to be shown on radar: Remove elements that occur in ListCopy from List
    ListRun =[x for x in List if x not in ListCopy]     
    global ListRun
    
    ## DATA LOG - CSV FILE WRITING
    b = open('BusDataLog.csv', 'a')    # open a file for writing
    a = csv.writer(b)                          # create the csv writer object.
    data = [['Bus no.', 'Arrival Time', 'Status']]
    a.writerows(data)
    b.close()
    
    while True:
        for i in ListRun:                                #runs through all buses in ListRun
            
            minutesSince(i,ID)                                #PART I: minutesSince(busNumber,busStopNumber)
            moveBus(len(ListRun),i,minutessince)  # PART II:  moveBus(n, bus, time)
            
            #DATA LOG UPDATE - CSV FILE WRITING
            b = open('BusDataLog.csv', 'a')    # open previous csv file for writing (appending)
            a = csv.writer(b)                         # create the csv writer object.
            data = [[i, Nextbustime,'Yes']] 
            a.writerows(data)
            b.close()     
            
        time.sleep(20)                      #loop it every 20 s



#Final commands

drawBigCircle(0, 0, 225)

runInfinitely()




