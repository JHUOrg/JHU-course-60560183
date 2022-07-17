import json
import os
"""
This class will be used for the Wheel experience.
"""

WHEEL_SECTOR_STORAGE_FILE = 'wheelsectorsstore.json'
STATIC_CONFIGS_DIR = 'jhucourse/woj/staticconfigurations/'


class WheelSubsystem:
    """
    This method will get all the static wheel sectors from json config file
    """
    @classmethod
    def get_static_wheel_sectors(cls):
        with os.scandir(STATIC_CONFIGS_DIR) as config_files:
            for entry in config_files:

                if entry.name == WHEEL_SECTOR_STORAGE_FILE:

                    wheel_sectors_file = open(STATIC_CONFIGS_DIR + entry.name, 'r')
                    wheel_sectors_data = json.load(wheel_sectors_file)

                    for sector in wheel_sectors_data['sector_details']:
                        print(sector['sector_name'])
                    wheel_sectors_file.close()
                    break
        config_files.close()