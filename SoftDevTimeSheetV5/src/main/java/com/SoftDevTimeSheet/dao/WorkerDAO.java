package com.SoftDevTimeSheet.dao;

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
    public boolean addHoursToWorker(String workerName, LocalDate date, int hoursToAdd) throws DAOException{ // timesheet method, that adds hours to worker by name
        Connection connection = null;
        PreparedStatement statement = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{

                if(timeSheetContainsDateForWorker(workerName, date)){
                    //contains date for same worker
                    statement = connection.prepareStatement("UPDATE timesheet SET hours = hours + (?) where name = (?) and date = (?)");
                    statement.setInt(1, hoursToAdd);
                    statement.setString(2,workerName);
                    statement.setString(3,String.valueOf(date));
                    if(statement.executeUpdate() > 0){
                        return true;
                    }

                }else{
                    //if no worker for this date
                    statement = connection.prepareStatement("INSERT INTO timesheet (name, date, hours) values ((?),(?),(?))");
                    statement.setString(1,workerName);
                    statement.setString(2, String.valueOf(date));
                    statement.setInt(3, hoursToAdd);
                    if(statement.executeUpdate() > 0){
                        return true;
                    }
                }
            }catch (SQLException e){
                System.out.println(e + "3");
            }finally {
                if(statement != null){
                    statement.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e+ "4");
            throw new DAOException("failed to add hours",e);
        }finally {
            if(connection != null){
                try {
                    connection.close();
                }catch (SQLException e){
                    System.out.println(e + "5");
                }
            }
        }
        return false;
    }

    private boolean timeSheetContainsDateForWorker (String workerName, LocalDate date) throws DAOException {
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("SELECT name, date from timesheet where name = (?) and date = (?)");
                statement.setString(1,workerName);
                statement.setString(2,String.valueOf(date));
                resultSet = statement.executeQuery();
                if(resultSet.next()) {
                    String tmpName = resultSet.getString("name");
                    String tmpDate = resultSet.getString("date");
                    if (tmpName.equals(workerName) && tmpDate.equals(String.valueOf(date))) {
                        return true;//contains
                    }
                }
            }catch (SQLException e){
                e.printStackTrace();
            }finally {
                if(statement != null){
                    statement.close();
                }
                if(resultSet != null){
                    resultSet.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e + "1");
        }finally {
            try {
                if (connection != null) {
                    connection.close();
                }
            } catch (SQLException e) {
                System.out.println( e + "2");
            }
        }
        return false; // not contains
    }

    @Override
    public List<WorkedDay> getReportForAllWorkers(LocalDate date, ReportDaysValue reportDaysValue) throws DAOException { //Director report maker DAO for all workers
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        List<WorkedDay> allWorkersReport = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("SELECT name, date, hours from timesheet where date between (?) and (?)");
                statement.setString(1,String.valueOf(date.minusDays(reportDaysValue.getValue())));
                statement.setString(2,String.valueOf(date));
                allWorkersReport = new ArrayList<>(10);
                resultSet = statement.executeQuery();
                while(resultSet.next()){
                    WorkedDay workedDay = new WorkedDay();
                    workedDay.setWorkerName(resultSet.getString("name"));
                    workedDay.setWorkDate(LocalDate.parse(resultSet.getString("date")));
                    workedDay.setHoursWorked(resultSet.getInt("hours"));
                    allWorkersReport.add(workedDay);
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
        }catch(SQLException e){
            System.out.println(e);
            throw new DAOException("failed to get report for all workers", e);
        }finally {
            if(connection != null){
                try {
                    connection.close();
                }catch (SQLException e){
                    System.out.println(e);
                }
            }
        }
        return allWorkersReport;
    }

    // method that getting a report for worker by
    //worker name
    @Override
    public List<WorkedDay> getReportForWorkerByName(String workerName, LocalDate date, ReportDaysValue reportDaysValue)  throws DAOException {
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
            throw new DAOException("failed to get report for worker by name",e);
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

    //DAO method that returns number of worked hours by worker name
    @Override
    public int getTotalHoursWorkedByWorkerName(String workerName) throws DAOException  {
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
            throw new DAOException("failed to get total hours for worker by worker name", e);
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

    @Override
    public boolean addNewWorkerWithRole(String workerName, String password, String role) throws DAOException {
        Connection connection = null;
        PreparedStatement statement = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("INSERT INTO roles (name, password, role)values ((?),(?),(?))");
                statement.setString(1,workerName);
                statement.setString(2,password);
                statement.setString(3, role);
                if(statement.executeUpdate() > 0){
                    return true;
                }
            }catch(SQLException e){
                if(statement !=null){
                    statement.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e);
            throw new DAOException("failed to add new worker with role", e);
        }finally {
            try{
                if(connection != null) {
                    connection.close();
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }
        return false;
    }

    @Override
    public boolean removeWorkerByName(String workerName) throws DAOException {
        Connection connection = null;
        PreparedStatement statement = null;
        try{
            connection = DAOConnectionFactory.getConnection();
            try{
                statement = connection.prepareStatement("DELETE FROM roles where name = (?)");
                statement.setString(1,workerName);
                if(statement.executeUpdate() > 0){
                    return true;
                }else{
                    return false;
                }
            }catch (SQLException e){
                System.out.println(e);
            }finally {
                if(statement != null){
                    statement.close();
                }
            }
        }catch (SQLException e){
            System.out.println(e);
            throw new DAOException("failed to remove worker by name", e);
        }finally {
            try{
                if(connection !=null){
                    connection.close();
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }
        return false;
    }


}
