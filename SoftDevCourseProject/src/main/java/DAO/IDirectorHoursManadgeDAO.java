package DAO;

import java.time.LocalDate;

public interface IDirectorHoursManadgeDAO {
    public boolean addHours(String workerName, LocalDate date, int hoursToAdd);
}
