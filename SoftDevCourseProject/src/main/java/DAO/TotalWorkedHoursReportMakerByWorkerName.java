package DAO;

import java.sql.*;

public class TotalWorkedHoursReportMakerByWorkerName implements ITotalWorkedHoursReportMakerByWorkerName {
    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public int getHoursWorkedValueByWorkerName(String workerName) {
        int totalHoursWorked = 0;
        try(Connection connection = DriverManager.getConnection(url,user,pass)){
            try (PreparedStatement state = connection.prepareStatement("SELECT hours FROM hours WHERE name = (?)")){
                state.setString(1,workerName);
                ResultSet resultSet = state.executeQuery();
                while (resultSet.next()){
                    totalHoursWorked += resultSet.getInt("hours");
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }catch (SQLException e){
            System.out.println(e);
        }
        return totalHoursWorked;
    }
}
