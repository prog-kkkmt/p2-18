package sample;
//подключение библеотек для работы с гтовыми классами java и javaFX
import java.net.URL;
import java.util.ResourceBundle;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.RadioButton;
import javafx.scene.control.ToggleGroup;
import javafx.scene.text.Text;
import java.io.IOException;//инклюды для работы с готовыми классами java
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.ArrayList;
import java.util.List;

public class Controller {
// подключение кнопок
    @FXML
    private ResourceBundle resources;

    @FXML
    private URL location;

    @FXML
    private Text totalTrueAnswers;

    @FXML
    private Text question;

    @FXML
    private RadioButton answer1;

    @FXML
    private ToggleGroup answer;

    @FXML
    private RadioButton answer2;

    @FXML
    private RadioButton answer3;

    @FXML
    private Text Author1;

    @FXML
    private Text Author2;

    @FXML
    private Text Author3;

    @FXML
    private Text Author4;

    @FXML
    private Button sumbitBtn;

    int i = 0;
    int k = 0;
    int totalTrueAnswerFromUser = 0;

    @FXML
    void initialize() {
        //открытие файла с воппрсами
        Path path = Path.of("D:\\dataForNovProject\\test1.txt");
        try {
            //читает файл и записывает в коллекцию лист
            List<String> list = Files.readAllLines(path); //P.s файл имеет определнную структуру для данных
            ArrayList<Question> arListQuestions = new ArrayList<>();
            // работа с данными файла создает вопросы на основе текста файла
            for(int i = 0;i<list.size();i+=5){
                arListQuestions.add(new Question(list.get(i), list.get(i+1), list.get(i+2), list.get(i+3), list.get(i+4)));
            }
            //запуск викторины
            question.setText(arListQuestions.get(k).question);
            answer1.setText(arListQuestions.get(k).answers[0]);
            answer2.setText(arListQuestions.get(k).answers[1]);
            answer3.setText(arListQuestions.get(k).answers[2]);
            sumbitBtn.setOnAction(event -> {//если нажали на подтверлить и что то выбрано
                RadioButton selectedRadio = (RadioButton) answer.getSelectedToggle();
                if(selectedRadio != null) {
                    if(arListQuestions.get(k).trueAnswer.equals(selectedRadio.getText()))//проверить правильно или нет
                        totalTrueAnswerFromUser++;//если правильно то кол-во правельных ответов +1
                    totalTrueAnswers.setText(String.valueOf(totalTrueAnswerFromUser));
                    if (k + 1 == arListQuestions.size()) {
                        answer1.setVisible(false);//если вопрос последний то скрыть все кнопки
                        answer2.setVisible(false);
                        answer3.setVisible(false);
                        sumbitBtn.setVisible(false);
                        question.setText("Вопросы закончились\nАвторы:\nКороленко\nКузнецов\nСлесарев\nБезбородов");
                    } else {
                        k++;//если вопрос не последний показать следующий
                        answer1.setSelected(false);//сбросить прошлый выбор
                        answer2.setSelected(false);
                        answer3.setSelected(false);
                        question.setText(arListQuestions.get(k).question);//заполнить новые вопросы и ответы
                        answer1.setText(arListQuestions.get(k).answers[0]);
                        answer2.setText(arListQuestions.get(k).answers[1]);
                        answer3.setText(arListQuestions.get(k).answers[2]);
                    }
                }
            });


        }catch (IOException e) { //тк метод readAllLines throws Exeption
            System.out.println(e);
        }


    }
}