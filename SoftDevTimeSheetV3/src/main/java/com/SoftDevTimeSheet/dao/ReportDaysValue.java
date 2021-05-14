package com.SoftDevTimeSheet.dao;

public enum ReportDaysValue {
//month = 31 day, week = 7 day, day = 1day
    MONTH(31), WEEK(7), DAY(1);
    private int value;
    ReportDaysValue(int value){
        this.value = value;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
}
