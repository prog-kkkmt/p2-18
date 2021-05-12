package DAO;

import java.time.LocalDate;

public interface IDirectorHoursManadgerDAO {
    public boolean addHours(String workerName, LocalDate date, int hoursToAdd);
}
