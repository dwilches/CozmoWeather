
import cozmo

import cozmo_utils


# display_image_file_on_face(robot, image_name, time_to_display):


def cozmo_program(robot: cozmo.robot.Robot):
    display_image_file_on_face(robot, "images/cloudy.png", 3000)


if __name__ == "__main__":
    cozmo.run_program(cozmo_program)
