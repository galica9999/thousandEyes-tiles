import datetime

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def endpointScheduledTests(scheduledTests):
    testList = scheduledTests['endpointTest']
    print(testList)
    tableRows=[]
    for test in testList:
        if test['enabled'] == 1 :
            tableRows.append(
                        {
                            'test_name': test['testName'],
                            'link_uri': 'https://app.thousandeyes.com/endpoint/test-settings/?tab=tests',
                            'type':test['type'],
                            'server':test['server'],
                            'port':test['port'],
                        }
                    )
    return {
            "observed_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "valid_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "data": {
                "hide_filters": False,
                "period": "last_24_hours",
                "key_type": "string",
                "columns": [
                    {
                        "key": "test_name",
                        "label": "Name",
                        "content_type": "linked_text"
                    },
                    {
                        "key": "type",
                        "label": "Type",
                        "content_type": "filter_text"
                    },
                    {
                        "key": "server",
                        "label": "Server",
                        "content_type": "text"
                    },
                    {
                        "key": "port",
                        "label": "Port",
                        "content_type": "filter_text"
                    },


                ],
                'rows':tableRows
                },
            "cache_scope": "org",
        }
    