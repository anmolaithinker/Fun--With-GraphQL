# Graphene import

import graphene

# Getting reference from the functions data
from data import get_character , get_friends , get_human , get_droid

class Character(graphene.Interface):
	# Id
	id = graphene.ID() 

	# Name
	name = graphene.String()

	# friends
	friends = graphene.List(lambda :Character)

	# appears_in
#	appears_in = graphene.List(Episode)

	def resolve_friends(self , info):
		return [get_character(f) for f in self.friends]


# Human -> Object Type
class Human(graphene.ObjectType):
	class Meta:
		interfaces = (Character , )

# Droid -> Object Type
class Droid(graphene.ObjectType):
	class Meta:
		interfaces = (Character , )

# Query -> Object Type ( Very Important -> Combine Everything)	
class Query(graphene.ObjectType):

	# Human pointer
	human = graphene.Field(Human , id = graphene.String())

	# droid pointer
	droid = graphene.Field(Droid , id = graphene.String())


	def resolve_human(self , info , id):
		return get_human(id)

	def resolve_droid(self , info , id):
		return get_droid(id)


# Make Schema1
schema = graphene.Schema(query = Query)		



