package com.SoftDevTimeSheet.restService;

import com.SoftDevTimeSheet.dao.DAOException;
import com.SoftDevTimeSheet.dao.IWorkerDAO;
import com.SoftDevTimeSheet.dao.ReportDaysValue;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.parsers.StringToReportDaysValueParser;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Collections;
import java.util.List;
import java.util.Locale;

public class TimesheetService {
    IWorkerDAO dao = new WorkerDAO();

    //director make report for all workers by date
    public List<WorkedDay> directorMakeReportForAllWorkers(String date, String reportDays){

        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate localDate = LocalDate.parse(date, dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(reportDays);

        try {
            return dao.getReportForAllWorkers(localDate, reportDaysValue);
        }catch (DAOException e){
            e.printStackTrace();
        }

        return Collections.emptyList();
    }


    //director make report for worker by name
    public List<WorkedDay> directorMakeReportByWorkerName(String workerName, String stringDate, String stringReportDaysValue){
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);
        List<WorkedDay> reportsByName = null;

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        try{
            reportsByName = dao.getReportForWorkerByName(workerName,date,reportDaysValue);
        }catch (DAOException e){
            e.printStackTrace();
        }

        if (reportsByName != null) {
            return reportsByName;
        }

        return Collections.emptyList();
    }

    //director add hours to worker by name
    public boolean directorAddHoursToWorker(String workerName, String stringDate, String stringHoursToAdd){
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);

        boolean added = false;

        try{
            added = dao.addHoursToWorker(workerName,date,hoursToAdd);
        }catch (DAOException e){
            e.printStackTrace();
        }

        return added;
    }

    public boolean directorAddNewWorker(String workerName, String password,String role){
        role = role.toUpperCase(Locale.ROOT);

        boolean added = false;
        try{
            added = dao.addNewWorkerWithRole(workerName,password,role);
        }catch(DAOException e){
            e.printStackTrace();
        }
        return added;
    }

    public boolean directorRemoveWorker(String workerName){
        boolean removed = false;
        try{
            removed = dao.removeWorkerByName(workerName);
        }catch (DAOException e){
            e.printStackTrace();
        }
        return removed;
    }

    public boolean workerAddSelfHours(String stringDate, String stringHoursToAdd){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);

        boolean added = false;

        try{
            added = dao.addHoursToWorker(workerName,date,hoursToAdd);
        }catch (DAOException e){
            e.printStackTrace();
        }

        return added;
    }

    public List<WorkedDay> workerMakeSelfReport(String stringDate, String stringReportDaysValue){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        List<WorkedDay> reportByName = null;

        try {
            reportByName = dao.getReportForWorkerByName(workerName, date, reportDaysValue);
        }catch (DAOException e){
            e.printStackTrace();
        }

        if(reportByName != null){
            return reportByName;
        }

        return Collections.emptyList();
    }

    public boolean freelancerAddSelfHours(String stringDate, String stringHoursToAdd){
        String workerName = getCurrentUsername();

        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);
        LocalDate nowLocalDate = LocalDate.now();

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);
        boolean added = false;

        //well date
        if(date.equals(nowLocalDate) || date.equals(nowLocalDate.minusDays(1)) || date.equals(nowLocalDate.minusDays(2))){
            try{
                added = dao.addHoursToWorker(workerName,date,hoursToAdd);
            }catch (DAOException e){
                e.printStackTrace();
            }
        }

        return added;
    }

    public List<WorkedDay> freelancerMakeSelfReport(String stringDate, String stringReportDaysValue){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        List<WorkedDay> reportByName = null;
        try{
            reportByName = dao.getReportForWorkerByName(workerName,date,reportDaysValue);
        }catch (DAOException e){
            e.printStackTrace();
        }

        if(reportByName != null){
            return reportByName;
        }

        return  Collections.emptyList();
    }

    private String getCurrentUsername() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        return auth.getName();
    }

}
