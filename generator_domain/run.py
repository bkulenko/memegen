import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
from api.app import make_app
from api.config import Config

app = make_app()

if __name__ == '__main__':
    app.run(Config.host, Config.port, Config.debug)
