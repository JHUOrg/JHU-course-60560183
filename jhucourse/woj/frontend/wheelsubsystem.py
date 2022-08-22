import json
# import os
import sys
from jhucourse.woj.logging.centrallogging import CentralLogger
import random

STATIC_CONFIGS_DIR = 'jhucourse/woj/staticconfigurations/'
DYNAMIC_CONFIGS_DIR = 'jhucourse/woj/dynamicconfigurations/'

WHEEL_SECTOR_STORAGE_FILE = 'wheelsectorsstore.json'
WHEEL_SECTOR_DYNAMIC_FILE = 'dynamicwheelsectors.json'


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
            wheel_sectors_file.close()

            golog = CentralLogger()
            golog.log_for_woj(__name__, 'INFO', 'get_static_wheel_sectors method execution complete')

            return wheel_sector_list

        except Exception:
            golog = CentralLogger()
            golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
            print(sys.exc_info())

    def get_dynamic_wheel_sectors(self) -> json:
        """
        This method will get the dynamic wheel sectors from the /dynamicconfigurations/dynamicwheelsectors.json file
        based on randomly chosen questions and associated question categories

        :return: json object for dynamic wheel sectors
        """
        try:
            wheel_sectors_file = open(DYNAMIC_CONFIGS_DIR + WHEEL_SECTOR_DYNAMIC_FILE, 'r')
            wheel_sectors_data = json.load(wheel_sectors_file)

            wheel_sectors_file.close()

            golog = CentralLogger()
            golog.log_for_woj(__name__, 'INFO', 'get_dynamic_wheel_sectors method execution complete')

            return wheel_sectors_data

        except Exception:
            golog = CentralLogger()
            golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
            print(sys.exc_info())

    def get_all_wheel_sectors(self) -> json:
        """
        This method will return all wheel sectors (static + dynamic) to the caller
        :return: json object for all wheel sectors (static + dynamic)
        """
        wss = WheelSubsystem()
        dynamic_wheel_sectors = wss.get_dynamic_wheel_sectors()
        static_wheel_sectors = WheelSubsystem.get_static_wheel_sectors()

        all_wheel_sectors: json = dynamic_wheel_sectors + dynamic_wheel_sectors + static_wheel_sectors
        random.shuffle(all_wheel_sectors)
        return all_wheel_sectors


# if __name__ == "__main__":
#     app.run(debug=True)
#     # print("something")
