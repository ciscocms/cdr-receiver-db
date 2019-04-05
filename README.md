# cdr-receiver-db
A sample CDR receiver for Cisco Meeting Server with persistent storage

### installation
#### prerequisites
* sqlite
* python packages from requirements.txt
* virtualenv (recommended but not required)

```bash
$ virtualenv env
$ . env/bin/activate
(env)$ pip install -r requirements.txt
```

### configuration
#### meeting server configuration
From webadmin on Cisco Meeting Server navigate to: **Configuration >> CDR Settings**

In one of the four Receiver URI slots enter the URI for host that is running the receiver.

``` http://<receiver host>:8444/cdr ```

### usage
#### overview
The application uses the Python Flask framework to implement three main components
* CDR receiver able to accept POST data from Cisco Meeting Server
* Admin interface to view CDR records
* API endpoint for retrieving records (JSON)

#### urls
* CDR receiver - ```http://<receiver host>:8444/cdr```
* Admin interface - ```http://<receiver host>:8444/admin```
* API - ```http://<receiver host>:8444/api/v1/records/```

#### runing
```
(env)$ python admin.py
* Serving Flask app "receiver" (lazy loading)
* Environment: production
  WARNING: Do not use the development server in a production environment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://0.0.0.0:8444/ (Press CTRL+C to quit)
```

#### testing
Start a meeting on CMS. Navigate to ```http://<receiver host>:8444/admin```

Click on the Record header. The first page of CDR records will be displayed.

#### api
The API will return twenty (20) records per call, and supports pagination. A response of ```{"records":0}``` on a page other than 1 indicates you have reached the end of the record set.

```
$ curl http://localhost:8444/api/v1/records/1
{
  "records":[
    {"@correlatorIndex":"115","@recordIndex":"24","@time":"2019-04-05T16:55:22Z","@type":"callEnd","call":{"@id":"6af88404-91a4-441a-b46e-b4c455c9959d","callLegsCompleted":"1","callLegsMaxActive":"1","durationSeconds":"4"}},
    {"@correlatorIndex":"114","@recordIndex":"23","@time":"2019-04-05T16:55:22Z","@type":"callLegEnd","callLeg":{"@id":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","activatedDuration":"4","durationSeconds":"4","encryptedMedia":"true","mediaUsagePercentages":{"mainVideoContributor":"100.0","mainVideoViewer":"100.0"},"reason":"remoteTeardown","remoteTeardown":"true","rxAudio":{"codec":"opus"},"rxVideo":{"codec":"h264"},"txAudio":{"codec":"opus"},"txVideo":{"codec":"h264","maxSizeHeight":"600","maxSizeWidth":"800"}}},
    {"@correlatorIndex":"113","@recordIndex":"22","@time":"2019-04-05T16:55:22Z","@type":"callLegUpdate","callLeg":{"@id":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","call":"6af88404-91a4-441a-b46e-b4c455c9959d","deactivated":"false","displayName":"Jyn Erso","groupId":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818"}},
    {"@correlatorIndex":"112","@recordIndex":"21","@time":"2019-04-05T16:55:18Z","@type":"callLegUpdate","callLeg":{"@id":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","call":"6af88404-91a4-441a-b46e-b4c455c9959d","deactivated":"false","displayName":"Jyn Erso","groupId":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","state":"connected"}},
    {"@correlatorIndex":"111","@recordIndex":"20","@time":"2019-04-05T16:55:18Z","@type":"callLegStart","callLeg":{"@id":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","call":"6af88404-91a4-441a-b46e-b4c455c9959d","direction":"incoming","displayName":"Jyn Erso","groupId":"ffaebfd2-6510-40a0-89ae-8c4a8a4d0818","remoteParty":"jyn@wobani.org","type":"acano"}},
    {"@correlatorIndex":"110","@recordIndex":"19","@time":"2019-04-05T16:55:18Z","@type":"callStart","call":{"@id":"6af88404-91a4-441a-b46e-b4c455c9959d","callCorrelator":"c6727635-cba3-4c22-bdfa-52b1c4112db7","callType":"coSpace","coSpace":"529dc096-5ad9-4347-ba0d-c5908c001479","name":"Scarif Weekly Data Backup Planning Meeting","ownerName":"Orson Krennic"}}
    ]
}
```
```
$ curl http://localhost:8444/api/v1/records/2
{"records":0}
```
