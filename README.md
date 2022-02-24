# HKU UAS Suas Connector

For the original repo, please visit https://github.com/auvsi-suas/interop

The package is used to interact with the Suas Interop server using Python

## First Time Setup

Gitclone the current Git repo.

```bash
$ git clone https://github.com/asd65241/HKU-UAS-Suas-Connector && cd HKU-UAS-Suas-Connector
```

Start a pip virtual environment
```bash
$ pipenv shell
```

Install the required packages
```bash
$ pip install -r requirements.txt
```

Install the package
```bash
$ python setup.py install
```


## Example Code
```python
# Import the package
from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2

# Initialize the Client Object
client = client.Client(url='YOUR-SUAS-ENDPOINT',
                       username='testuser',
                       password='testpass')

# Get the mission from the suas server
mission = client.get_mission(1)

# Print the mission
print(mission)
```

## More Methods

The following shows how to request the status of teams.

```python
teams = client.get_teams()
print(teams)
```

The following shows how to request the mission details.

```python
mission = client.get_mission(1)
print(mission)
```

The following shows how to upload UAS telemetry.

```python
telemetry= interop_api_pb2.Telemetry()
telemetry.latitude = 38
telemetry.longitude = -76
telemetry.altitude = 100
telemetry.heading = 90

client.post_telemetry(telemetry)
```

The following shows how to upload a object and it's image.

```python
odlc = interop_api_pb2.Odlc()
odlc.type = interop_api_pb2.Odlc.STANDARD
odlc.latitude = 38
odlc.longitude = -76
odlc.orientation = interop_api_pb2.Odlc.N
odlc.shape = interop_api_pb2.Odlc.SQUARE
odlc.shape_color = interop_api_pb2.Odlc.GREEN
odlc.alphanumeric = 'A'
odlc.alphanumeric_color = interop_api_pb2.Odlc.WHITE

odlc = client.post_odlc(odlc)

with open('path/to/image/A.jpg', 'rb') as f:
    image_data = f.read()
    client.put_odlc_image(odlc.id, image_data)
```

The following shows how to upload a map image.

```python
mission_id = 1

with open('path/to/image/A.jpg', 'rb') as f:
    image_data = f.read()
    client.put_map_image(mission_id, image_data)
```

For more details on the API, see the code [here](https://github.com/auvsi-suas/interop/tree/master/client/auvsi_suas/client).
