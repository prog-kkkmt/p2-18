package com.SoftDevTimeSheet.restService;

import com.SoftDevTimeSheet.dao.DAOInterfaces.IWorkerDAO;
import com.SoftDevTimeSheet.dao.WorkerDAO;
import com.SoftDevTimeSheet.entity.Worker;
//service that using auth dao, to get worker if there one in base data
public class AuthService {
    public Worker auth(String name){
        IWorkerDAO dao = new WorkerDAO();
        Worker worker = new Worker();
        worker.setName(name);
        worker.setRole(dao.getWorkerRoleByName(name));
        return worker;
    }
}
