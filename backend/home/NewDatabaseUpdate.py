import pandas as pd
import os
import requests
import json
import matplotlib.pyplot as plt
import random

def DataFirstTimeEntry():
	all_states = []
	workpath = os.path.dirname(os.path.abspath(__file__)) #Returns the Path your .py file is in
	c = open(os.path.join(workpath, 'list_of_state.csv'), 'rb')
	country2code =  pd.read_csv (c)

	c = open(os.path.join(workpath, 'state_wise_daily.csv'), 'rb')
	df = pd.read_csv (c)

	c = open(os.path.join(workpath, 'tweets.csv'), 'rb')
	all_tweets =  pd.read_csv (c)

	
	c = open(os.path.join(workpath, 'names.csv'), 'rb')
	names = pd.read_csv (c)

	genders = names["gender"]
	names = names["name"]

	country2code.dropna(subset = ["State"], inplace=True)
	states = country2code["State"]

	data_table = []
	case_data_table = []
	case_data_relation_table = []

	all_dates = []
	for i in range(14,32):
		all_dates.append(str(i)+"-Mar-20")
	for i in range(1,10):
		all_dates.append("0"+str(i)+"-Apr-20")
	for i in range(10,31):
		all_dates.append(str(i)+"-Apr-20")
	for i in range(1,10):
		all_dates.append("0"+str(i)+"-May-20")
	for i in range(10,32):
		all_dates.append(str(i)+"-May-20")
	for i in range(1,6):
		all_dates.append("0"+str(i)+"-Jun-20")

	data_number = 1

	for state in states:
		c = 0
		a = 0
		r = 0
		d = 0
		for date in all_dates:
			current_data = [data_number,state,date]

			code = country2code["Abbreviation"][country2code[country2code["State"] == state].index.tolist()].tolist()[0]
			case_data = df[code][df[df["Date"] == date].index.tolist()].tolist()

			c += case_data[0]
			r += case_data[1]
			d += case_data[2]
			a += c - r -d
			case_data = [data_number,c,a,r,d]

			case_data_table.append(case_data)
			data_table.append(current_data)
			case_data_relation_table.append([data_number,data_number])

			data_number += 1

	tweet_relation_table = []
	tweet_table = []
	for tweet in all_tweets["ID"]:
		code = all_tweets["State"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
		state = country2code["State"][country2code[country2code["Abbreviation"] == code].index.tolist()].tolist()
		if len(state) > 0:
			s = all_tweets["Sentiment"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
			date = all_tweets["Date"][all_tweets[all_tweets["ID"] == tweet].index.tolist()].tolist()[0]
			m = date[:3]
			d = date[-2:]
			date = d+"-"+m+"-20"
			current_tweet = [tweet,s]

			for data in data_table:
			    if data[1] == state[0] and data[2] == date:
			    	current_relation = [data[0],tweet]
			    	break

			tweet_table.append(current_tweet)
			tweet_relation_table.append(current_relation)

	month = {'04':"Apr" , '05':"May",'06': "Jun"}
	patient_table = []
	patient_relation_table = []
	patient_num = 1
	entry_num = 1
	for i in range(3,6):
		c = open(os.path.join(workpath, 'raw_data'+str(i)+'.csv'), 'rb')
		patients = pd.read_csv (c)
		for patient in patients["Patient Number"]:
			if entry_num % 8 == 0 :

				date = patients["Date Announced"][patients[patients["Patient Number"] == patient].index.tolist()].tolist()
				if len(date) == 0:
					continue
				date = date[0]
				d = date[0:2]
				m = date[3:5]
				if int(m) < 4 or int(m) > 6 :
					continue

				date = d+"-"+month[m]+"-20"
				#print(date)
				if date not in all_dates:
					continue

				state_code = patients["State code"][patients[patients["Patient Number"] == patient].index.tolist()].tolist()[0]
				state = country2code["State"][country2code[country2code["Abbreviation"] == state_code].index.tolist()].tolist()
				if len(state) == 0:
					state = "Maharashtra"
				else:
					state = state[0]

				for data in data_table:
				    if data[1] == state and data[2] == date:
				    	current_relation = [data[0],patient_num] 
				    	break

				num = random.randint(0,len(names)-1)
				status = patients["Current Status"][patients[patients["Patient Number"] == patient].index.tolist()].tolist()[0]
				current_patient = [patient_num,names[num],genders[num],random.randint(20,70),status]
				
				patient_table.append(current_patient)
				patient_relation_table.append(current_relation)
				patient_num += 1
			entry_num+=1

	return case_data_relation_table,data_table,case_data_table,tweet_table,tweet_relation_table,patient_table,patient_relation_table