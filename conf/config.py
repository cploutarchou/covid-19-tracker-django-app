import os

from dotenv import load_dotenv
# LOAD Project ENV FILE
project_folder = os.path.expanduser(
    '~/PersonalProjects/covid-19-tracker-django-app')
load_dotenv(os.path.join(project_folder, '.env'))

env_type = os.environ['ENV_TYPE']

