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

import cozmo
from PIL import Image

# Default time to display the images in the screen
DISPLAY_TIME = 3000.0


# Function taken from the Cozmo's SDK tutorials, and modified a bit by me.
# Returns the Action.
def display_image_file_on_face(robot: cozmo.robot.Robot, image_name):
    # load image and convert it for display on cozmo's face
    image = Image.open(image_name)

    # resize to fit on Cozmo's face screen
    resized_image = image.resize(cozmo.oled_face.dimensions(), Image.NEAREST)

    # convert the image to the format used by the OLED screen
    face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                             invert_image=True)

    # display image for 'time_to_display' milliseconds
    return robot.display_oled_face_image(face_image, DISPLAY_TIME)


def say_forecast(robot: cozmo.robot.Robot, date_text, fc_text):
    '''
    Receives a date in a readable format (Monday, Saturday, etc.) and a forecast
    text (something like 'thunderstorm' or 'sunny') and displays an appropriate
    image in the OLED face of Cozmo and speaks the forecast out loud.
    '''

    # Given the keywords in the forecast text, find a suitable icon
    icon_file = get_icon_for_forecast(fc_text)

    # Expand abbreviations int he forecast so Cozmo can speak them properly
    forecast = fix_forecast_abbrevs(date_text + ": " + fc_text)

    # Ask Cozmo to speak the forecsat
    action = robot.say_text(forecast)

    # Show the icon in Cozmo's face
    display_image_file_on_face(robot, icon_file)

    # Wait until Cozmo has finished speaking.
    action.wait_for_completed()


def fix_forecast_abbrevs(forecast):
    ''' Expand abbreviations int he forecast so Cozmo can speak them properly '''
    return forecast.replace('w/', 'with')


def get_icon_for_forecast(forecast):
    ''' Given the keywords in the forecast text, find a suitable icon '''

    # Search for the first keyword that matches the forecast text (case insensitive)
    forecast = forecast.lower()
    if "cloud" in forecast:
        return "images/cloudy.png"
    elif "sunny" in forecast:
        return "images/sunny.png"
    elif "rain" in forecast:
        return "images/rainy.png"
    elif "snow" in forecast:
        return "images/snow.png"
    elif "storm" in forecast:
        return "images/storm.png"
    else:
        return "images/unknown.png"
