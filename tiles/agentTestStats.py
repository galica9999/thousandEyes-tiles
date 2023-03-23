import datetime

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def agentTestStats(enabledAgentIds, enabledTests, offlineEnabledAgentIds, enabledTestsAffectedByOfflineAgent):
    metricTestsData = [
                        {'label':'Enabled Agents', 'value':str(len(enabledAgentIds)),'icon':'information', 'value_unit':'integer',    'link_uri':'https://app.thousandeyes.com/settings/agents/enterprise/?section=agents'},
                        {'label':'Enabled Tests', 'value':str(len(enabledTests)),'icon':'information', 'value_unit':'integer','link_uri':'https://app.thousandeyes.com/settings/tests/'},
                        {'label':'Offline Agents', 'value':str(len(offlineEnabledAgentIds)),'icon':'warning', 'value_unit':'integer','link_uri':'https://app.thousandeyes.com/settings/agents/enterprise/?section=agents', 'severity':'critical'},
                        {'label':'Impacted Tests', 'value':str(len(enabledTestsAffectedByOfflineAgent)),'icon':'warning', 'value_unit':'integer', 'link_uri':'https://app.thousandeyes.com/settings/tests/', 'severity':'critical'}
                    ]
    payload = {
            "observed_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "valid_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "data": metricTestsData,
            "cache_scope": "org",
        }
    return payload