package DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;

public class DirectorAddStateWorkerDAO implements IDirectorAddStateWorkerDAO{

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public boolean addStateWorker(String WorkerName, Roles role) {
     try( Connection connection = DriverManager.getConnection(url,user,pass)){
         try(PreparedStatement state = connection.prepareStatement("INSERT INTO Workers (NAME ,ROLE) VALUES ((?), (?))")){
             state.setString(1,WorkerName);
             state.setString(2, role.getRoleName());
             if(state.executeUpdate() != 0){
                 System.out.println("created new worker " + WorkerName + " with role " + role.getRoleName());//sout if added new worker
                 return true;
             }else {
                 System.out.println("new worker not created"); //sout if not added new worker
                 return false;
             }
         }


     }catch (SQLException e){
         System.out.println("exception in DirectorAddStateWorkerDAO" + e);
     }
     return false;
    }
}
