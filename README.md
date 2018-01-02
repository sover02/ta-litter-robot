ta-litter-robot
===============


A Splunk App for getting data from your [Robot Litter Box](https://www.litter-robot.com/)!
-------------------------------------------------------------------------------------------

### How to use:

1. Install the App on a Forwarder.

2. Create the litter-robot index and enable the input scripted input.

3. Get x-api-key from the Litter Robot Connect App. Hell if I know how they translate the credentials into the JWT and then into the x-api-key, but you can use burpsuite or some other web proxy solution to intercept web traffic between the app and the CloudFront API.  
Resources:
   * [Configuring an iOS Device to Work With Burp](https://support.portswigger.net/customer/portal/articles/1841108-configuring-an-ios-device-to-work-with-burp)
   * [Installing Burp's CA Certificate in an iOS Device](https://support.portswigger.net/customer/portal/articles/1841109-Mobile%20Set-up\_iOS%20Device%20-%20Installing%20CA%20Certificate.html)

4. Add x-api token to state file. Copy or rename `state.example` to `state`. Add in your x-api token.  It should look something like:
```
[auth]
x-api-key = sesks4saFEdlk332klssSDSKGAar
```

5. Install the App on Search Heads.

* Coming Soon - Alert: `run_cycle.py`

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

### Screenshots

Raw Events
![Raw Events](https://raw.github.com/sover02/litter-robot/screenshots/contrib/Screen%20Shot%202018-01-02%20at%202.13.10%20PM.png)

Lookup Table with Types of Litter Robot Events
![Lookup Table with Types of Litter Robot Events](https://raw.github.com/sover02/litter-robot/screenshots/contrib/Screen%20Shot%202018-01-02%20at%202.16.08%20PM.png)

Robot Events Tracked over Time
![Robot Events Tracked over Time](https://raw.github.com/sover02/litter-robot/screenshots/contrib/Screen%20Shot%202018-01-02%20at%202.15.37%20PM.png)


