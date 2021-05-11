package DAO;

public enum Roles {
    Director("director"), stateWorker("stateWorker");

    private String roleName;

    Roles(String roleName){
        this.roleName = roleName;
    }

    public String getRoleName() {
        return roleName;
    }

    public void setRoleName(String roleName) {
        this.roleName = roleName;
    }
}
