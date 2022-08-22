import csv 
import json
import random
from jhucourse.woj.logging.centrallogging import CentralLogger
import sys

# app = Flask(__name__)

PATH_TO_QB = 'jhucourse/woj/staticconfigurations/test_question.csv'
QUESTIONS_FOR_CURRENT_GAME = 'jhucourse/woj/dynamicconfigurations/questionsforcurrentgame.json'
DYNAMIC_WHEEL_SECTORS = 'jhucourse/woj/dynamicconfigurations/dynamicwheelsectors.json'


class QuestionBank:
    # @app.route("/questionbank")
    def read_question_bank(self) -> list:
        path_to_question_bank = PATH_TO_QB
        json_question_array = []
        with open(path_to_question_bank, encoding='utf-8') as csv_file:
            csv_read = csv.DictReader(csv_file) 
            for row in csv_read: 
                json_question_array.append(row)
        # Return user a json object which contains jeopardy questions 
        return json_question_array

    def choose_and_write_random_questions(self):
        """
        This method will randomly select questions, set wheel sectors from the categories,
        and add question details for the game session
        1. Call read_question_bank which will read the question bank csv
        2. Parse the results from previous call and randomly choose 6 question categories
        and 5 questions for each category
        3. Remove any existing question categories and add the question categories from previous step in
        the /dynamicconfigurations/dynamicwheelsectors.json file
        4. Remove any existing data and add question category, question text, answers,
        and score value to /dynamicconfigurations/questionsforcurrentgame.json file
        :return: None
        """
        try:
            json_question_array = self.read_question_bank()
            len_of_json_question_array = len(json_question_array)
            json_cat_array = [json_question_array[random.randint(1, len_of_json_question_array-1)]["Category"]]
            cat_array_counter = 0
            minimal_question_array = []

            while cat_array_counter < 6:    # maximum 6 question categories
                random_question_indices = [question_index for question_index, random_cat_name
                                           in enumerate(json_question_array)
                                           if random_cat_name["Category"] == json_cat_array[cat_array_counter]]
                _question_count = 0
                with open(QUESTIONS_FOR_CURRENT_GAME, "w") as question_file:
                    for random_question_index in random_question_indices:
                        _question_count += 1
                        if _question_count > 5:
                            break   # break if the number of questions for a category exceeds 5
                        minimal_question_array.append(json_question_array[random_question_index])
                    json.dump(minimal_question_array, question_file, indent=4)

                _random_num_gen_trial = 0   # to keep track of runaway while loop. sh!t happens
                _random_index = random.randint(1, len_of_json_question_array - 1)
                while any(ele == json_question_array[_random_index]["Category"] for ele in json_cat_array):
                    _random_index = random.randint(1, len_of_json_question_array - 1)
                    _random_num_gen_trial += 1
                    if _random_num_gen_trial > len_of_json_question_array:
                        break   # this will invoke if random number gen have tried enough
                        # but unable to find new distinct categories due to limited types of distinct categories in QB
                if _random_num_gen_trial <= len_of_json_question_array:   # only add more cat if while is not exhausted
                    json_cat_array.append(json_question_array[_random_index]["Category"])
                cat_array_counter += 1

            with open(DYNAMIC_WHEEL_SECTORS, "w") as wheel_sector_file:
                json.dump(json_cat_array, wheel_sector_file, indent=2)

        except Exception:
            golog = CentralLogger()
            golog.log_for_woj(__name__, 'ERROR', sys.exc_info())
            print(sys.exc_info())

    def get_questions_for_current_game(self):
        """
        This method will read /dynamicconfigurations/questionsforcurrentgame.json and pass a json
        object back to the caller
        :return: Questions for current game
        """

# if __name__ == "__main__":
#     app.run(debug=True)
