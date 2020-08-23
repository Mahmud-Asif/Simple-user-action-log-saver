




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
Use Pipenv:


```bash
$ virtualenv venv
$ . venv/bin/activate
```

## Run the Code

```bash
$ sh userLogs.sh
```


* **URL**

  '/openhouse/logs'

* **Method: POST**
  
  
   **Required:**
 
   `userId=[string]`
   `sessionId=[string]`
   `actions=[list_of_actions]`

* **Success Response:**
  

  * **Code:** 201 CREATED <br />
    **Content:** [the posted log]
 
* **Error Response:**

  * **Code:** 400 BAD REQUEST  <br />
    **Content:** `{ error : "Please check the parameters!!" }`

* **Sample Call:**

```yaml
POST /openhouse/logs <br />
Host: localhost:5000 <br />
Content-Type: application/json <br />
{
		"userId": "test", <br />
		"sessionId": "XYABC", <br />
		"actions": [ <br />
			{ <br />
				"time": "2018-10-18T21:37:28-06:00", <br />
				"type": "CLICK", <br />
				"properties": { <br />
					"locationX": 52, <br />
					"locationY": 11 <br />
				} <br />
			}, <br />
			{ <br />
				"time": "2018-10-18T21:37:30-06:00", <br />
				"type": "VIEW", <br />
				"properties": { <br />
					"viewedId": "FDJKLHSLD" <br />
				} <br />
			}, <br />
			{ <br />
				"time": "2018-10-18T21:37:30-06:00", <br />
				"type": "NAVIGATE", <br />
				"properties": { <br />
					"pageFrom": "queries", <br />
					"pageTo": "requests" <br />
				} <br />
			} <br />
		] <br />
	} <br />



* **Method: GET**
  
  
   **Optional:**
 
   `userId = [string]` <br />
   `type = [string]` <br />
   `startTime = [timestamp]` <br />
   `endTime = [timestamp]` <br />

* **Success Response:**
  
  * **Code:** 200 OK <br />
    **Content:** [the posted log]
 
* **Error Response:**

  * **Code:** 404 NOT FOUND  <br />
    **Content:** `{ "error": "User id not found" }` <br />
		 `{ "error": "Action type not found"}` <br />
		 `{"error": "No action found in this time frame"}` <br />

* **Sample Call:**

GET /openhouse/logs

   * **Parameters**
	`userId:test` <br />
	`type:CLICK` <br />
	`startTime:2018-10-18T21:37:28-06:00` <br />
	`endTime:2018-11-18T21:37:30-06:00` <br />


