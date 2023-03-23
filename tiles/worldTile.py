import datetime
import time
import re

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def epochTime():
    timeString = str(time.time()).split('.')[0]
    return int(timeString)


def convertDateToEpoch(dateTime):
    #2023-03-06 19:57:53
    # date,time = dateTime.split(' ')
    dateTime = '2023-03-06 19:57:53'
    date = re.split('-| |:', dateTime)
    epoch = datetime.datetime(int(date[0]), int(date[1]), int(date[2]), int(date[3]), int(date[4]), int(date[5])).strftime('%s')
    return int(epoch)

def endpointLastSeenStatus(lastSeenTime, currentTime):
    if currentTime - lastSeenTime > 86400 * 3:
        return 'malware'
    if currentTime - lastSeenTime > 86400:
        return 'spam'
    else:
        return ''
    


def worldTileList(enabledAgents):
    currentTime = epochTime()
    agentDataList = []
    index = 0
    for agent in enabledAgents:
        index+=1
        agentEpoch = convertDateToEpoch(agent['lastSeen'])
        endpointLastSeenStatus(agentEpoch, currentTime)
        endpointStatus = endpointLastSeenStatus(agentEpoch, currentTime)
        agentDataList.append({
            'id':  index,
            'coordinates' : [agent['location']['latitude'], agent['location']['longitude']],
            "geoip_accuracy_radius":10,
            "hostname":agent['agentName'],
            "ip_address":agent['publicIP'],
            'last_online': agent['lastSeen'],
            'email_type': endpointStatus
                    })
    payload = {
            "observed_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "valid_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "data": agentDataList,
            "cache_scope": "org",
        }
    return payload