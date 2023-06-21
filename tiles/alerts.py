import datetime

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def alerts(alerts):
    tableRows=[]
    status = {'INFO': 'Low',
              'MINOR':'Medium',
              'MAJOR':'High',
              'CRITICAL':'Critical'
              }
    for alert in alerts['alert']:
        tableRows.append(
                    {
                        'alert_name': alert['ruleName'],
                        'link_uri': alert['permalink'],
                        'test_name':alert['testName'],
                        'severity':status[alert['severity']]
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
    