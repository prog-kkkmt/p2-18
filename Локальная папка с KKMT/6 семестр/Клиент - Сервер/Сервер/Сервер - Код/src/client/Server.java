package client;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.PrintWriter;
import  java.net.ServerSocket;
import  java.net.Socket;
import java.util.ArrayList;
import java.util.Scanner;



public class Server extends JFrame {
    private static int PORT = 6542;
    private JTextField jtfMessage;
    private JTextField jtfName;
    private JTextArea jtaTextAreaMessage;


    private ArrayList<Handler> requests = new ArrayList<Handler>();
    public Server(){
        Socket clientSocket = null; //сокет для обратной связи
        ServerSocket serverSocket = null;//сокет для этого сервера


        try {
            serverSocket = new ServerSocket(PORT);
            setBounds(600, 300, 600, 500);
            setTitle("Server");
            setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
            jtaTextAreaMessage = new JTextArea();
            jtaTextAreaMessage.setEditable(false);
            jtaTextAreaMessage.setLineWrap(true);
            JScrollPane jsp = new JScrollPane(jtaTextAreaMessage);
            add(jsp, BorderLayout.CENTER);
            JPanel bottomPanel = new JPanel(new BorderLayout());
            add(bottomPanel, BorderLayout.SOUTH);
            JButton jbSendMessage = new JButton("Отправить всем подключенным клиентам");
            bottomPanel.add(jbSendMessage, BorderLayout.EAST);
            jtfMessage = new JTextField();
            bottomPanel.add(jtfMessage, BorderLayout.CENTER);

            jbSendMessage.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                        SendMsgToAllFromServer(jtfMessage.getText());
                }
            });

            setVisible(true);
            System.out.println("server on");

                while(true){
                    clientSocket = serverSocket.accept();
                Handler handler = new Handler(clientSocket, this);
                requests.add(handler);
                new Thread(handler).start();

            }
        }catch(Exception e){
            System.out.println(e);
        }
    }


    public void addInfoToLog(String info){
        jtaTextAreaMessage.append(info);
    }

    public void SendMsgToAllFromServer(String msg){
        for(Handler item : requests){
            item.sendMsgFromServer(msg);
        }
    }
    public void sendMsgToAll(String msg){
        for(Handler item : requests){
            item.sendMsg(msg);
        }
    }
}
