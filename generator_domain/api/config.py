class Config(object):
    DEBUG = True
    SECRET_KEY = b'lB6PEBJEjM+WEUJz8bd/3sUGUnsWx8HcUfAC8MPJ+P4EKyJbXtspsFdjaGWDGTR51nYNIkctDE7EkEduH99XeQ=='
#    ENV = 'development'
    validator_class = {"package": "Validator", "name": "generator_domain.validator"}
    generator_class = {"package": "Generator", "name": "generator_domain.generator"}
    thumbnailer_class = {"package": "Thumbnailer", "name": "generator_domain.thumbnailer"}
    host = "localhost"
    port = 8000
    debug = True
