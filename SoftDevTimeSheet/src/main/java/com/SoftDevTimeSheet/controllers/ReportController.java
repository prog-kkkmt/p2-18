package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.ReportDaysValue;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.parsers.StringToReportDaysValueParser;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

@RestController
public class ReportController {
    @GetMapping("/report")
        public List<WorkedDay> getReport(@RequestParam(value = "name", defaultValue = "leha") String name,
                                         @RequestParam(value = "date", defaultValue = "01-01-2021") String date,
                                         @RequestParam(value = "daysValue", defaultValue = "week") String reportDays){

            IWorkerDAO dao = new WorkerDAO();
            DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
            LocalDate localDate = LocalDate.parse(date, dtf);
            return dao.getReportForWorkerByName(name, localDate, StringToReportDaysValueParser.parseStingToDaysValue(reportDays));
        }
}
