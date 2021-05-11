package DAO;

public enum ReportDaysValue {
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
