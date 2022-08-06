import Category from "./Category"
import round_one_data from "../testData/round1.json"

class QuestionBank {
    categories;

    constructor() {
        let tempArray = []
        round_one_data.map((jsonCategory) => (
            tempArray.push(new Category(jsonCategory.name,jsonCategory.questions))
        ))
        this.categories = tempArray;
    }

    answerQuestion(category){
        return this.categories[category].nextQuestion()
    } //Done

    getAllCategories(){
        //DONE
        let arrayOfCategoryNames = [];
        this.categories.forEach(category => arrayOfCategoryNames.push(category.getName()));
        return arrayOfCategoryNames;
    }

    getCategoryName(category){return this.categories[category].getName();}

    getCurrentQuestion(category){return this.categories[category].getCurrentQuestion()}

    getAvailableCategories(){
        // DONE
        let arrayOfCategoryNames = []
        this.categories.forEach((category) => {
            if (category.getCurrentQuestion() < 5){
                arrayOfCategoryNames.push(category.getName())
                console.log()
            } else {
                arrayOfCategoryNames.push("")
            }
        })
        return arrayOfCategoryNames
    }
    

    verifyQuestionsRemaining(){
        // DONE
        for (const category of this.categories){
            if (category.getCurrentQuestion < 5){
                return true
            }
        }
        return false
    }

    verifyQuestionsInCategory(category){
        // DONE
        if (this.categories[category].getCurrentQuestion() < 5){
            return true
        }
        return false
    }
}

export default QuestionBank