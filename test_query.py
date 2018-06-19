from graphene.test import Client

# Getting setupt to setup database
from data import setup

# Getting schema
from schema import schema


# Setup database
setup()

# get the client for the given schema
client = Client(schema)

# writing query
query = '''
	query data{
		human(id : "1000"){
			name
		}
	}
'''

a = client.execute(query)
print a