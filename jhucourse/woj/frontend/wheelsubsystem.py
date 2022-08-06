import json
# import os
import sys
from jhucourse.woj.logging.centrallogging import CentralLogger
from flask import Flask

app = Flask(__name__)

WHEEL_SECTOR_STORAGE_FILE = 'wheelsectorsstore.json'
STATIC_CONFIGS_DIR = ''


class WheelSubsystem:
    """
    This method will get all the static wheel sectors from json config file
    """
    @staticmethod
    def get_static_wheel_sectors() -> json:
        """
        This method will get the static wheel sectors from the /staticconfigurations/wheelsectorstore.json file
        :return: json object for static wheel sectors
        """
        try:

            wheel_sector_list = []
            wheel_sectors_file = open(STATIC_CONFIGS_DIR + WHEEL_SECTOR_STORAGE_FILE, 'r')
            wheel_sectors_data = json.load(wheel_sectors_file)

            for sector in wheel_sectors_data['sector_details']:
                wheel_sector_list.append(sector['sector_name'])
                # TODO: Implementation pending
                #  Add code for using the sector data upstream
            wheel_sectors_file.close()

            golog = CentralLogger()
            golog.log_for_woj(__name__, 'INFO', 'get_static_wheel_sectors method execution complete')

            return wheel_sectors_data

        except Exception:
            golog = CentralLogger()
            golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
            print(sys.exc_info())

    def get_dynamic_wheel_sectors(self) -> json:
        """
        This method will get the dynamic wheel sectors based on randomly chosen questions and associated
        question categories
        pseudo-code:
        1. Read /dynamicconfigurations/dynamicwheelsectors.json file
        2. Return the wheel sectors to the caller
        :return: json object for dynamic wheel sectors
        """

        return "dynamic wheel sectors"

    def get_all_wheel_sectors(self) -> json:
        """
        This method will return all wheel sectors (static + dynamic) to the caller
        pseudo-code:
        1. call get_static_wheel_sectors
        2. call get_dynamic_wheel_sectors
        3. merge json from the previous 2 calls
        4. return json
        :return: json object for all wheel sectors (static + dynamic)
        """
        wss = WheelSubsystem()
        static_wheel_sectors = WheelSubsystem.get_static_wheel_sectors()
        dynamic_wheel_sectors = wss.get_dynamic_wheel_sectors()

        all_wheel_sectors: json = ''
        return all_wheel_sectors


if __name__ == "__main__":
    app.run(debug=True)
    # print("something")
