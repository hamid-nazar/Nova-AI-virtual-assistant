

descriptions = [
    {
        "type": "function",
        "function": {
            "name": "get_local_time",
            "description": "Returns the current local time.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        "returns": "The current local time."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_flight_info",
            "description": "Get flight information between two locations",
            "parameters": {
                "type": "object",
                "properties": {
                    "origin": {
                        "type": "string",
                        "description": "The departure airport, e.g. DUS",
                    },
                    "destination": {
                        "type": "string",
                        "description": "The destination airport, e.g. HAM",
                    },
                },
                "required": ["origin", "destination"],
            },
            "returns": "The flight information between the two locations."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_cheapest_flight",
            "description": "Get cheapest flight between two locations.",
            "parameters": {
                "type": "object",
                "properties": {
                    "origin": {
                        "type": "string",
                        "description": "The departure city, e.g. Hamburg",
                    },
                    "destination": {
                        "type": "string",
                        "description": "The destination city, e.g. Berlin",
                    },
                },
                "required": ["origin", "destination"],
            },
            "returns": "The cheapest flight between the two locations."
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_weather_info",
            "description": "Get weather in a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to get the weather for, e.g. Hamburg",
                    },
                },
                "required": ["city"],
            },
            "returns": "The weather in the city."
        }
    },
    {
    "type": "function",
    "function": {
        "name": "add_reminder",
        "parameters": {
            "type": "object",
            "properties": {
                "reminder_text": {
                    "type": "string",
                    "description": "The text of the reminder to add."
                }
            },
            "required": ["reminder_text"]
        }
    }
},
    {
    "type": "function",
    "function": {
        "name": "remove_reminder",
        "parameters": {
            "type": "object",
            "properties": {
                "reminder_text": {
                    "type": "string",
                    "description": "The text of the reminder to remove."
                }
            },
            "required": ["reminder_text"]
        }
    }
    },
{
    "type": "function",
    "function": {
        "name":"get_exchange_rate_info_for_currency",
        "parameters": {
            "type": "object",
            "properties": {
                "currency": {
                    "type": "string",
                    "description": "The currency to get the exchange rate for, e.g. EUR"
                }
            },
            "required": ["currency"]
        }
    }
}

]
