import requests
from pprint import pprint

URL = 'https://api.stackexchange.com/search?fromdate=1651708800&todate=1651881600&order=desc&sort=activity&tagged=python&site=stackoverflow'
def stack_overflow_request():
    response = requests.get(url=URL)
    return response.json()

def sorting_out():
    links = stack_overflow_request()
    for k in links['items']:
        print(k['link'])

def main():
    sorting_out()
    
if __name__ == '__main__':
    main()
    