package DAO;

import Entity.WorkedDay;

import java.sql.*;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class DirectorHoursReportMakerForWorkerDAO implements IDirectorHoursReportMakerForWorker {

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public List<WorkedDay> getHoursReportForWorker(String workerName, LocalDate date, ReportDaysValue daysValue) {
        List<WorkedDay> reports = new ArrayList<>(10);

        try(Connection connection = DriverManager.getConnection(url, user,pass)){
            try(PreparedStatement state = connection.prepareStatement("SELECT name, date, hours FROM hours WHERE name = (?) and date between (?) and (?)")){
                state.setString(1, workerName);
                state.setString(2,String.valueOf(date));
                state.setString(3, String.valueOf(date.minusDays(daysValue.getValue())));
                ResultSet resultSet = state.executeQuery();
                final DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");

                while (resultSet.next()) {
                    WorkedDay tmpWorkedDayForReport = new WorkedDay();
                    tmpWorkedDayForReport.setWorkerName(resultSet.getString("name"));
                    LocalDate localDate = LocalDate.parse(resultSet.getString("date"), dtf);
                    tmpWorkedDayForReport.setWorkDate(localDate);
                    tmpWorkedDayForReport.setHoursWorked(resultSet.getInt("hours"));
                    reports.add(tmpWorkedDayForReport);
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