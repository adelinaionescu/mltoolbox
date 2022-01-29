def search_city(query):
    '''Look for a given city and disambiguate between several candidates.
        Return one city (or None)'''
    url = f"{BASE_URI}/api/location/search/?query={query}"
    response = requests.get(url)
    response_json = response.json()
    if response_json == []:
        return None
    dict_resonse = response_json[0]
    return dict_resonse