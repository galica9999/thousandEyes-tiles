import requests
import json
from multiprocessing.pool import ThreadPool
#id = 0c8259fe-ad58-4245-8ac1-f63da1a92993

BASE_URL = 'https://api.thousandeyes.com/v6/'

def testApi(url, user, token):
    apiEndpoint = 'endpoint-agents/1.json'
    apiUrl = url + apiEndpoint
    response = requests.get(apiUrl, auth=(user,token))
    if response.status_code == 200:
        return 200
    if response.status_code == 401:
        return 401

def getTestList(url, user, token):
    apiEndpoint = 'tests.json'
    apiUrl = url + apiEndpoint
    response = requests.get(apiUrl, auth=(user, token))
    return response.json()

def getEnabledTests(tests):
    if not tests:
        return 'Empty array'
    testList = []
    for entry in tests.keys():
        for test in tests[entry]:
            if type(test) is dict:
                if 'enabled' in test.keys():
                    if test['enabled'] == 1:
                        testList.append(test)
            else:
                return 'Unexpected data'
    return testList


def getAgentList(url, user, token):
    apiEndpoint = 'agents.json'
    apiUrl = url + apiEndpoint
    response = requests.get(apiUrl, auth=(user, token))
    return response.json()

def getEnabledAgents(agents):
    if not agents:
        return 'Empty array'
    enabledAgentList = []
    enabledAgentIdList = []
    offlineEnabledAgents = []
    offlineEnabledIdList = []
    for entry in agents.keys():
        for agent in agents[entry]:
            if 'enabled' in agent.keys():
                if agent['enabled'] == 1:
                    enabledAgentList.append(agent)
                    enabledAgentIdList.append(agent['agentId'])
                    if 'Offline' in agent['agentState']:
                        offlineEnabledAgents.append(agent)
                        offlineEnabledIdList.append(agent['agentId'])
    return enabledAgentList, enabledAgentIdList, offlineEnabledAgents, offlineEnabledIdList

def getEndpointAgents(url, user, token):
    apiEndpoint='endpoint-agents.json'
    apiUrl = url + apiEndpoint
    response = requests.get(apiUrl, auth=(user, token))
    return response.json()

def getEnabledEndpointAgents(agents):
    if not agents:
        return 'empty array'
    enabledAgents = []
    for agent in agents['endpointAgents']:
        if agent['status'] == 'enabled':
            enabledAgents.append(agent)
    return enabledAgents

def agentDetails(agentList, user, token):
    if not agentList:
        return 'Empty array'
    def getAgentDetails(id):
        apiEndpoint = 'https://api.thousandeyes.com/v6/agents/{}.json'.format(id)
        response = requests.get(apiEndpoint, auth=(user, token))
        return response.json()
    thread_cnt = 5
    #needs retry checking for backoff timing
    pool = ThreadPool(processes=thread_cnt)
    agentDetailList=pool.map(getAgentDetails, agentList)
    pool.close()
    pool.join()
    return agentDetailList

def getScheduledTests(url, user, token):
        endpointScheduledTests = 'endpoint-tests.json'
        endpoint = url + endpointScheduledTests
        response = requests.get(endpoint, auth=(user, token))
        return response.json()

def getAutomatedTests(url, user, token):
        endpointAutomatedTests = 'endpoint-automated-session-tests.json'
        endpoint = url + endpointAutomatedTests
        response = requests.get(endpoint, auth=(user, token))
        return response.json()


def compareEnabledTestsToOfflineEnabledAgents(enabledTests, offlineAgents):
    affectedTest = set()
    for i in enabledTests:
        if i['testName'] in str(offlineAgents):
            affectedTest.add(i['testName'])
    return affectedTest



# testList = getTestList(BASE_URL, USER, TOKEN)
# enabledTests = getEnabledTests(testList)

# agentList = getAgentList(BASE_URL, USER, TOKEN)
# enabledAgents, enabledAgentIds ,offlineEnabledAgents, offlineEnabledAgentIds = getEnabledAgents(agentList)
# # agentDetailList = agentDetails(enabledAgentIds)
# offLineAgentDetails = agentDetails(offlineEnabledAgentIds)


# enabledAgentsNumber = len(enabledAgents)
# offlineEnabledAgentsNumber = len(offlineEnabledAgents)



# enabledTestsAffectedByOfflineAgent = compareEnabledTestsToOfflineEnabledAgents(enabledTests, offLineAgentDetails)
# print('enabled agents: ' + str(enabledAgentsNumber) + ' tests lists: ' + str(len(enabledTests)) +  ', offline agents: ' + str(offlineEnabledAgentsNumber) + ', affect tests: ' + str(enabledTestsAffectedByOfflineAgent))

# USER = 'rymaclen@cisco.com'
# TOKEN = 'jmi1999rta80m7oivfly47b4jvnf45go'


# getScheduledTests(BASE_URL, USER, TOKEN)
# getAutomatedTests(BASE_URL, USER, TOKEN)
# endpoints = getEndpointAgents(BASE_URL, USER, TOKEN)
# enabledEndpoints = getEnabledEndpointAgents(endpoints)
# print(enabledEndpoints)