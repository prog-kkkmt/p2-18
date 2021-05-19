package com.SoftDevTimeSheet.dao;

import com.SoftDevTimeSheet.entity.WorkedDay;
import java.time.LocalDate;
import java.util.List;

public interface IWorkerDAO {
    public boolean addHoursToWorker(String workerName, LocalDate date, int hoursToAdd) throws DAOException;
    public List<WorkedDay>getReportForAllWorkers(LocalDate date, ReportDaysValue reportDaysValue) throws DAOException;
    public List<WorkedDay> getReportForWorkerByName(String workerName, LocalDate date, ReportDaysValue reportDaysValue) throws DAOException;
    public int getTotalHoursWorkedByWorkerName(String workerName) throws DAOException;
    public boolean addNewWorkerWithRole(String workerName, String password, String role) throws DAOException;
    public boolean removeWorkerByName(String workerName) throws DAOException;
}
