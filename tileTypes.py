tileTypes = [
            {
                "id": "impacted-tests",
                "type": "data_table",
                "periods": [
                    'last_hour',
                ],
                "title": "ENT/Cloud Tests Impacted by Offline Agents",
                "short_description": "Impacted tests by offline but enabled enterprise/cloud agents",
                "description": '',
                'tags':['impacted', 'tests']
            },
            # {
            #     "id": "test-graph",
            #     "type": "line_chart",
            #     "title": "Test Graph",
            #     "periods": ["last_hour"],
            #     "short_description": "A short description",
            #     "description": "A longer description",
            #     "tags": ["test"],
            # },
            {
                "id": "tests-down",
                "type": "metric_group",
                "title": "Enabled ENT/Cloud Agents and Tests",
                "periods": ["last_hour"],
                "short_description": "A short description",
                "description": "A longer description",
                "tags": ["test"],
            },
            {
                "id": "endpoint-scheduled-tests",
                "type": "data_table",
                "periods": [
                    'last_hour',
                ],
                "title": "Endpoint Scheduled Tests",
                "short_description": "List of tests that are run on endpoint agents",
                "description": "List of tests that are run on endpoint agents",
                "tags": ["test"],
            },
            {
                "id": "endpoint-agent-map",
                "type": "threat_map",
                "title": "Endpoint Agents Map",
                "periods": ["last_hour"],
                "short_description": "A short description",
                "description": "A longer description",
                "tags": ["test"],
            },
            {
                "id": "alerts",
                "type": "data_table",
                "periods": [
                    'last_hour',
                ],
                "title": "Active Alerts",
                "short_description": "Active Alerts in ThousandEyes",
                "description": '',
                'tags':['alerts', 'overview']
            },
            # {
            #     "description": "Tests Down Markdown",
            #     "periods": [
            #         "last_hour"
            #     ],
            #     "tags": [
            #         "test",
            #         "test2"
            #     ],
            #     "type": "markdown",
            #     "short_description": "Shows some markdown stuff",
            #     "title": "Tests Down Markdown",
            #     "id": "tests-markdown"
            # } 
        ]