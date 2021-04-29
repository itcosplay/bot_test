import os

from dotenv import load_dotenv
from dotenv import dotenv_values

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

# some_data = os.getenv('SOME_KEY')
some_data = dotenv_values('.env')
print(some_data['SOME_KEY'])