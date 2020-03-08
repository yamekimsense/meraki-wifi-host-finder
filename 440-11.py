#works at goorm.io
# -*- coding:utf-8 -*-
# to test by flask combind with (430) 010.py - which for ble
# and 440-10.py which shows AP

from flask import Flask, render_template, redirect, request, url_for
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
from meraki_sdk.exceptions.api_exception import APIException
import json
import datetime

app = Flask(__name__, template_folder='/workspace/meraki2')


@app.route('/')
def main_get(num=None):
    return render_template('440-11.html', num=num)


@app.route('/calculate', methods=['POST', 'GET'])
def calculate(num=None):
    x_cisco_meraki_api_key = 'your meraki key'

    client = MerakiSdkClient(x_cisco_meraki_api_key)

    clients_controller = client.clients
    collect = {}
    network_id = 'your network ID'
    collect['network_id'] = network_id

    client_id = request.args.get('char1')
    print ("client_id = ", client_id)

    collect['client_id'] = client_id

    result = clients_controller.get_network_client(collect)

    # print (json.dumps(result, indent=4))
    # print ("==========================")

    last_time = datetime.datetime.fromtimestamp(int(result['lastSeen'])).strftime('%Y-%m-%d %H:%M:%S')
    last_ap_mac = result['recentDeviceMac']
    print ("last seen", last_time)
    print ("AP MAC ", last_ap_mac)

    last_ap_name = ""
    last_lat = ""
    last_lng = ""

    f = open("440-ap-list.txt", 'r')
    lines = f.readlines()
    for line in lines:
        # print (line)
        separate = line.split(' ')
        if last_ap_mac == separate[0]:
            # print (line)
            last_ap_name = separate[1]
            last_lat = separate[2]
            last_lng = separate[3]
    f.close()

    print (last_ap_mac, last_ap_name, last_lat, last_lng, last_time)

    # end of 440-10.py

    return render_template('440-11-map.html', last_ap_mac=last_ap_mac, last_ap_name=last_ap_name, last_lat=last_lat,
                           last_lng=last_lng, last_time=last_time, client_id=client_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port="80", debug=True, threaded=True)