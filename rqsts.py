import requests
a = {"coord":{"lon":-0.1257,"lat":51.5085},
 "weather":[{"id":804,"main":"Clouds","description":"overcast clouds","icon":"04d"}],
 "base":"stations","main":{"temp":290.46,"feels_like":290.28,"temp_min":289.1,
 "temp_max":291.86,"pressure":1016,"humidity":78},
 "visibility":10000,
 "wind":{"speed":5.36,"deg":142,"gust":6.71},
 "clouds":{"all":100},
 "dt":1664891729,
 "sys":{"type":2,"id":2075535,"country":"GB","sunrise":1664863537,"sunset":1664904762},
 "timezone":3600,"id":2643743,"name":"London","cod":200}

 
def reqs(place):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&APPID=4c00b3191c06fb02182473dd7523df7b'.format(place)
    res = requests.get(url)
    return res

def reqs_form(res):
    res1 = res.json()
    # = res
    ans = 'Weather: {}, {}\n'.format(res1['weather'][0]['main'], res1['weather'][0]['description'])
    ans = ans + 'Temperature: {}, feels like: {}, maximum temperature: {}\n'.format(str(float(res1['main']['temp']) - 273.15)[:4], 
    str(float(res1['main']['feels_like'] - 273.15))[:4], str(float(res1['main']['temp_max'] - 273.15))[:4])

    ans = ans + 'Pressure: {}\n'.format(res1['main']['pressure'])
    ans = ans + 'Wind speed: {}\n'.format(res1['wind']['speed'])

    return ans

#ans = reqs_form(a)
#print(ans)
#res = reqs('London,uk')
#res1 = reqs_form(res)
#print(res1)
