package com.SoftDevTimeSheet.dao;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.entity.Role;
import com.SoftDevTimeSheet.entity.WorkedDay;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class WorkerDAO implements IWorkerDAO {
    @Override
    public Role getWorkerRoleByName(String workerName) {
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        Role workerRole = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("SELECT role FROM roles WHERE name = (?)");
                statement.setString(1,workerName);
                    resultSet = statement.executeQuery();
                if (resultSet != null) {
                    resultSet.next();
                    workerRole = new Role(resultSet.getString("role"));
                }
            }catch (SQLException e){
                System.out.println(e);
            }finally {
                if(statement != null){
                    statement.close();
                }
                if(resultSet != null){
                    resultSet.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e);
        }finally {
            try {
                if(connection != null) {
                    connection.close();
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }
        return workerRole;
    }

    @Override
    public boolean addHoursToWorker(String workerName, LocalDate date, int hoursToAdd) {
        return false;
    }

    @Override
    public List<WorkedDay> getReportForAllWorkers(LocalDate date, ReportDaysValue reportDaysValue) {
        return null;
    }

    @Override
    public List<WorkedDay> getReportForWorkerByName(String workerName, LocalDate date, ReportDaysValue reportDaysValue) {
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        List<WorkedDay> reportForWorker = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("SELECT name, date, hours FROM timesheet where name = (?) AND date BETWEEN (?) AND (?)");
                statement.setString(1, workerName);
                statement.setString(2, String.valueOf(date.minusDays(reportDaysValue.getValue())));
                statement.setString(3, String.valueOf(date));
                reportForWorker = new ArrayList<>(10);
                resultSet = statement.executeQuery();
                while(resultSet.next()){
                    WorkedDay workedDay = new WorkedDay();
                    workedDay.setWorkerName(resultSet.getString("name"));
                    workedDay.setWorkDate(LocalDate.parse(resultSet.getString("date")));
                    workedDay.setHoursWorked(resultSet.getInt("hours"));
                    reportForWorker.add(workedDay);
                }

            }catch (SQLException e){
                System.out.println(e);
            }finally {
                if(statement != null){
                    statement.close();
                }
                if(resultSet != null){
                    resultSet.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e);
        }finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }
        return reportForWorker;
    }

    @Override
    public int getTotalHoursWorkedByWorkerName(String workerName) {
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        int totalHoursWorked = 0;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("SELECT hours from timesheet where name = (?)");
                statement.setString(1,workerName);
                resultSet = statement.executeQuery();
                while (resultSet.next()){
                    totalHoursWorked += resultSet.getInt("hours");
                }
            }catch (SQLException e){
                System.out.println(e);
            }finally {
                if(statement != null){
                    statement.close();
                }
                if(resultSet != null){
                    resultSet.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e);
        }finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            }catch (SQLException e) {
                System.out.println(e);
            }
        }
        return totalHoursWorked;
    }
}
