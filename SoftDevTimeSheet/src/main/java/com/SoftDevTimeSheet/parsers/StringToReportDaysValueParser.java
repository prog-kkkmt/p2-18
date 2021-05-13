package com.SoftDevTimeSheet.parsers;

import com.SoftDevTimeSheet.dao.ReportDaysValue;

public class StringToReportDaysValueParser {
    public static ReportDaysValue parseStingToDaysValue(String reportDaysStringValue) {
        if(reportDaysStringValue.toUpperCase().equals("MONTH")){
            return ReportDaysValue.MONTH;
        }else if(reportDaysStringValue.toUpperCase().equals("WEEK")){
            return ReportDaysValue.WEEK;
        }else if(reportDaysStringValue.toUpperCase().equals("DAY")){
            return ReportDaysValue.DAY;
        }
        return ReportDaysValue.DAY;//default value
    }
}
