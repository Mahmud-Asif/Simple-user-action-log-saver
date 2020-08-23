#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import json
import pendulum



app = Flask(__name__)

logs = []


### Get the logs

@app.route('/openhouse/logs', methods=['GET'])
def get_logs():

	mainLog = logs

	userId = request.args.get('userId', None)
	logType = request.args.get('type', None)
	startTime = request.args.get('startTime', None)
	endTime = request.args.get('endTime', None)


	if userId:
		log = [log for log in logs if log["userId"] == userId]
		if len(log) == 0:
			return json.dumps({ "error": "User id not found"}), 404

		mainLog=log

	
	if logType:
		log=[]
		for log1 in mainLog :
			for log2 in log1["actions"]:
				if log2["type"] == logType:
					temp_log={
						'userId': log1['userId'],
						'sessionId': log1['sessionId'],
						'actions' : [log2],
					}

					log.append(temp_log)

		if len(log) == 0:
			return json.dumps({ "error": "Action type not found"}), 404

		mainLog = log


	if startTime:
		startTime =pendulum.parse(startTime)
		startTime = startTime.in_tz('UTC')
		startTime = startTime. to_datetime_string ()
		log=[]
		for log1 in mainLog :
			for log2 in log1["actions"]:
				dt = pendulum.parse(log2["time"])
				dt = dt.in_tz('UTC')
				dt = dt.to_datetime_string ()

				if dt >= startTime :
					temp_log={
						'userId': log1['userId'],
						'sessionId': log1['sessionId'],
						'actions' : [log2],
					}

					log.append(temp_log)

		if len(log) == 0:
			return json.dumps({ "error": "No action found in this time frame"}), 404

		mainLog = log

	if endTime:
		endTime = pendulum.parse(endTime)
		endTime = endTime.in_tz('UTC')
		endTime = endTime. to_datetime_string ()
		log=[]
		for log1 in mainLog :
			for log2 in log1["actions"]:

				dt = pendulum.parse(log2["time"])
				dt = dt.in_tz('UTC')
				dt = dt.to_datetime_string ()

				if dt <= endTime :
					temp_log={
						'userId': log1['userId'],
						'sessionId': log1['sessionId'],
						'actions' : [log2],
					}

					log.append(temp_log)

		if len(log) == 0:
			return json.dumps({ "error": "No action found in this time frame"}), 404

		mainLog = log

	return jsonify({'logs': mainLog})



### POST a new log

@app.route('/openhouse/logs', methods=['POST'])
def create_logs():
	if not request.json or not 'userId' in request.json or not 'sessionId' in request.json or not 'actions' in request.json:
		return json.dumps({ "error": "Please check the parameters!!"}), 400
	log = {
		'userId': request.json.get('userId',""),
		'sessionId': request.json.get('sessionId',""),
		'actions': request.json.get('actions',""),
	}
	logs.append(log)

	with open('logs.txt', 'w') as outfile:
		json.dump(logs, outfile)
	return jsonify({'log': log}), 201



if __name__ == '__main__':
	try:
		with open('logs.txt') as json_file:
			logs = json.load(json_file)
	except:
		f = open("logs.txt", "w")
		f.close()

	app.run(debug=True)



