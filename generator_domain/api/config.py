class Config(object):
    DEBUG = True
    SECRET_KEY = 'lB6PEBJEjM+WEUJz8bd/3sUGUnsWx8HcUfAC8MPJ+P4EKyJbXtspsFdjaGWDGTR51nYNIkctDE7EkEduH99XeQ=='
#    ENV = 'development'
    validator_class = {"package": "Validator", "name": "generator_domain.validator"}
    generator_class = {"package": "Generator", "name": "generator_domain.generator"}
    thumbnailer_class = {"package": "Thumbnailer", "name": "generator_domain.thumbnailer"}
    host = "0.0.0.0"
    port = 8000
    dbschema = "http://"
    dbhost = "localhost"
    dbport = "8000"
    dbendpoint = "storage"
