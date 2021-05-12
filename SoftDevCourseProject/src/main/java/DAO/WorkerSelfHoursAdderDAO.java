package DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;

public class WorkerSelfHoursAdderDAO implements IWorkerSelfHoursAdderDAO{
    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public boolean stateWorkerSelfHoursAdd(String workerName, LocalDate date, int hoursToAdd) {
        try (Connection connection = DriverManager.getConnection(url,user,pass)){
            try(PreparedStatement state = connection.prepareStatement("INSERT INTO Hours (name, date, hours) VALUES ((?), (?), (?))")){
                state.setString(1, workerName);
                state.setString(2, String.valueOf(date));
                state.setInt(3, hoursToAdd);
                if(state.executeUpdate()>0){
                    return true;
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }catch (SQLException e){
            System.out.println(e);
        }
        return false;
    }
}
