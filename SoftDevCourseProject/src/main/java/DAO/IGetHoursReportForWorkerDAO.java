package DAO;

import Entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IGetHoursReportForWorkerDAO {
    public List<WorkedDay> getHoursReportForWorker(String workerName, LocalDate date, ReportDaysValue daysValue);
}

