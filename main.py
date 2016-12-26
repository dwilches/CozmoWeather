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

import time

import cozmo

import cozmo_utils
import api_accuweather

# City name. Put something very explicit, this acts as a search string in AccuWeather's API
CITY_NAME = "Laramie,WY"


# Main function
def cozmo_program(robot: cozmo.robot.Robot):
    ''' Retrieves the weather forecast from AccuWeather and asks Cozmo to read it out loud '''

    # Put a lot of volume so we can hear Cozmo across home
    robot.set_robot_volume(1.0)

    # Some light effect, lift and head animation
    robot.set_backpack_lights(cozmo.lights.red_light,
                              cozmo.lights.green_light,
                              cozmo.lights.blue_light,
                              cozmo.lights.white_light,
                              cozmo.lights.red_light)
    robot.set_lift_height(0).wait_for_completed()
    robot.set_lift_height(0.25).wait_for_completed()
    robot.set_lift_height(0).wait_for_completed()
    robot.set_head_angle(cozmo.util.Angle(degrees=20)).wait_for_completed()
    robot.set_head_angle(cozmo.util.Angle(degrees=0)).wait_for_completed()

    # Get the forecast from AccuWeather
    forecasts = api_accuweather.get_forecasts(CITY_NAME)

    # Cozmo requests your attention
    action = robot.say_text("Weather Forecast")
    cozmo_utils.display_image_file_on_face(robot, "images/weather.png")
    action.wait_for_completed()

    # For each day's forecast, read it out loud
    for fc in forecasts["Forecasts"]:
        # Get the date from the forecast (yyyy-mm-dd)
        date = fc["Date"]

        # Get the forecast itself (sunny, cloudy, etc.)
        fc_text = fc["Forecast"]

        # Converts the date from the format 'yyyy-mm-dd' to the name of the
        # weekday (Tuesday, Monday, etc.)
        date_text = time.strftime("%A", time.strptime(date, "%Y-%m-%d"))

        # Finally, Cozmo tells the forecast
        cozmo_utils.say_forecast(robot, date_text, fc_text)

    # Turn off the lights, although it seems to be automatic
    robot.set_backpack_lights_off()


# Start the program
if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
