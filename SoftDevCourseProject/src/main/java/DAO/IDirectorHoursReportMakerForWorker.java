package DAO;

import DAO.ReportDaysValue;
import Entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IDirectorHoursReportMakerForWorker {
    public List<WorkedDay> getHoursReportForWorker(String workerName, LocalDate date, ReportDaysValue daysValue);
}

