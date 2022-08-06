import csv 
import json
from flask import Flask

app = Flask(__name__)


class QuestionBank:
    # def __init__(self, path_to_question_bank):
    #     self.path_to_question_bank = path_to_question_bank

    @app.route("/questionbank")
    def read_question_bank(self, path_to_question_bank):
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
        pseudo-code:
        1. Call read_question_bank which will read the question bank csv
        2. Parse the results from previous call and randomly choose 6 question categories
        and 5 questions for each category
        3. Remove any existing question categories and add the question categories from previous step in
        the /dynamicconfigurations/dynamicwheelsectors.json file
        4. Remove any existing data and add question category, question text, answers,
        and score value to /dynamicconfigurations/questionsforcurrentgame.json file
        :return: None
        """

    def get_questions_for_current_game(self):
        """
        This method will read /dynamicconfigurations/questionsforcurrentgame.json and pass a json
        object back to the caller
        :return: Questions for current game
        """


if __name__ == "__main__":
    app.run(debug=True)