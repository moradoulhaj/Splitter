from dotenv import set_key, find_dotenv

# Specify the path to your .env file
env_path = find_dotenv('.env')

entity = input("Set Entity (1,2,3....): ")

while (int(entity) > 15 or int(entity) <= 0):
	print("Invalid Entity (1 - 15), try again ")
	entity = input("Entity FOR SESSIONS (1,2,3....): ")

set_key(env_path, "ENTITY", entity)