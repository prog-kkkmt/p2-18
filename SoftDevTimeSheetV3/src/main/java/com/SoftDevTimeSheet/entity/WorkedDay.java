package com.SoftDevTimeSheet.entity;

import java.time.LocalDate;


//worked day entity
public class WorkedDay {
    private String workerName;
    private int hoursWorked;
    private LocalDate workDate;

    public String getWorkerName() {
        return workerName;
    }

    public void setWorkerName(String workerName) {
        this.workerName = workerName;
    }

    public int getHoursWorked() {
        return hoursWorked;
    }

    public void setHoursWorked(int hoursWorked) {
        this.hoursWorked = hoursWorked;
    }

    public LocalDate getWorkDate() {
        return workDate;
    }

    public void setWorkDate(LocalDate workDate) {
        this.workDate = workDate;
    }

    @Override
    public String toString() {
        return "workerName = " + workerName + " workDate=" + workDate + " hoursWorked= " + hoursWorked;
    }
}
