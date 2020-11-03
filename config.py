import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'#OZ\xb0\xaf\xdb\xfb\xad*\xc6\xfeg\xf7\x9e\xbd6'

    MONGODB_SETTINGS = { 'db' : 'UTA_Enrollment' }