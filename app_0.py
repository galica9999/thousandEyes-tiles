import os, datetime, sys
from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify
import base64
import requests, json
from schemas import DashboardTileDataSchema, DashboardTileSchema
from utils import get_json, get_jwt, jsonify_data
from crayons import *
from thousandEyes import *
from tileTypes import *

sys.path.append('./tiles')
from impactedTests import impactedTests
from agentTestStats import agentTestStats
from worldTile import worldTileList
from endpointScheduledTest import endpointScheduledTests
from alerts import alerts

app = Flask(__name__)

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def jsonify_data(data):
    return jsonify({'data': data})


def jsonify_errors(data):
    return jsonify({'errors': [data]})

@app.route('/')
def test0():
    return "<h1>RELAY MODULE IS UP</h1>"
    
@app.route('/test')
def test():
    truc = 1 + 40
    return "<h1>Sounds Good the server is UP "+str(truc)+"</h1>"

@app.route('/health', methods=['POST'])
def health(): 
    data = {'status': 'ok'}
    return jsonify({'data': data})  

@app.route("/tiles", methods=["POST"])
def tiles():
    return jsonify_data(
        tileTypes
    )
    
@app.route("/tiles/tile-data", methods=["POST"])
def tile_data():
    USER, TOKEN, GROUP = base64.b64decode(request.headers['Authorization'][6:]).decode('utf-8').split(':')
    if not TOKEN:
        print(TOKEN)
        return
    if not USER:
        print(USER)
        return
    data = get_json(DashboardTileDataSchema())
    # print (green(data["tile_id"],bold=True))
    apiOk = testApi(BASE_URL, USER, TOKEN)
    # print(apiOk)
    if apiOk == 401:
        return jsonify_data({"observed_time": {
                    "start_time": "2020-12-28T04:33:00.000Z",
                    "end_time": "2021-01-27T04:33:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-27T04:33:00.000Z",
                    "end_time": "2021-01-27T04:38:00.000Z",
                },"key_type": "string",'data':{'errors':['Not authorized']}})
    testList = getTestList(BASE_URL, USER, TOKEN)
    enabledTests = getEnabledTests(testList)
    agentList = getAgentList(BASE_URL, USER, TOKEN)
    enabledAgents, enabledAgentIds ,offlineEnabledAgents, offlineEnabledAgentIds = getEnabledAgents(agentList)
    offLineAgentDetails = agentDetails(offlineEnabledAgentIds, USER, TOKEN)
    enabledTestsAffectedByOfflineAgent = compareEnabledTestsToOfflineEnabledAgents(enabledTests, offLineAgentDetails)
    if data["tile_id"] == "impacted-tests":
        return jsonify_data(
                impactedTests(enabledTestsAffectedByOfflineAgent,enabledTests)
            )
    if data["tile_id"] == "endpoint-agent-map":
        endpoints = getEndpointAgents(BASE_URL, USER, TOKEN)
        enabledEndpoints = getEnabledEndpointAgents(endpoints)
        return jsonify_data(worldTileList(enabledEndpoints))

    if data["tile_id"] == "endpoint-scheduled-tests":
        tile = endpointScheduledTests(getScheduledTests(BASE_URL, USER, TOKEN))
        return jsonify_data(
            tile
        )
    if data["tile_id"] == "tests-down":
        return jsonify_data(
            agentTestStats(enabledAgentIds, enabledTests, offlineEnabledAgentIds, enabledTestsAffectedByOfflineAgent)
        )
    if data["tile_id"] == "alerts":
        return jsonify_data(
            alerts(getAlerts(BASE_URL, USER, TOKEN))
        )
    else:
        return jsonify_data(
            {
                "observed_time": {
                    "start_time": "2020-12-28T04:33:00.000Z",
                    "end_time": "2021-01-27T04:33:00.000Z",
                },
                "valid_time": {
                    "start_time": "2021-01-27T04:33:00.000Z",
                    "end_time": "2021-01-27T04:38:00.000Z",
                },
                "key_type": "timestamp",
                "data": [
                    {"key": 1611731572, "value": 13},
                    {"key": 1611645172, "value": 20},
                ],
                "cache_scope": "org",
            }
        )

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404 

    
if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=False,host='0.0.0.0', port=80)
