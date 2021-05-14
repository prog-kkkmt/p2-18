package com.SoftDevTimeSheet.restService;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.ReportDaysValue;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.parsers.StringToReportDaysValueParser;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class TimesheetService {
    IWorkerDAO dao = new WorkerDAO();

    public List<WorkedDay> allWorkersMakeReport(String date, String reportDays){
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate localDate = LocalDate.parse(date, dtf);
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(reportDays);
        return dao.getReportForAllWorkers(localDate,reportDaysValue);
    }
}
