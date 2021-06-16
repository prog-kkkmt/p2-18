package client;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.nio.file.NoSuchFileException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class Handler implements Runnable{
    private Server server;
    Scanner inReq = null;//Получение запроса с клиента
    PrintWriter outReq = null;//отправка на сервер
    private static final String HOST = "localhost";//host
    private static final int PORT = 6542;//port
    private Socket clientSocket = null;//Данные для обратной связи
    private String login;//логин юзера
    private String password;//пасс юзера
    private String loginPassword;//логин пассворд
    private boolean authorized = false;
    private boolean foundAuthorize;
    private boolean loginBusy;

    //создание подключения
    public Handler(Socket socket, Server server){
        try{
            this.server = server;//Сервер
            this.clientSocket = socket;//сокет обратной связи
            this.outReq = new PrintWriter(socket.getOutputStream());//поток вывода
            this.inReq = new Scanner(socket.getInputStream());//поток чтения
        }catch (Exception e){
            System.out.println(e);//вывод ошибки подключения
        }
    }

    public void run() {
        try{
            while (true){
                if(inReq.hasNextLine()){//если новый запрос
                    String clientReqText =  inReq.nextLine();//получение запроса
                    this.requestHandler(clientReqText);
                }
            }

        }catch (NoSuchElementException e){
            server.sendMsgToAll("sending: invalid login or pass\n");
            outReq.println("Invalid log or pass");
            outReq.flush();
        }catch (Exception e){
            System.out.println(e);
        }

    }
    public void sendMsgFromServer(String msg) {
        try {
            server.addInfoToLog("Sending " + msg + " from server to all clients\n");
            outReq.println("server: " + msg);
            outReq.flush();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void sendMsg(String msg) {
        try {
            outReq.println(login + ": " + msg);
            outReq.flush();
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }

    public void requestHandler(String msg) {
        server.addInfoToLog("got request: " + msg + "\n");//log
        try {
            if (msg.contains("/login")) {
                if(!authorized){
                    Scanner msgScanner = new Scanner(msg);
                    msgScanner.next();
                    login = msgScanner.next();
                    password = msgScanner.next();
                    Path path = Paths.get("bd.txt");//Адрес бд))
                    Scanner bdChecker = new Scanner(path);//Сканер для бд
                    foundAuthorize = false;
                    loginPassword = new String(login + " " + password);
                    while (bdChecker.hasNextLine()) {
                        if (bdChecker.nextLine().equals(loginPassword)) {
                            foundAuthorize = true;
                            server.addInfoToLog("succuess login for " + login + "\n");
                            this.authorized = true;
                            outReq.println("welcome " + login);
                            outReq.flush();
                            break;
                        }
                    }
                    if(!foundAuthorize){
                        server.addInfoToLog("invalid login or password" + "\n");
                        outReq.println("invalid login or password");
                        outReq.flush();
                        }
                }else {
                    outReq.println("you are already authorized");
                    outReq.flush();
                }
            }
            else if (msg.contains("/reg")) {
                Scanner msgScanner = new Scanner(msg);
                msgScanner.next();
                login = msgScanner.next();
                password = msgScanner.next();
                loginPassword = new String(login + " " + password);
                Path path = Paths.get("bd.txt");//Адрес бд))
                Scanner bdChecker = new Scanner(path);
                loginBusy = false;
                while (bdChecker.hasNextLine()) {//проверка на занятый логин
                    String currentBdCheck = bdChecker.nextLine();
                    Scanner handlerForCurrentCheck = new Scanner(currentBdCheck);
                    if(handlerForCurrentCheck.next().equals(login)){
                        outReq.println("login busy");
                        outReq.flush();
                        server.addInfoToLog("login busy " + login + "\n");
                        loginBusy = true;
                        break;
                    }
                }//если логин свободный
                if(!loginBusy) {
                    FileWriter adderToBd = new FileWriter(String.valueOf(path), true);
                    adderToBd.write("\n" + loginPassword);
                    server.addInfoToLog("succuess reg " + loginPassword + "\n");//log
                    outReq.println("succuess reg " + login);
                    outReq.flush();
                    adderToBd.close();
                }
            }
            else if (msg.contains("/msgToAll")) {
                if(authorized ) {
                    String sendThisMsgToAll = msg.substring(10, msg.length());
                    server.addInfoToLog("sending msg to all clients: " + sendThisMsgToAll + "\n");
                    server.sendMsgToAll(sendThisMsgToAll);
                }else{
                    server.addInfoToLog("error : not authorized sending message" + "\n");
                    outReq.println("you cant send message without authorization");
                    outReq.flush();
                }
            }
        } catch (NoSuchElementException e) {
            server.addInfoToLog("Missed login or pass in request || invalid log or pass" + "\n");//log
        } catch (NoSuchFileException e) {
            server.addInfoToLog("Base date not found " + "\n");
        } catch (IOException e) {
            server.addInfoToLog("IOE exeption in handler contact Kostya to fix error in server, remember this code!");
        }

    }


}

