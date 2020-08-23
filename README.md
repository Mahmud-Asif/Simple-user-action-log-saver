




**Backend Developer**

## Installation

Clone this repository:

```bash
$ git clone https://github.com/Mahmud-Asif/backend-developer.git
```

Then go to the  `backend-developer` folder:

```bash
$ cd backend-developer
```

Now, you need to create a virtual environment and install all the dependencies. 

```bash
$ virtualenv venv
$ . venv/bin/activate
```

## Run the Code
Use the following shell command and it will install the requirements and the code: 
```bash
$ sh userLogs.sh
```


* **URL**

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
   `startTime = [timestamp]` <br />
   `endTime = [timestamp]` <br />

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


