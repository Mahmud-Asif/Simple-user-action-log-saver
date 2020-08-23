## Description of the process

Initially the `logs` will be empty. Once a new log is posted, it will be saved into the running server 
as well as a file `logs.txt`. Whenever we restart the server and run the code,
it will load the logs from the file and perform accordingly. We can provide any combination of parameters
between one userId, one Action Type, and one Time Range (a Start Time and an End Time) to filter the logs and get them. 
These parameters are optional, so we will get only the logs that filtered by the given parameters. If no parameters are
provided, all the logs will be shown. If we only provide an `Action Type` all the logs for that particular Action Type will be
returned along with their corresponding `userId` and `sessionId`. About the time range, if you provide times from different timezone,
it will still work as all the timestamps are converted into the `UTC` timezone before processing.

## Allowed HTTPs Requests

`POST: Update the Log file with new logs` <br />
`GET: Get a list of logs based on different combinations user. action type and time frame. `

## Description of Expected Server Responses

* 201 `Created` - The request of updating the loglist was sucesful
* 400 `Bad Request` - All the parameters are not present or there is a problem with the parameters 
values while posting a new log into the list. The required parameters for this request are 
`useriD` , `sessionId`, `actions` - which is the list of actions.
* 404 `Not Found` - No logs found using the combination of given parameters (userId, Action Type, Time range). 


## API Details

* **Base URL**

  `/openhouse/logs`

* **Method: POST**
  
  
   **Required Parameters:**
 
   `userId=[string]`
   `sessionId=[string]`
   `actions=[list_of_actions]`

* **Success Response:**
  

  * **Code:** `201 CREATED` <br />
    **Content:** [the posted log]
 
* **Error Response:**

  * **Code:** `400 BAD REQUEST`  <br />
    **Content:** `{ error : "Please check the parameters!!" }`

* **Sample Call:**

```json
POST /openhouse/logs
Host: localhost:5000
Content-Type: application/json 
{
	"userId": "test",
	"sessionId": "XYABC",
	"actions": [
		{
			"time": "2018-10-18T21:37:28-06:00",
			"type": "CLICK",
			"properties": {
				"locationX": 52,
				"locationY": 11
			}
		},
		{
			"time": "2018-10-18T21:37:30-06:00",
			"type": "VIEW",
			"properties": {
				"viewedId": "FDJKLHSLD"
			}
		},
		{
			"time": "2018-10-18T21:37:30-06:00",
			"type": "NAVIGATE",
			"properties": {
				"pageFrom": "queries",
				"pageTo": "request"
			}
		}
	]
}
```


* **Method: GET**
  
  
   **Optional Parameters:**
 
   `userId = [string]` <br />
   `type = [string]` <br />
   `startTime = [timestamp]`<br />
   `endTime = [timestamp]` <br />
   
  The format for the timestamps should be : `YYYY-MM-DDTHH:MM:SSZ`. <br />
   Here `Z` refers to the time zone in the format of `sHH:MM` , where `s` denotes as the sign (+/-).
   
   * Example: `2018-10-18T21:37:30-06:00`

* **Success Response:**
  
  * **Code:** `200 OK` <br />
    **Content:** [the posted log]
 
* **Error Response:**

  * **Code:** `404 NOT FOUND`  <br />
  
    **Content:**  
    
	One of the following based on the error type: <br />	
		 `{ "error": "User id not found" }` <br />
		 `{ "error": "Action type not found"}` <br />
		 `{"error": "No action found in this time frame"}` <br />

* **Sample Call:**

`GET /openhouse/logs` <br />
`Host: localhost:5000`

   * **Sample Parameters**
   
	userId:test
	type:CLICK
	startTime:2018-10-18T21:37:28-06:00
	endTime:2018-11-18T21:37:30-06:00


## Follow up Question

To make this code cloud scalable, it can be improved in two ways: 
1. To reduce the usage of memory, save the logs into small segments into different files. 
For example all the logs for a particular date will be saved into one file. So, it will 
be faster for retrieval and it will consume less memory.
2. Make different methods capable of running in parallel, which will save time and ensure the most usage of the CPUs as thousands of logs will be posted continuously. 



