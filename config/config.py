import os
import sys

from dynaconf import Dynaconf


ALLOWED_ENVS = ['DEV', "BETA", 'PROD']
ENVIRONMENT = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] in ALLOWED_ENVS else 'DEV'

config_files = ['config.yaml']
if ENVIRONMENT.upper() == 'BETA':
    config_files.append('config-beta.yaml')
if ENVIRONMENT.upper() == 'PROD':
    config_files.append('config-prod.yaml')


ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

settings = Dynaconf(
    root_path=ROOT_PATH,
    settings_files=config_files,
    load_dotenv=True,
    dotenv_path="../.env"
)
