retrieval_func_desc = [
    {
        "name": "get_user_information",
        "description": "Get user information from database",
        "parameters": {
            "type": "object",
            "properties": {
                "user_query": {
                    "type": "string",
                    "description": "The query sentence of user. Ex. Userの誕生日は？"
                }
            },
            "required": ["user_query"],
        }
    }
]

def get_user_information(user_query: str, query_engine):
    return query_engine.query(user_query).response
