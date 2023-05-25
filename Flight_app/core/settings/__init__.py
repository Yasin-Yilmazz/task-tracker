
from decouple import config

ENVRIONMENT = config('ENV')

if ENVRIONMENT=='development':
    from .development import *
else:
    from .production import *