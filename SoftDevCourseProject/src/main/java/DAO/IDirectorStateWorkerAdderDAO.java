package DAO;

import DAO.Roles;

public interface IDirectorStateWorkerAdderDAO {
    public boolean addStateWorker(String WorkerName, Roles role);
}
