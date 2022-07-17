import os 
import sys
import json

class QuestionBank:
    def __init__(self, path_to_question_bank):
        self.path_to_question_bank = path_to_question_bank

    def read_question_bank(self):
        with open(self.path_to_question_bank) as json_file:
            json_question_bank = json.load(json_file)
            json_file.close()
            return json_question_bank
