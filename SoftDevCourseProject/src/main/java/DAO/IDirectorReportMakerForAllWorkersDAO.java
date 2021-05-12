package DAO;

import DAO.ReportDaysValue;
import Entity.WorkedDay;

import java.time.LocalDate;
import java.util.List;

public interface IDirectorReportMakerForAllWorkersDAO {
    List<WorkedDay> getReportForDays(LocalDate date, ReportDaysValue value);//dont forget to create class
}


