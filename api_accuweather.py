#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
   API calls to the weather forecast services (from AccuWeather).
"""
import sys
import requests


# This should be your own key, created through: http://developer.accuweather.com/
API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


class AccuWeatherAPIError(Exception):
    """Base class for exceptions in this module."""
    pass


#
# Sample input:
# "Laramie,WY"
#
# Sample output:
# 336576
#
def get_location_key(place_name):
    """" Returns the first location that matches the place name passed as parameter """

    params = {'apikey': API_KEY, 'q': place_name}
    r = requests.get('http://dataservice.accuweather.com/locations/v1/search', params=params)
    if r.status_code != requests.codes.ok:
        print("Error querying AccuWeather's API. Did you provide the right API_KEY?", file=sys.stderr)
        results = r.json()
        print("Error message was: {}".format(results["Message"]), file=sys.stderr)
        raise AccuWeatherAPIError()

    results = r.json()
    if len(results) == 0:
        print("No location found with the name: '{}'".format(place_name), file=sys.stderr)
        raise AccuWeatherAPIError()

    return results[0]["Key"]


# Sample input:
# 336576
#
# Sample output:
# {
#   "Summary": "Snowfall late Tuesday night will total 1-3 cm"
#   "Forecasts":
#   [
#     {'Date': '2016-12-25', 'MinTemp': -9.4, 'MaxTemp': 1.7, 'Forecast': 'Freezing rain'},
#     {'Date': '2016-12-26', 'MinTemp': -9.5, 'MaxTemp': -2.9, 'Forecast': 'Mostly sunny'},
#     {'Date': '2016-12-27', 'MinTemp': -3.2, 'MaxTemp': 3.0, 'Forecast': 'Mostly sunny'},
#     {'Date': '2016-12-28', 'MinTemp': -9.2, 'MaxTemp': 0.1, 'Forecast': 'Mostly cloudy w/ flurries'},
#     {'Date': '2016-12-29', 'MinTemp': -4.9, 'MaxTemp': 1.7, 'Forecast': 'Mostly sunny'}
#   ]
# }
#
def get_forecasts_by_key(location_key):
    """ Returns the weather forecast for the place with key 'locationKey' """

    params = {'apikey': API_KEY, 'metric': True}
    r = requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/5day/' + location_key, params=params)
    results = r.json()

    daily_forecasts = []

    for forecast in results["DailyForecasts"]:
        fc = {
            "Date": forecast["Date"][:10],
            "MinTemp": forecast["Temperature"]["Minimum"]["Value"],
            "MaxTemp": forecast["Temperature"]["Maximum"]["Value"],
            "Forecast": forecast["Day"]["IconPhrase"],
        }
        daily_forecasts.append(fc)

    headline = results["Headline"]["Text"]

    return {"Summary": headline, "Forecasts": daily_forecasts}


#
# Sample input:
# Laramie,WY
#
# Sample output:
# {
#   "Summary": "Snowfall late Tuesday night will total 1-3 cm"
#   "Forecasts":
#   [
#     {'Date': '2016-12-25', 'MinTemp': -9.4, 'MaxTemp': 1.7, 'Forecast': 'Freezing rain'},
#     {'Date': '2016-12-26', 'MinTemp': -9.5, 'MaxTemp': -2.9, 'Forecast': 'Mostly sunny'},
#     {'Date': '2016-12-27', 'MinTemp': -3.2, 'MaxTemp': 3.0, 'Forecast': 'Mostly sunny'},
#     {'Date': '2016-12-28', 'MinTemp': -9.2, 'MaxTemp': 0.1, 'Forecast': 'Mostly cloudy w/ flurries'},
#     {'Date': '2016-12-29', 'MinTemp': -4.9, 'MaxTemp': 1.7, 'Forecast': 'Mostly sunny'}
#   ]
# }
#
def get_forecasts(place_name):
    """ Returns the weather forecast for the place named 'placeName' """

    return get_forecasts_by_key(get_location_key(place_name))

