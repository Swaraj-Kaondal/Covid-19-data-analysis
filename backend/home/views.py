from django.shortcuts import render
from django.http import JsonResponse
from .models import CARDdata, Tweet, Patient, DateAndArea, Tweets, Status, From
from .NewDatabaseUpdate import DataFirstTimeEntry
import json
import pandas as pd
import datetime
from django.views.decorators.csrf import csrf_exempt

def allStates(request):
	json_response = {}
	all_states = DateAndArea.objects.all().values("State").distinct()
	for state in all_states:
		state = state["State"]
		all_data = DateAndArea.objects.filter(State__startswith = state).order_by("Id")
		Sum = 0
		Sentiment = "Neutral"
		for data in all_data:
			relationObj = Tweets.objects.filter(DateAndAreaId = data.Id)
			if len(relationObj) > 0: 
				relationObj = relationObj[0]
				temp_tweet = Tweet.objects.filter(TweetId = relationObj.TweetId)[0]
				Sum += temp_tweet.Sentiment
		if Sum > 0.75:
			Sentiment = "Extremely Positive"
		elif Sum > 0.25:
			Sentiment = "Positive"
		elif Sum > -0.25:
			Sentiment = "Neutral"
		elif Sum > -0.75:
			Sentiment = "Negative"
		else:
			Sentiment = "Extremely Negative"
		
		last_element = len(all_data) - 1
		relationObj = Status.objects.filter(DateAndAreaId = all_data[last_element].Id)[0]
		temp_card = CARDdata.objects.filter(Data_ID = relationObj.CARDdataId)[0]
		
		Jstate = {	
			"C" : temp_card.Confirmed,
			"A" : temp_card.Active,
			"R" : temp_card.Recovered,
			"D" : temp_card.Deceased,
			"S" : Sentiment
		}

		json_response[state] = Jstate

	return JsonResponse(json_response)

def specificState(request,stateName):
	json_response = {}
	C = []
	A = []
	R = []
	D = []
	all_data = DateAndArea.objects.filter(State__startswith = stateName).order_by('Id')
	for data in all_data:
		relationObj = Status.objects.filter(DateAndAreaId = data.Id)
		if len(relationObj) > 0: 
			relationObj = relationObj[0]
			temp_card = CARDdata.objects.filter(Data_ID = relationObj.CARDdataId)[0]
			C.append(temp_card.Confirmed)
			A.append(temp_card.Active)
			R.append(temp_card.Recovered)
			D.append(temp_card.Deceased)
			
	json = {
		"C" : C,
		"A" : A,
		"R" : R,
		"D" : D,
	}		
	return JsonResponse(json)

def allPatients(request,stateName):
	json_response = {}
	all_data = DateAndArea.objects.filter(State__startswith = stateName)
	for data in all_data:
		relationObj = From.objects.filter(DateAndAreaId = data.Id)
		if len(relationObj) > 0: 
			relationObj = relationObj[0]
			temp_patient = Patient.objects.filter(Id = relationObj.PatientId)[0]
			
			temp = {
				"Name" : temp_patient.Name,
				"Date" : data.Date,
				"State" : data.State,
				"Gender" : temp_patient.Gender,
				"Status" : temp_patient.Status,
				"Age" : temp_patient.Age
			}

			json_response[temp_patient.Id] = temp
	return JsonResponse(json_response)

def India(request):
	json_response = {}
	C = []
	A = []
	R = []
	D = []
	all_data = DateAndArea.objects.filter(State__startswith = "India").order_by('Id')
	for data in all_data:
		relationObj = Status.objects.filter(DateAndAreaId = data.Id)
		if len(relationObj) > 0: 
			relationObj = relationObj[0]
			temp_card = CARDdata.objects.filter(Data_ID = relationObj.CARDdataId)[0]
			C.append(temp_card.Confirmed)
			A.append(temp_card.Active)
			R.append(temp_card.Recovered)
			D.append(temp_card.Deceased)
			
	json = {
		"C" : C,
		"A" : A,
		"R" : R,
		"D" : D,
	}		
	return JsonResponse(json)

#@csrf_exempt
""" def patient(request):
	if request.method == "POST":
		print(request.POST)
		json_response = {}
		state = request.POST.get("state")
		date1 = request.POST.get("date1")
		date2 = request.POST.get("date2")
		if len(state) > 1 and date1 != None and date2 != None:
			state = state[0].upper() + state[1:]
			date1 = datetime.date(2020, int(date1[3:5]), int(date1[0:2]))
			date2 = datetime.date(2020, int(date2[3:5]), int(date2[0:2]))
			print("date1="+str(date1)+"		date2="+str(date2))
			all_data = DateAndArea.objects.filter(State__startswith = state,Date__range=[date1, date2])
			print("state and date"+str(len(all_data)))
		elsale:
			l_data = DateAndArea.objects.all()
		for data in all_data:
			relationObj = From.objects.filter(DateAndAreaId = data.Id)
			if len(relationObj) > 0:
				relationObj = relationObj[0]
				temp_patient = Patient.objects.filter(Id = relationObj.PatientId)[0]
				print(temp_patient.Name)
				if temp_patient.Age > int(request.POST.get("age1")) and temp_patient.Age < int(request.POST.get("age2")) and temp_patient.Gender == request.POST.get("gender").lower() and  temp_patient.Status == request.POST.get("status"):
					
					temp = {
						"Name" : temp_patient.Name,
						"Date" : data.Date,
						"State" : data.State,
						"Gender" : temp_patient.Gender,
						"Status" : temp_patient.Status,
						"Age" : temp_patient.Age
					}

					json_response[temp_patient.Id] = temp
		print("response:"+str(json_response))
		#return JsonResponse(json_response)
		return({"Done":"done"}) """


@csrf_exempt
def patient(request):
	if request.method == 'POST':
		json_response = {}
		key = list(request.POST.keys())[0]
		print("Key data: "+ key)
		obj = json.loads(key)
		obj = obj["data"]
		if "state" in obj and "date1" in obj and "date2" in obj:
			state = obj["state"]
			date1 = obj["date1"]
			date2 = obj["date2"]
			state = state[0].upper() + state[1:]
			date1 = datetime.date(2020, int(date1[3:5]), int(date1[0:2]))
			date2 = datetime.date(2020, int(date2[3:5]), int(date2[0:2]))
			all_data = DateAndArea.objects.filter(State__startswith = state,Date__range=[date1, date2])
		elif "date1" in obj and "date2" in obj:
			date1 = obj["date1"]
			date2 = obj["date2"]
			date1 = datetime.date(2020, int(date1[3:5]), int(date1[0:2]))
			date2 = datetime.date(2020, int(date2[3:5]), int(date2[0:2]))
			all_data = DateAndArea.objects.filter(Date__range=[date1, date2])
		elif "state" in obj:
			state = obj["state"]
			state = state[0].upper() + state[1:]
			all_data = DateAndArea.objects.filter(State__startswith = state)
		else:
			all_data = DateAndArea.objects.all()

		
		for data in all_data:
			relationObj = From.objects.filter(DateAndAreaId = data.Id)
			if len(relationObj) > 0:
				relationObj = relationObj[0]
				temp_patient = Patient.objects.filter(Id = relationObj.PatientId)[0]
				
				if ("age1" in obj) and ("age2" in obj):
					if not (temp_patient.Age > int(obj["age1"]) and temp_patient.Age < int(obj["age2"])):
						continue
				
				if "gender" in obj:
					if temp_patient.Gender != obj["gender"].lower():
						continue
				
				if "status" in obj:
					if temp_patient.Status != obj["status"]:
						continue
	
				temp = {
					"Name" : temp_patient.Name,
					"Date" : data.Date,
					"State" : data.State,
					"Gender" : temp_patient.Gender,
					"Status" : temp_patient.Status,
					"Age" : temp_patient.Age
				}

				json_response[temp_patient.Id] = temp

		return JsonResponse(json_response)
		

@csrf_exempt
def DatabaseFirstEntry(request):
	if request.method != "POST":
		return JsonResponse({"data":"use post"})
	months = {'Mar':3 , 'Apr': 4, 'May': 5, 'Jun': 6}
	case_data_relation_table,data_table,case_data_table,tweet_table,tweet_relation_table,patient_table,patient_relation_table = DataFirstTimeEntry()
	
	for data in case_data_relation_table:
		data_entry = Status(CARDdataId = data[0], DateAndAreaId = data[1])
		data_entry.save() 

	for data in data_table:
		date = data[2]
		day = int(date[0:2])
		mon = months[date[3:6]]
		date = datetime.date(2020, mon, day)
		data_entry = DateAndArea(Id = data[0], State = data[1], Date = date)
		data_entry.save()

	for data in case_data_table:
		data_entry = CARDdata(Data_ID = data[0], Confirmed = data[1], Active = data[2],Recovered = data[3],Deceased = data[4])
		data_entry.save()	
	
	for data in tweet_table:
		data_entry = Tweet(TweetId = data[0], Sentiment = data[1])
		data_entry.save()

	for data in tweet_relation_table:
		data_entry = Tweets(TweetId = data[1], DateAndAreaId = data[0])
		data_entry.save()

	for data in patient_table:
		data_entry = Patient(Id = data[0], Age = data[3], Name =  data[1], Gender =  data[2], Status = data[4])
		data_entry.save()

	for data in patient_relation_table:
		data_entry = From(PatientId = data[1], DateAndAreaId = data[0])
		data_entry.save()

	return JsonResponse({"Done" : "Done"})

@csrf_exempt
def DatabaseUpdate(request):
	if request.method != "POST":
		return JsonResponse({"data":"use post"})
	all_states = EverdayEntry()
	for state in all_states:
		stateObj = State.objects.filter(Name__startswith = state)
		if len(stateObj) > 0:
			stateObj = stateObj[0]
			stateObj.Confirmed.append(all_states[state]["C"])
			stateObj.Active.append(all_states[state]["A"])
			stateObj.Recovered.append(all_states[state]["R"])
			stateObj.Deceased.append(all_states[state]["D"])
			stateObj.save()
	return JsonResponse({"Done" : "Done"})

@csrf_exempt
def DatabaseTweetsFirstTime(request):
	if request.method != "POST":
		return JsonResponse({"data":"use post"})
	all_tweets = TweetsFirstTimeEntry()
	for tweet in all_tweets:
		ID = tweet["ID"]
		Sentiment = tweet["Sentiment"]
		Date = tweet["Date"]
		state = tweet["State"]
		state = State.objects.filter(Name__startswith = state)[0]
		SaveTweet = Tweet(TweetId = ID,State = state,Date = Date,Sentiment = Sentiment)
		SaveTweet.save()
	return JsonResponse({"Done" : "Done"})

@csrf_exempt
def DatabasePatientsFirstTime(request):
	if request.method != "POST":
		return JsonResponse({"data":"use post"})
	all_patients = PatientsFirstTimeEntry()
	for patient in all_patients:
		ID = patient["ID"]
		Name = patient["Name"]
		Date = patient["Date"]
		state = patient["State"]
		Gender = patient["Gender"]
		Status = patient["Status"]
		Age = patient["Age"]

		state = State.objects.filter(Name__startswith = state)[0]
		SavePatient = Patient(Id = ID,State = state,Date = Date,Name = Name,Age = Age,Gender = Gender,Status = Status)
		SavePatient.save()
	return JsonResponse({"Patient" : "Recovered"})