import pandas as pd
import os
import requests
import json
import matplotlib.pyplot as plt
import random

def FirstTimeEntry():
	all_states = []
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'list_of_state.csv'), 'rb')
	country2code =  pd.read_csv (c)
	c = open(os.path.join(workpath, 'state_wise_daily.csv'), 'rb')
	df = pd.read_csv (c)

	country2code.dropna(subset = ["State"], inplace=True)
	states = country2code["State"]

	for state in states:
		this_state = []
		C = []
		A = []
		R = []
		D = []
		c_sum = 0
		a_sum = 0
		r_sum = 0
		d_sum = 0
		j = 0
		code = country2code["Abbreviation"][country2code[country2code["State"] == state].index.tolist()].tolist()[0]
		for i in df[code]:
			if j%3 == 0:
				c_sum += i
				C.append(c_sum)
			elif j%3 == 1:
				r_sum += i
				R.append(r_sum)
			elif j%3 == 2:
				d_sum += i
				D.append(d_sum)
				a_sum = c_sum - r_sum - d_sum
				A.append(a_sum)
			
			j += 1
		#print(str(state)+": "+str(A))
		this_state.append(str(state))
		this_state.append(C)
		this_state.append(A)
		this_state.append(R)
		this_state.append(D)
		all_states.append(this_state)

	return all_states


def EverdayEntry():
	response = {}
	states_data = requests.get('https://api.covidindiatracker.com/state_data.json')
	#print(response.json())
	for state in states_data.json():
		response[state["state"]] = {
			"C" : state["confirmed"],
			"A" : state["active"],
			"R" : state["recovered"],
			"D" : state["deaths"],
		}

	return response

def TweetsFirstTimeEntry():
	month = {"Jan": '01', "Feb": '02', "Mar": '03', "Apr": '04', "May": '05', "Jun": '06', "Jul": '07', "Aug": '08', "Sep": '09', "Oct": '10', "Nov": '11', "Dec": '12'}
	response = []
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'list_of_state.csv'), 'rb')
	country2code =  pd.read_csv (c)
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'tweets.csv'), 'rb')
	all_tweets =  pd.read_csv (c)

	for tweet in all_tweets["ID"]:
		code = all_tweets["State"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
		state = country2code["State"][country2code[country2code["Abbreviation"] == code].index.tolist()].tolist()
		if len(state) > 0:
			date = all_tweets["Date"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
			s = all_tweets["Sentiment"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
			m = date[:3]
			d = date[-2:]
			date = d+month[m]+"2020"
			
			json = {
				"ID" : tweet,
				"State" : state[0],
				"Date" : date,
				"Sentiment" : s,
			}

			response.append(json)
	return response

def PatientsFirstTimeEntry():
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'list_of_state.csv'), 'rb')
	country2code =  pd.read_csv (c)
	c = open(os.path.join(workpath, 'raw_data.csv'), 'rb')
	df = pd.read_csv (c)
	c = open(os.path.join(workpath, 'names.csv'), 'rb')
	names = pd.read_csv (c)
	
	genders = names["gender"]
	names = names["name"]


	Patients = []
	for patient in df["Patient Number"]:
		if int(patient) == 17305:
			break
		num = random.randint(0,len(names)-1)
		state_code = df["State code"][df[df["Patient Number"] == patient].index.tolist()].tolist()[0]
		state = country2code["State"][country2code[country2code["Abbreviation"] == state_code].index.tolist()].tolist()
		if len(state) == 0:
			state = "Maharashtra"
		else:
			state = state[0]

		temp = {"Name": names[num],
				"ID": int(patient),
				"Status": df["Current Status"][df[df["Patient Number"] == patient].index.tolist()].tolist()[0],
				"Gender": genders[num],
				"Age": random.randint(20,70),
				"State": state,
				"Date": df["Date Announced"][df[df["Patient Number"] == patient].index.tolist()].tolist()[0]
				}
		Patients.append(temp)
	return Patients

def dataGraph():
	all_dates = ["Apr28","Apr29","Apr30"]
	data = {}
	dates = []
	all_tweets = TweetsFirstTimeEntry()
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'list_of_state.csv'), 'rb')
	country2code =  pd.read_csv (c)
	# print(country2code["State"])
	for i in range(1,32):
		all_dates.append("May"+str(i))
	for i in range(1,7):
		all_dates.append("Jun"+str(i))

	for state in country2code["State"]:
		sent = [0]*40
		for tweet in all_tweets:
			if tweet["State"] == state:
				if tweet["Date"][2:4] == "04":
					sent[int(tweet["Date"][:2])-28] += tweet["Sentiment"]
				if tweet["Date"][2:4] == "05":
					sent[int(tweet["Date"][:2])+2] += tweet["Sentiment"]
				if tweet["Date"][2:4] == "06":
					sent[int(tweet["Date"][:2])+33] += tweet["Sentiment"]
		
		data[state] = sent

	keys = list(data.keys())
	i = 0
	while i < 34:
		plt.figure()
		plt.subplot(221)
		plt.plot(all_dates,data[keys[i]])
		plt.tick_params(axis='x', which='major', labelsize=7)
		plt.xticks(rotation=90)
		plt.ylabel('Sentiment')
		plt.title(keys[i])
		i+=1
		plt.subplot(222)
		plt.plot(all_dates,data[keys[i]])
		plt.tick_params(axis='x', which='major', labelsize=7)
		plt.xticks(rotation=90)
		plt.ylabel('Sentiment')
		plt.title(keys[i])
		i+=1
		plt.subplot(223)
		plt.plot(all_dates,data[keys[i]])
		plt.tick_params(axis='x', which='major', labelsize=7)
		plt.xticks(rotation=90)
		plt.ylabel('Sentiment')
		plt.title(keys[i])
		i+=1
		plt.subplot(224)
		plt.plot(all_dates,data[keys[i]])
		plt.tick_params(axis='x', which='major', labelsize=7)
		plt.xticks(rotation=90)
		plt.ylabel('Sentiment')
		plt.title(keys[i])
		i+=1

		plt.subplots_adjust(hspace=0.5,wspace=0.35)
		plt.show()

PatientsFirstTimeEntry()