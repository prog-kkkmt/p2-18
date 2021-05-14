package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;

@RestController
public class AddHoursController {
    @GetMapping("/addhours")
    public String addHours(@RequestParam(value = "name",defaultValue = "default") String name,
                           @RequestParam(value = "date",defaultValue = "default") String date,
                           @RequestParam(value = "hourstoadd",defaultValue = "-1") String hours){
        IWorkerDAO dao = new WorkerDAO();
        if(dao.addHoursToWorker(name, LocalDate.parse(date),Integer.parseInt(hours))){
            return "added";
        }else{
            return "not added";
        }
    }
}
