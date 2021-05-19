package com.SoftDevTimeSheet.controllers;


import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.restService.TimesheetService;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("Worker")
public class WorkerController {


    @PreAuthorize("hasAuthority('worker:selfReport')")
    @GetMapping("/selfReport")
    public List<WorkedDay> makeSelfReport(@RequestParam(value = "date", defaultValue = "03-01-2021") String date,
                                          @RequestParam(value = "daysValue", defaultValue = "week") String reportDays){

        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.workerMakeSelfReport(date,reportDays);
    }


    @PreAuthorize("hasAuthority('worker:addHours')")
    @GetMapping("/selfHoursAdd")
    public boolean addHours(@RequestParam(value = "date", defaultValue = "03-01-2021") String date,
                           @RequestParam(value = "hours",defaultValue = "88") String hours){

        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.workerAddSelfHours(date,hours);
    }

}
