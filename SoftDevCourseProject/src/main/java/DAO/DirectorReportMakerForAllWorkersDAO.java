package DAO;

import Entity.WorkedDay;

import java.sql.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class DirectorReportMakerForAllWorkersDAO implements IDirectorReportMakerForAllWorkersDAO {

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public List<WorkedDay> getReportForDays(LocalDate date, ReportDaysValue value) {
        List<WorkedDay> reports = new ArrayList<>(10);
        try(Connection connection = DriverManager.getConnection(url, user,pass)){
            try(PreparedStatement state = connection.prepareStatement("SELECT name, date, hours FROM HOURS WHERE date between (?) AND (?)")){
                state.setString(1,String.valueOf(date));
                state.setString(2,String.valueOf(date.minusDays(value.getValue())));
                ResultSet resultSet = state.executeQuery();
                final DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
                while (resultSet.next()){
                    WorkedDay workedDayForReport = new WorkedDay();
                    workedDayForReport.setWorkerName(resultSet.getString("name"));
                    LocalDate tmpDate = LocalDate.parse(resultSet.getString("date"), dtf);
                    workedDayForReport.setWorkDate(tmpDate);
                    workedDayForReport.setHoursWorked(resultSet.getInt("hours"));
                    reports.add(workedDayForReport);
                }


            }catch (SQLException e){
                System.out.println(e);
            }
        }catch (SQLException e){
            System.out.println(e);
        }

        return reports;
    }
}
