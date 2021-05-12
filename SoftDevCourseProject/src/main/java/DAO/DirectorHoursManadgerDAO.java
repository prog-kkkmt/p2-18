package DAO;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;

public class DirectorHoursManadgerDAO implements IDirectorHoursManadgerDAO {

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public boolean addHours(String workerName, LocalDate date, int hoursToAdd) {
        try(Connection connection = DriverManager.getConnection(url,user,pass)){
            try(PreparedStatement state = connection.prepareStatement("UPDATE hours SET hours = hours + (?) WHERE NAME = (?) AND date = (?)")){
                state.setInt(1, hoursToAdd);
                state.setString(2,workerName);
                state.setString(3,String.valueOf(date));
                if(state.executeUpdate() != 0){
                    System.out.println("hours for " +workerName + " for date " + date + " valueHours " + hoursToAdd + " updated");//sout if updated
                    return true;
                }else{
                    System.out.println("failed update hours for worker");//sout if not updated
                    return false;
                }
            }catch (SQLException e){
                System.out.println("sql excption in directorHoursManadgeDao" + e);
            }
        }catch (SQLException e){
            System.out.println("sql exeption in directorHoursManadgeDao" + e);
        }
        return false;
    }
}
