package DAO;

import Entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IStateWorkerSelfReportMakerDAO {
    List<WorkedDay> getStateWorkerSelfReport(String workerName, LocalDate date, ReportDaysValue reportDaysValue);
}
