import check50
import requests
@check50.check()
def exists():
    """space.py exists"""
    check50.exists("space.py")

@check50.check(exists)
def test_json_response():
    """space.py makes a successful request and parses JSON response"""
    

    url = "http://api.open-notify.org/astros.json"
    response = requests.get(url)

    api_dict = response.json()

    result = check50.run("python3 space.py")

    # Add more specific checks for names and crafts
    result.stdout(api_dict["people"][0]["name"]).stdout(api_dict["people"][0]["craft"])
    result.stdout(api_dict["people"][1]["name"]).stdout(api_dict["people"][0]["craft"])
    result.stdout(api_dict["people"][2]["name"]).stdout(api_dict["people"][0]["craft"])
    # Add more names and crafts as needed

    result.exit(0)
