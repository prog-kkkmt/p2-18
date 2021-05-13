package com.SoftDevTimeSheet.entity;

public class Worker {
    private String name;
    private Role role = new Role("undefined");
    private Integer workedHours;

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Role getRole() {
        return role;
    }

    public void setRole(Role role) {
        this.role = role;
    }

    @Override
    public String toString() {
        return "name " + name + " role " + role.getRoleName();
    }
}
