import csv 

class QuestionBank:
    def __init__(self, path_to_question_bank):
        self.path_to_question_bank = path_to_question_bank

    def read_question_bank(self):
        json_question_array = []
        with open(self.path_to_question_bank , encoding='utf-8') as csv_file: 
            csv_read = csv.DictReader(csv_file) 
            for row in csv_read: 
                json_question_array.append(row)
        # Return user a json object which contains jeopardy questions 
        return json_question_array
        
