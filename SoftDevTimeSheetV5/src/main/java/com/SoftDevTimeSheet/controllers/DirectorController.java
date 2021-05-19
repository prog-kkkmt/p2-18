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
@RequestMapping("/Director")
public class DirectorController {

    @PreAuthorize("hasAuthority('director:allWorkerReport')")
    @GetMapping("/makeReportForAll")
    public List<WorkedDay> allWorkersReport(@RequestParam(value = "date", defaultValue = "03-01-2021")String date,
                                            @RequestParam(value = "daysValue", defaultValue = "week") String reportDays){
        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.directorMakeReportForAllWorkers(date,reportDays);
    }

    @PreAuthorize("hasAuthority('director:addHoursToWorker')")
    @GetMapping("/addHoursToWorker")
    public boolean addHours(@RequestParam(value = "name",defaultValue = "default") String name,
                           @RequestParam(value = "date",defaultValue = "01-01-2001") String date,
                           @RequestParam(value = "hours",defaultValue = "88") String hours){

        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.directorAddHoursToWorker(name, date, hours);
    }


    @PreAuthorize("hasAuthority('director:workerReport')")
    @GetMapping("/makeReportForWorker")
    public List<WorkedDay> allWorkersReport(@RequestParam(value = "name",defaultValue = "kostya")String name,
                                            @RequestParam(value = "date", defaultValue = "03-01-2021")String date,
                                            @RequestParam(value = "daysValue", defaultValue = "week") String reportDays){

        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.directorMakeReportByWorkerName(name, date, reportDays);
    }

    @PreAuthorize("hasAuthority('director:addNewWorker')")
    @GetMapping("/addNewWorker")
    public boolean addNewWorker(@RequestParam(value = "name",defaultValue = "default") String name,
                            @RequestParam(value = "password",defaultValue = "default") String password,
                            @RequestParam(value = "role",defaultValue = "worker") String role){

        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.directorAddNewWorker(name,password,role);
    }

    @PreAuthorize("hasAuthority('director:removeWorker')")
    @GetMapping("/removeWorker")
    public boolean removeWorker(@RequestParam(value = "name", defaultValue = "default") String name){
        TimesheetService timesheetService = new TimesheetService();
        return timesheetService.directorRemoveWorker(name);
    }


}
