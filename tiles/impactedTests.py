import datetime

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def impactedTests(enabledTestsAffectedByOfflineAgent,enabledTests):
    tableRows=[]
    for test in enabledTestsAffectedByOfflineAgent:
        tableRows.append(
                    {
                        'test_name': test,
                        'link_uri': 'https://app.thousandeyes.com/settings/tests/?tab=settings',
                        'status':'Impacted',
                        'severity':'High'
                    }
                )
    for test in enabledTests:
        if test['testName'] not in enabledTestsAffectedByOfflineAgent:
            tableRows.append(
                    {
                        'test_name': test['testName'],
                        'link_uri': 'https://app.thousandeyes.com/settings/tests/?tab=settings',
                        'status':'Ok',
                        'severity':'None'
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
                        "key": "status",
                        "label": "Status",
                        "content_type": "icon_and_text"
                    },
                    {
                        "key": "severity",
                        "label": "severity",
                        "content_type": "icon_and_text"
                    },

                ],
                'rows':tableRows
                },
            "cache_scope": "org",
        }
    