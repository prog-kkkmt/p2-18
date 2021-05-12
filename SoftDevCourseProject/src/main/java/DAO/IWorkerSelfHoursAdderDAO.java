package DAO;

import java.time.LocalDate;

public interface IWorkerSelfHoursAdderDAO {
    boolean stateWorkerSelfHoursAdd(String workerName, LocalDate date, int hoursToAdd);
}

