import datetime

def formatTime():
    t = datetime.datetime.now(datetime.timezone.utc)
    s = t.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return s[:-3]+'Z'

def markdownTile(enabledTestsAffectedByOfflineAgent):
    def parseTests(tests):
        parsedTest = ['# Affected Tests','* This is the **definition** of the first term.',' ',' `Dorothy followed` ', ' ', '| Impacted Tests |', '| :- |']
        for i in tests:
            print(i)
            parsedTest.append('| [{}](https://app.thousandeyes.com/settings/tests/?tab=settings) |'.format(str(i)))
        return parsedTest
    parsedTests = parseTests(enabledTestsAffectedByOfflineAgent)
    print(parsedTests)
    payload = {
            "observed_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "valid_time": {
                "start_time": formatTime(),
                "end_time": formatTime(),
            },
            "data": parsedTests,
            "cache_scope": "org",
        }
    return jsonify_data(
        payload
    )