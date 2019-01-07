import requests
from app.config import Config

def query_get_all():
    queryset = []
    url = '{}{}:{}/storage/'.format(Config.dbschema, Config.dbhost, Config.dbport)
    print(url)
    response = requests.get(url).json()
    for item in response:
        queryset.append({'uid': item.get('uid'), 'thumb': item.get('base64_200_thumb')})
    return queryset
