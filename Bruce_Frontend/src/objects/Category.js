import Question from "./Question"

class Category {
    currentQuestion;
    name;
    quesitons;

    constructor(name, jo) {
        this.name = name;
        let tempArray = []
        jo.map((jsonQuestion) => (
            tempArray.push(new Question(jsonQuestion))
        ))
        this.questions = tempArray;
        this.currentQuestion = 0;
    }

    getCurrentQuestion(){return this.currentQuestion} //DONE
    getName(){return this.name;} //DONE

    nextQuestion(){
        //DONE
        this.currentQuestion +=1;
        return this.questions[this.currentQuestion-1];
    }
}

export default Category