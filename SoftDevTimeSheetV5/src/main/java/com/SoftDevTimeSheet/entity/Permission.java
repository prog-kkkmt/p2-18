package com.SoftDevTimeSheet.entity;

public enum Permission {
    WORKER_SELF_HOURS_ADD("worker:addHours"),
    WORKER_SELF_REPORT_MAKE("worker:selfReport"),
    DIRECTOR_MAKE_REPORT_FOR_ALL("director:allWorkerReport"),
    DIRECTOR_MAKE_REPORT_FOR_WORKER("director:workerReport"),
    DIRECTOR_ADD_HOURS_TO_WORKER("director:addHoursToWorker"),
    DIRECTOR_ADD_NEW_WORKER("director:addNewWorker"),
    DIRECTOR_REMOVE_WORKER("director:removeWorker"),
    FREELANCER_SELF_HOURS_ADD("freelancer:addHours"),
    FREELANCER_SELF_REPORT_MAKE("freelancer:selfReport");

    private final String permission;

    Permission(String permission) {
        this.permission = permission;
    }

    public String getPermission() {
        return permission;
    }
}
