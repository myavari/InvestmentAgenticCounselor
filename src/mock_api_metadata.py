functions_metadata = [
    {
        "name": "mock_twitter_api",
        "description": "Simulates a Twitter API response based on a query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query for Twitter data (e.g., 'bitcoin price')."
                },
                "num_results": {
                    "type": "integer",
                    "description": "The number of tweets to include in the response.",
                    "default": 20
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "mock_newsdata_api",
        "description": "Simulates a NewsData.io API response based on a query.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query for news articles (e.g., 'bitcoin price')."
                },
                "num_results": {
                    "type": "integer",
                    "description": "The number of news articles to include in the response.",
                    "default": 20
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "mock_tiingo_api",
        "description": "Simulates a Tiingo API response with historical price data.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query or ticker symbol for the stock (e.g., 'bitcoin')."
                },
                "num_results": {
                    "type": "integer",
                    "description": "The number of historical price entries to include in the response.",
                    "default": 20
                }
            },
            "required": ["query"]
        }
    }
]
