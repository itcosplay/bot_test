import os

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))

print('BOT_TOKEN: ', BOT_TOKEN)


###
###
# from dotenv import dotenv_values

# env_data = dotenv_values('.env')
# print(env_data['BOT_TOKEN'])