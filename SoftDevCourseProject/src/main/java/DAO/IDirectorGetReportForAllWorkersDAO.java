package DAO;

import Entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IDirectorGetReportForAllWorkersDAO {
    List<WorkedDay> getReportForDays(LocalDate date, ReportDaysValue value);//dont forget to create class
}


