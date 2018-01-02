ta-litter-robot
============


A Splunk App for getting data from your Robot Litter Box!
---------------------------------------------------------

### How to use:

1. Install the App on a forwarder and Search Head.  Disable the input on the Search Head (n/a if single server deployment).

2. Get x-api-key from the Litter Robot Connect App. Hell if I know how they translate the credentials into the JWT and then into the x-api-key, but you can use burpsuite or some other web proxy solution to intercept web traffic between the app and the CloudFront API.  
Resources:
* [Configuring an iOS Device to Work With Burp](https://support.portswigger.net/customer/portal/articles/1841108-configuring-an-ios-device-to-work-with-burp)
* [Installing Burp's CA Certificate in an iOS Device](https://support.portswigger.net/customer/portal/articles/1841109-Mobile%20Set-up\_iOS%20Device%20-%20Installing%20CA%20Certificate.html)

3. Add x-api token to state file. Copy or rename `state.example` to `state`. Add in your x-api token.  It should look something like:
```
[auth]
x-api-key = sesks4saFEdlk332klssSDSKGAar
```

* Coming Soon - `run_cycle.py`

### Example Output:

    (venv)whisper:litter-robot david$ python activity.py 

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
	"timestamp": "2017-12-16T23:46:51.379723", 
	"unitStatus": "CST", 
	"litterRobotId": "3434lddaseb3c9"
    }
    {
	"timestamp": "2017-12-16T23:46:57.705861", 
	"unitStatus": "CCC", 
	"litterRobotId": "3434lddaseb3c9"
    }


### Status Codes Mapping:

| Code | Message |
| ---- |:-------:|
| RDY  | Ready |
| CCC  | Clean Cycle Complete |
| CCP  | Clean Cycle In Progress |
| CST  | Cat Sensor Timing |
| OFF  | Device is off.  I'm not sure how this even comes up... |
