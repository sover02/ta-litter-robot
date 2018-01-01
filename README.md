litter-robot
============


simple set of scripts to pull data from the litter-robot
--------------------------------------------------------

### How to use:

1. Get x-api-key from the Litter Robot Connect App. Hell if I know how they translate the credentials into the JWT and then into the x-api-key, but you can use burpsuite or some other web proxy solution to intercept web traffic between the app and the CloudFront API.  
Resources:
* Configuring an iOS Device to Work With Burp (https://support.portswigger.net/customer/portal/articles/1841108-configuring-an-ios-device-to-work-with-burp)
* Installing Burp's CA Certificate in an iOS Device (https://support.portswigger.net/customer/portal/articles/1841109-Mobile%20Set-up\_iOS%20Device%20-%20Installing%20CA%20Certificate.html)


2. Create your virtual environment, activate it, and install necessary packages.
* `virtualenv venv`
* `. venv/bin/activate`
* `pip install -r requirements.txt`

3. Add x-api token to state file. Copy or rename `state.example` to `state`. Add in your x-api token.  It should look something like:
```
[auth]
x-api-key = sesks4saFEdlk332klssSDSKGAar
```

4. Run it. 
`python activity.py`


\*. Coming Soon - run\_cycle.py

### Example Output:

    (venv)whisper:litter-robot david$ python activity.py 

    {
	"timestamp": "2017-12-16T23:44:25.379723", 
	"unitStatus": "OFF", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:44:38.689644", 
	"unitStatus": "RDY", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:46:43.766606", 
	"unitStatus": "CCP", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:46:57.705861", 
	"unitStatus": "CCC", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:47:04.560274", 
	"unitStatus": "RDY", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:49:15.449989", 
	"unitStatus": "CST", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:50:07.489981", 
	"unitStatus": "RDY", 
	"litterRobotId": "3434lddaseb3c9"
    }
