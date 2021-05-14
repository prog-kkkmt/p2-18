package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.SoftDevTimeSheetApplication;
import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class TotalHoursWorkedController {
    //get number of hours by worker name
    @GetMapping("/hours")
    public int getHours(@RequestParam(value = "name", defaultValue = "kostya") String name){
        IWorkerDAO dao =  new WorkerDAO();
        return dao.getTotalHoursWorkedByWorkerName(name);
    }
}
