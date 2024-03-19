import check50
import requests
@check50.check()
def exists():
    """weather.py exists"""
    check50.exists("weather.py")

@check50.check(exists)
def test_json_response():
    """weather.py makes a successful request and parses JSON response"""
    city = "tbilisi"
    api_key = "45fca6311fa8a41b61aee922ec47c231"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
            'q': city,
            'appid': api_key,
            'units': 'imperial'
    }

    response = requests.get(base_url, params=params)
    weather_data = response.json()
    temperature = weather_data['main']['temp']

    result = check50.run("python3 space.py").stdin("tbilisi")
    result.stdout("Temperature in Tbilisi is:", temperature)
    # result.exit(0)