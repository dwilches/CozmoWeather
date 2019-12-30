# Weather Forecasts for Cozmo

This program connects to AccuWeather's API and downloads the weather forecast for the next 5 days.
Then, the forecast is sent to a Cozmo robot that reads it out loud, while showing in its face an image
representing the weather conditions.

[![Cozmo Weather](http://img.youtube.com/vi/cwfPXQNXe5k/0.jpg)](http://www.youtube.com/watch?v=cwfPXQNXe5k)

# Getting started

## Dependencies

Install the Python package 'requests' by issuing this command:

    pip3 install requests




## Input your AccuWeather key

Open the file `api_accuweather.py` and put your AccuWeather application key in this line:

    API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

For example, if your key is `54FECBEF45ECBE4FE12354FECBE5ECBE` then the line should read:

    API_KEY = '54FECBEF45ECBE4FE12354FECBE5ECBE'

You can get a free key from AccuWeather in this url: http://developer.accuweather.com/

That should be all, now run the file `main.py` while Cozmo is in the SDK mode.


# Cozmo SDK

Notice CozmoWeather depends on Cozmo's SDK from Anki. There are installation instructions in their website:
https://developer.anki.com/blog/learn/tutorial/getting-started-with-the-cozmo-sdk/index.html

# License:

```html
Licensed under the Apache License, Version 2.0 (the "License");
you may not use these files except in compliance with the License.
You may obtain a copy of the License in the file LICENSE.txt or at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
