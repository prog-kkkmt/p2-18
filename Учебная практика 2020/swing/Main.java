import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileReader;
import java.io.FileWriter;

import javax.swing.*;

public class Main implements ActionListener{
    File file = new File("");//Объект для хранения пути
    public Main(){
        int width = 800, height = 600;//размеры окна
        JFrame mainFrame = new JFrame("My Text Redactor");//создание основного окна
        mainFrame.setVisible(true);
        mainFrame.setSize(width,height);

        JTextArea textField = new JTextArea();//создание поля для ввода текста
        textField.setLocation(0,0);
        textField.setSize(width,height-50);
        textField.setVisible(false);


        JMenu menu = new JMenu("file");//создание меню
        JMenuItem file1 = new JMenuItem("New"); //создание вариантов меню
        JMenuItem file2 = new JMenuItem("Save");
        JMenuItem file3 = new JMenuItem("Open");
        JMenuBar menuFileBar = new JMenuBar();//добавление меню в бар который потом надо добавить в основной бар



//open
        file1.addActionListener(new ActionListener() {//обработчик для открытия
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();//выбор файла
                if(chooser.showSaveDialog(null) == JFileChooser.APPROVE_OPTION){//если подтвердили выбор
                    file = chooser.getSelectedFile();//объекту для хранения файла присвоить путь
                    textField.setVisible(true);//включить поле для ввода
                    try(FileWriter writer = new FileWriter(file)){//считать текст файла
                        char[] buffer = new char[(int) file.length()];
                        writer.write("");
                        writer.flush();
                    }catch (Exception e1){
                        System.out.println(e1);
                    }
                }

            }
        });

        //save
        file2.addActionListener(new ActionListener() {//обработка сохранения
            @Override
            public void actionPerformed(ActionEvent e) {
             try(FileWriter writer = new FileWriter(file)){//записать в файл по открытому пути
                 char [] buf = new char[(int)file.length()];
                 writer.write(textField.getText());//из текста в поле ввода
                 writer.flush();
             }catch (Exception e1){
                 System.out.println(e1);
             }
            }
        });

        //new
        file3.addActionListener(new ActionListener() {//обработчик для нового файла
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();//выбор места для файла
                chooser.showOpenDialog(mainFrame);
                file = chooser.getSelectedFile();// сохранить путь до файла
                textField.setVisible(true);//включить отображение файла
                try(FileReader reader = new FileReader(file)){//считать файл записать в буфффер
                    char [] buffer =  new char [(int) file.length()];
                    reader.read(buffer);
                    textField.setText(new String(buffer));//записать в поле
                }catch (Exception e1){
                    System.out.println(e1);
                }
            }
        });
        mainFrame.setLayout(null);

        menu.add(file1);//добавление элеметов в основное окно
        menu.add(file2);
        menu.add(file3);
        menuFileBar.add(menu);
        mainFrame.setJMenuBar(menuFileBar);
        mainFrame.add(textField);
    }

    public static void main (String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new Main();
            }
        });

    }

    @Override
    public void actionPerformed(ActionEvent e) {

    }
}