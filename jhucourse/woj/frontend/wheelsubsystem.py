import json
import os
import sys
from jhucourse.woj.logging.centrallogging import CentralLogger

"""
This class will be used for the Wheel experience
"""

WHEEL_SECTOR_STORAGE_FILE = 'wheelsectorsstore.json'
STATIC_CONFIGS_DIR = 'jhucourse/woj/staticconfigurations/'


class WheelSubsystem:
    """
    This method will get all the static wheel sectors from json config file
    """
    @classmethod
    def get_static_wheel_sectors(cls):
        try:
            with os.scandir(STATIC_CONFIGS_DIR) as config_files:
                for entry in config_files:

                    if entry.name == WHEEL_SECTOR_STORAGE_FILE:

                        wheel_sectors_file = open(STATIC_CONFIGS_DIR + entry.name, 'r')
                        wheel_sectors_data = json.load(wheel_sectors_file)

                        for sector in wheel_sectors_data['sector_details']:
                            print(sector['sector_name'])
                            # TODO: Implementation pending
                            #  Add code for using the sector data upstream
                        wheel_sectors_file.close()
                        break
            config_files.close()

            golog = CentralLogger()
            golog.log_for_woj(__name__, 'INFO', 'get_static_wheel_sectors method execution complete')
        except Exception:
            golog = CentralLogger()
            golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
