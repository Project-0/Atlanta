MONGO_HOST = 'localhost'
MONGO_PORT = 27017

MONGO_DBNAME = 'atlanta'

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
API_VERSION = 'v1'

kanban_schema = {
    'title': {
        'type': 'string',
        'minlength': 3,
        'maxlength': 80,
        'required': True,
    },
    'description': {
        'type': 'string',
    },
    'tags': {
        'type': 'list'
    }
}

DOMAIN = {
    'kanban': {
        'schema': kanban_schema
    }
}
