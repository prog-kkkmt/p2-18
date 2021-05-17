package com.SoftDevTimeSheet.dao.DAOInterfaces;

import com.SoftDevTimeSheet.dao.ReportDaysValue;
import com.SoftDevTimeSheet.entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IWorkerDAO {
    public boolean addHoursToWorker(String workerName, LocalDate date, int hoursToAdd);
    public List<WorkedDay>getReportForAllWorkers(LocalDate date, ReportDaysValue reportDaysValue);
    public List<WorkedDay> getReportForWorkerByName(String workerName, LocalDate date, ReportDaysValue reportDaysValue);
    public int getTotalHoursWorkedByWorkerName(String workerName);
    public boolean addNewWorkerWithRole(String workerName, String password, String role);
}
