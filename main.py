from auvsi_suas.client import client
from auvsi_suas.proto import interop_api_pb2

client = client.Client(url='https://hkuuas-suas.mysgapp.co',
                       username='testuser',
                       password='testpass')

mission = client.get_mission(1)
print(mission)
