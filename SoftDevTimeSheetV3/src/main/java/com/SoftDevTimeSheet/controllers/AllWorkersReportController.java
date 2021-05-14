package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.parsers.StringToReportDaysValueParser;
import com.SoftDevTimeSheet.restService.TimesheetService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;

@RestController
public class AllWorkersReportController {
    //only director can run this controller
    @GetMapping("/allreport")
        public List<WorkedDay> getAllWorkersReport(@RequestParam(value = "date", defaultValue = "01-01-2000")String date,
                                                   @RequestParam(value = "daysValue", defaultValue = "week") String reportDays){

        TimesheetService timesheetService = new TimesheetService();

        return timesheetService.allWorkersMakeReport(date,reportDays);
        }
}

