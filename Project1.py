def container():

tag = {'green', 'blue', 'brown', 'yellow', 'grey'}
report
check

#rota oluşturulurken kullanılan doluluk oranını
#bu verilerin “sent_date” saati temel alınmalıdır
createing_route_rate = raw_input("Enter the occupancy rate used when creating the route: ")

#rota oluşturulduktan sonra ve rota başlamadan önce iletilmiş en yeni doluluk oranı
#bu verilerin “fixed time” saati temel alınmalıdır
before_after_rate = raw_input("Enter the latest occupancy rate delivered after and before the route was created: ")

#konteyner toplanmadan hemen önce ölçülen doluluk oranı
#bu verilerin “fixed time” saati temel alınmalıdır
recent_rate = raw_input("Enter the recent rate before the container come: ")

answer = raw_input("Type 'successful' or 'fail' and hit 'Enter'.").lower()
route = raw_input("Type 'on' or 'off' for the route and hit 'Enter'.").lower()
interval = raw_input("Type 'high' or 'low' and hit 'Enter'.").lower()
visit = raw_input("Type 'visited' or 'unvisited' and hit 'Enter'").lower() 
anomaly_score = raw_input("Enter the anamaly score for the sensor: ")

if answer == "successful" and route == "on":
	tag = "green"
elif answer == "successful" and route == "off":
	tag = "blue"
elif interval == "high" answer == "fail" and route == "on":
	tag = "brown"
elif visit = "visited" and answer == "fail" and route == "on":
	tag = "yellow"
elif visit = "unvisited" and answer == "fail" and route == "on":
	tag = "red-yellow"
elif answer == "fail" and route == "on":
	tag = "grey"
else:
    print "You didn't pick anything! Try again."
	container()

---------

threshold = raw_input("Please enter the threshold: ")

#for blue container
if tag == "blue" and report == FALSE:
	check = check_sensor()
	print check
	if createing_route_rate == before_after_rate:
		print "Devam"
	else:
		if before_after_rate > threshold and threshold > createing_route_rate:
			print "Sensör veri kaçırmış."
		elif before_after_rate < createing_route_rate:
			print "Sorunlu!"
			print "Keyfi Toplama"
			print "Yapay Doluluk"
		elif createing_route_rate == before_after_rate and threshold > before_after_rate and before_after_rate > createing_route_rate:
			print "Devam"
			print "Sensörden gelen veri için zaman aralığı belirlenmeli - 1 gün"
		elif before_after_rate == recent_rate:
			print "Devam"
		else:
			if recent_rate > threshold and threshold > createing_route_rate and (recent_rate - createing_route_rate) > 20:
				print "Ani Doluluk - A grubu!"
				print "Sensör veri kaçırmış!"
			elif recent_rate > threshold and threshold> createing_route_rate and (recent_rate - createing_route_rate) < 20:
				print "Ani Doluluk - B grubu!"
				print "Sensör veri kaçırmış!"
			elif recent_rate < createing_route_rate:
				print "Sorunlu!"
				print "Keyfi Toplama"
				print "Yapay Doluluk"
			elif recent_rate == createing_route_rate:
				print "Eğer sensörden gelen verilerin %70’den fazlası aynıysa"
				print "Sorunlu"
			else
				print "Devam"
			print "Ani doluluk grupları eşik değerleri değişebilir, grup sayısı artırılabilir."
			print "Sensörden gelen veri için zaman aralığı belirlenmeli; 1 gün" 
	
	#Konteynere ait önceki günün etiketi (dün) bulunur
	from datetime import datetime
	now = datetime.now()
	date = (now.day)-1
	#Container labels for the last 5 days are listed
	last_5_day
	#Container lists the tags of the last 5 rotations listed as visitors to visit.
	last_5_route
	#Ertesi gün doluluğu verisi
	next_day_data
	
	if date.tag = "red": --SOOOOR
		if last_5_day < 60 and last_5_route < 40:
			print "Sorunlu"
		else:
			print "Takip Edilecek"
	else:
		if last_5_day < 80 and last_5_route < 60:
			print next_day_data
			if (recent_rate + next_day_data) < 100:
				print "Keyfi Toplama"
			else:
				print "Eşik Değer Hatalı"
		else:
			print "Sorunlu"
			print "Takip edilecek"
	print "last_5_day ve last_5_route eşik değerleri değişebilir, aksi takdirde senaryoları çeşitlendirilebilir"
	
elif tag == "yellow" and report == FALSE":
	check = check_sensor()
	print check
	
elif tag == "red-yellow" and report == FALSE:
	check = check_sensor()
	print check
elif tag == "green" and report == TRUE:
	check = check_sensor()
	print check
	if report > 4: --eşik değeri değiştirilebilir
		print "Sensor Takip Edilecek"
	else:
		print "Devam"
elif tag == "grey" and report == TRUE:
	check = check_sensor()
	print check
	if report > 4: --eşik değeri değiştirilebilir
		print "Sensor Takip Edilecek"
	else:
		print "Devam"
container()

--------------------

def check_sensor():
sensor = {'kapak', 'ofwp', '...'}
anomaly_score

if sensor == "kapak":
	return sensor
elif sensor == "ofwp":
	return sensor
elif sensor == "...":
	return anomaly_score
else:
	print "You didn't pick anything! Try again."
	check_sensor()

check_sensor()

