import socket
import sys
import json


class UdpClient:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_request(self, cmd):
        try:
            self.sock.sendto(cmd, (self.ip, self.port))
            data = self.sock.recvfrom(2048)

            print(cmd + ' : ' + data[0])

            return data[0]
        except:
            print('UDP Connection Error: ', sys.exc_info()[0])
            raise

    def set_light(self, bright, red, green, blue, status, active_bulb):
        cmd = '{"cmd":"light_ctrl",' \
              '"r":"' + str(red) + '",' \
              '"g":"' + str(green) + '",' \
              '"b":"' + str(blue) + '",' \
              '"bright":"' + str(bright) + '",' \
              '"effect":"9",' \
              '"iswitch":"' + str(status) + '",' \
              '"matchValue":"0",' \
              '"sn_list":[' \
              '{"sn":"' + active_bulb + '"}' \
              ']}'

        data = self.send_request(cmd)

    def set_title(self, sn, title):
        cmd = '{"cmd":"set_title","sn":"' + sn + '","title":"' + title + '"}'

        data = self.send_request(cmd)

    def get_lights(self):
        cmd = '{"cmd":"light_list"}'

        data = self.send_request(cmd)

        try:
            json_data = json.loads(data)

            return json_data
        except:
            print('JSON Parsing Error: ', sys.exc_info()[0])
            raise
