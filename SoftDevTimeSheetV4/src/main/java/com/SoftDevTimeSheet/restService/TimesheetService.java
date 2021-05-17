package com.SoftDevTimeSheet.restService;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.ReportDaysValue;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.WorkedDay;
import com.SoftDevTimeSheet.parsers.StringToReportDaysValueParser;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
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

        return dao.getReportForAllWorkers(localDate,reportDaysValue);
    }


    //director make report for worker by name
    public List<WorkedDay> directorMakeReportByWorkerName(String workerName, String stringDate, String stringReportDaysValue){
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        List<WorkedDay> reportByName = dao.getReportForWorkerByName(workerName,date,reportDaysValue);
        if(!reportByName.isEmpty()){
            return reportByName;
        }
        return  reportByName;
    }

    //director add hours to worker by name
    public boolean directorAddHoursToWorker(String workerName, String stringDate, String stringHoursToAdd){
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);

        if(dao.addHoursToWorker(workerName,date,hoursToAdd)){
            return true;
        }else{
            return false;
        }
    }

    public boolean directorAddNewWorker(String workerName, String password,String role){
        role = role.toUpperCase(Locale.ROOT);

        if(dao.addNewWorkerWithRole(workerName,password,role)){
            return true;
        }else {
            return false;
        }
    }

    public boolean workerAddSelfHours(String stringDate, String stringHoursToAdd){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);
        if(dao.addHoursToWorker(workerName,date,hoursToAdd)){
            return true;
        }else{
            return false;
        }
    }

    public List<WorkedDay> workerMakeSelfReport(String stringDate, String stringReportDaysValue){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        List<WorkedDay> reportByName = dao.getReportForWorkerByName(workerName,date,reportDaysValue);
        if(!reportByName.isEmpty()){
            return reportByName;
        }
        return  reportByName;
    }

    public boolean freelancerAddSelfHours(String stringDate, String stringHoursToAdd){
        String workerName = getCurrentUsername();

        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);
        LocalDate nowLocalDate = LocalDate.now();

        //string hours to int hours
        int hoursToAdd = Integer.parseInt(stringHoursToAdd);

        if(date.equals(nowLocalDate) || date.equals(nowLocalDate.minusDays(1)) || date.equals(nowLocalDate.minusDays(2))){
            //well date
            if(dao.addHoursToWorker(workerName,date,hoursToAdd)){
                return true;
            }else {
                return false;
            }
        }else {
            //if date longer that 2 days from now
            return false;
        }
    }

    public List<WorkedDay> freelanerMakeSelfReport(String stringDate, String stringReportDaysValue){
        String workerName = getCurrentUsername();
        //string date to local date
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse(stringDate,dtf);

        //string report days value to report days value
        ReportDaysValue reportDaysValue = StringToReportDaysValueParser.parseStingToDaysValue(stringReportDaysValue);

        List<WorkedDay> reportByName = dao.getReportForWorkerByName(workerName,date,reportDaysValue);
        if(!reportByName.isEmpty()){
            return reportByName;
        }
        return  reportByName;
    }

    private String getCurrentUsername() {
        Authentication auth = SecurityContextHolder.getContext().getAuthentication();
        return auth.getName();
    }

}
