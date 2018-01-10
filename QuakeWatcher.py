# Lab 6: QuakeWatcher.py
# Gathers all the earthquake data in the last week in the Alaska region and the Coastal region.
# CS496
# 4/13/2016
# @author Steven Duong

import earthquakes
print("Program 6, Steven Duong, masc1653\n")

report = earthquakes.get_report('week','all')		#get all earthquakes from last week
quakes = report['earthquakes']				#copy contents to quakes

location = []
for quake in quakes:
	location.append(quake['location'])


#save to file
alaska_quakes = open("alaska_quakes.txt", "w")
coastal_quakes = open("coastal_quakes.txt", "w")


#get longitude list for alaska
longitudes = []
for loc in location:
	for key,value in loc.items():
		if key is 'longitude':
			longitudes.append(value)
			
#get latitude list for alaska
latitudes = []
for loc in location:
	for key,value in loc.items():
		if key is 'latitude':
			latitudes.append(value)

#get all earthquakes in Alaska region
isAlaska = []
for i in range(len(quakes)):
	if latitudes[i] > 50 and latitudes[i] < 63 and longitudes[i] > -178 and longitudes[i] < -130:
		isAlaska.append(quakes[i]['magnitude'])
		alaska_quakes.write("Latitude: %f     Longitude: %f   Magnitude: %f	Location:%s\n" %(latitudes[i],longitudes[i],quakes[i]['magnitude'],quakes[i]['location_description']))

alaska_quakes.close()

#get all earthquakes in Coastal region
isCoastal = []
for i in range(len(quakes)):
	if latitudes[i] > 20 and latitudes[i] < 50 and longitudes[i] > -130 and longitudes[i] < -105:
		isCoastal.append(quakes[i]['magnitude'])
		coastal_quakes.write("Latitude: %f     Longitude: %f   Magnitude: %f	Location:%s\n" %(latitudes[i],longitudes[i],quakes[i]['magnitude'],quakes[i]['location_description']))

coastal_quakes.close()


#the number of earthquakes in Alaska region
print("Number of quakes in Alaska region: %d" % len(isAlaska))

#the number of earthquakes in Coastal region
print("Number of quakes in Coastal region: %d" % len(isCoastal))

#frequency of Alaska quakes compared to Coastal quakes
if len(isAlaska) > len(isCoastal):
	print("There are more earthquakes in the Alaska region!")
else:
	print("There are more earthquakes in the Coastal region!")


#average magnitude for Alaska region
totalAlaska = 0
for i in range(len(isAlaska)):
	totalAlaska = totalAlaska + isAlaska[i]

avgAlaska = 0
avgAlaska = totalAlaska / len(isAlaska)
print("Average magnitude of earthquakes in Alaska region: %f" % avgAlaska)


#average magnitude for Coastal region
totalCoastal = 0
for i in range(len(isCoastal)):
	totalCoastal = totalCoastal + isCoastal[i]

avgCoastal = 0
avgCoastal = totalCoastal / len(isCoastal)
print("Average magnitude of earthquakes in Coastal region: %f" % avgCoastal)

#max magnitude for Alaska region
maxAlaska = 0
for i in range(len(isAlaska)):
	if isAlaska[i] > maxAlaska:
		maxAlaska = isAlaska[i]

#max magnitude for Coastal region
maxCoastal = 0
for i in range(len(isCoastal)):
	if isCoastal[i] > maxCoastal:
		maxCoastal = isCoastal[i]

print("Maximum magnitude in Alaska region: %f" %maxAlaska)
print("Maximum magnitude in Coastal region: %f" %maxCoastal)


print("\nList containing magnitude and coordinates of earthquakes over 3.9 in Alaska and the Coastal region:")

#Alaska Quakes over the 3.9 threshold
AlaskaQuakeThres = []
for i in range(len(quakes)):
	if latitudes[i] > 50 and latitudes[i] < 63 and longitudes[i] > -178 and longitudes[i] < -130 and quakes[i]['magnitude'] > 3.9:
		AlaskaQuakeThres.append(quakes[i]['magnitude'])
		print("Latitude: %f     Longitude: %f   Magnitude: %f	Location: %s"	%(latitudes[i],longitudes[i],quakes[i]['magnitude'],quakes[i]['location_description']))

#Coastal Quakes over 3.9 threshold
CoastalQuakeThres = []
for i in range(len(quakes)):
	if latitudes[i] > 20 and latitudes[i] < 50 and longitudes[i] > -130 and longitudes[i] < -105 and quakes[i]['magnitude'] > 3.9:
		CoastalQuakeThres.append(quakes[i]['magnitude'])
		print("Latitude: %f     Longitude: %f   Magnitude: %f	Location: %s"	%(latitudes[i],longitudes[i],quakes[i]['magnitude'],quakes[i]['location_description']))


#avg magnitude of Alaska quakes over 3.9
totalAlaskaThres = 0
for i in range(len(AlaskaQuakeThres)):
	totalAlaskaThres = totalAlaskaThres + AlaskaQuakeThres[i]

avgAlaskaThres = 0
avgAlaskaThres = totalAlaskaThres / len(AlaskaQuakeThres)
print("\nAverage magnitude of earthquakes over 3.9 in Alaska region: %f" %avgAlaskaThres)


#avg magnitude of Coastal quakes over 3.9
totalCoastalThres = 0
for i in range(len(CoastalQuakeThres)):
	totalCoastalThres = totalCoastalThres + CoastalQuakeThres[i]

avgCoastalThres = 0
avgCoastalThres = totalCoastalThres / len(CoastalQuakeThres)
print("Average magnitude of earthquakes over 3.9 in Alaska region: %f" %avgCoastalThres)

#which has highest avg magn of quakes over 3.9
if avgAlaskaThres > avgCoastalThres:
	print("Alaska has a greater average magnitude of quakes over 3.9 than Coastal!")
else:
	print("Coastal has a greater average magnitude of quakes over 3.9 than Alaska!")




