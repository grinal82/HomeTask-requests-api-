import requests

def super_hero_request(url):
    response = requests.get(url)
    return response.json()
    
hulk = super_hero_request(r'https://superheroapi.com/api/2619421814940190/search/Hulk')
captain_america = super_hero_request(r'https://superheroapi.com/api/2619421814940190/search/Captain_America')
thanos = super_hero_request(r'https://superheroapi.com/api/2619421814940190/search/Thanos')

hulk_intell =int((hulk['results'][0]['powerstats']['intelligence']))
cap_america_intel = int((captain_america['results'][0]['powerstats']['intelligence']))
thanos_intell = int((thanos['results'][0]['powerstats']['intelligence']))

comparison_list = {}
comparison_list['Hulk'] = hulk_intell
comparison_list['Captain America'] = cap_america_intel
comparison_list['Thanos'] = thanos_intell
comparison_list = sorted(comparison_list, key=comparison_list.get, reverse=True)

print(f'Самый умнный супергерой- {comparison_list[0]}(интеллект {thanos_intell}), затем {comparison_list[1]}(интеллект {hulk_intell}),затем {comparison_list[2]}(интеллект {cap_america_intel})')


# print(f'Интеллект Hulk равен: {hulk_intell}')
# print(f'Интеллект Captain America равен: {cap_america_intel}')
# print(f'Интеллект Thanos равен: {thanos_intell}')

