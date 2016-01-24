import json

import configparser
from twitter import *

config = configparser.ConfigParser()
config.read('config.ini');

tApi = Twitter(auth=OAuth(
    config['OAUTH']['TOKEN'],
    config['OAUTH']['TOKEN_SECRET'],
    config['OAUTH']['CONSUMER_KEY'],
    config['OAUTH']['CONSUMER_KEY_SECRET']
));

def search_for_term(term):
    return json.dumps(tApi.search.tweets(q = term),
                        sort_keys=True,
                        indent=4,
                        ensure_ascii=False)

if __name__ == "__main__":
    try:
        # statuses = tApi.statuses.home_timeline(count=5)
        # print(json.dumps(statuses[0], sort_keys=True, indent=4))
        search_results = tApi.search.tweets(q = "プログラミング　大学生 ", lang="ja", count=100)
        filtered = []
        for status in search_results['statuses']:
            d = {}
            d["id"] = status['id']
            d["user"] = {}
            d["user"]["name"] = status['user']['name']
            d["user"]["description"] = status['user']['description']
            d["entities"] = status['entities'];
            filtered.append(d)


            # print(status['user']['description'])
            print(" < " + status['text'] + " > ")
        with open('./results.json','w',encoding='utf8') as outfile:
            json.dump(filtered, outfile, ensure_ascii=False, indent=4)

        # print(tApi.search.tweets(q = "艦これ"))
    except TwitterHTTPError as e:
        print(e)
