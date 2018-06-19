from graphene.test import Client

# Getting setupt to setup database
from data import setupDatabase

# Getting schema
from schema import schema


# Setup database
setupDatabase()

# get the client for the given schema
client = Client(schema)


def test_hero_name_query():

	# Hero(name)
	query = '''
		query data{
			hero{
				name
			}
		}

	'''
	result = client.execute(query)
	print '<<<<------------- Test Hero Name Query ------------->>>>>'
	print result
	print '---------------------------------------------------------'


def test_hero_name_and_friends_query():

	# Hero (id , name , friends(name))
	query = '''
		query data{
			hero{
				id
				name
				friends{
					name
				}
			}
		}
	'''	

	result = client.execute(query)
	print '<<<<----------------Test Hero Name and Friends Query ---------->>>>>'
	print result
	print '---------------------------------------------------------------------'



def test_nested_query():

 # Hero( name , friends(name , appearsIn , friends(name)))	
	query = '''
 		query data{
 		 hero{
 		 	name
 	 		friends{
 	 			name
 	 			appearsIn
 	 			friends{
 	 				name
 	 			}
 	 		}
 		 }
 		}

 	'''	
	result = client.execute(query)
	print '<<<<----------------Test Nested Query ---------->>>>>'
	print result
	print '---------------------------------------------------------------------'


def test_fetch():
	# Human(name){id = 1000}
	query = '''
		query data{
			human(id : "1000"){
				name
			}
		}
	'''

	result = client.execute(query)
	print '<<<<----------------Test Fetch ---------->>>>>'
	print result
	print '---------------------------------------------------------------------'


test_hero_name_query()
test_hero_name_and_friends_query()
test_nested_query()
test_fetch()