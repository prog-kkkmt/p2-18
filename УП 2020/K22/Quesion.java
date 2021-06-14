package sample;
//структруа вопроса
import java.util.Scanner;

class Question {
    //структура одного вопроса
    String question;
    String[] answers = new String[3];
    String trueAnswer;
    String answer;
    boolean correctly;

    //констурктор новых объектов с вопросами
    Question(String quest, String answ1, String answ2, String answ3, String trAnswer){
        this.question = quest;
        this.answers[0] = answ1;
        this.answers[1] = answ2;
        this.answers[2] = answ3;
        this.trueAnswer = trAnswer;
    }
}