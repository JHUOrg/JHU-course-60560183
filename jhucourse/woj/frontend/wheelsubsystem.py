import json
import os
import sys
# from jhucourse.woj.logging.centrallogging import CentralLogger
from flask import Flask

app = Flask(__name__)

WHEEL_SECTOR_STORAGE_FILE = 'wheelsectorsstore.json'
STATIC_CONFIGS_DIR = '/Users/somsubhr/JHU-course-60560183/jhucourse/woj/staticconfigurations/'


class WheelSubsystem:
    """
    This method will get all the static wheel sectors from json config file
    """
    @app.route("/wheelsectors")
    def get_static_wheel_sectors():
        try:

            wheel_sector_list = []
            wheel_sectors_file = open(STATIC_CONFIGS_DIR + WHEEL_SECTOR_STORAGE_FILE, 'r')
            wheel_sectors_data = json.load(wheel_sectors_file)

            for sector in wheel_sectors_data['sector_details']:
                wheel_sector_list.append(sector['sector_name'])
                # TODO: Implementation pending
                #  Add code for using the sector data upstream
            wheel_sectors_file.close()

            return str(wheel_sectors_data)

            # golog = CentralLogger()
            # golog.log_for_woj(__name__, 'INFO', 'get_static_wheel_sectors method execution complete')
        except Exception:
            # golog = CentralLogger()
            # golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
            print(sys.exc_info())


if __name__ == "__main__":
    app.run(debug=True)
    # print("something")

