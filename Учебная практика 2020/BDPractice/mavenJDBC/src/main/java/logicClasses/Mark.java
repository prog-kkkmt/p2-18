package logicClasses;

public class Mark {
    private long id;
    private String markName;

    public Mark() {
        id = -1;
        markName = "default";
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getMarkName() {
        return markName;
    }

    public void setMarkName(String markName) {
        this.markName = markName;
    }

    @Override
    public String toString() {
        return "Mark{" +
                "id=" + id +
                ", markName='" + markName + '\'' +
                '}';
    }
}
