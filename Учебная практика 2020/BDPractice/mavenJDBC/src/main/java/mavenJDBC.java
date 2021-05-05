import DAORealisation.MarkDAO;
import logicClasses.Mark;

import java.sql.*;
import java.util.List;

public class mavenJDBC {
    public static void main(String[] args) throws SQLException {

        MarkDAO dao = new MarkDAO();
        List<Mark> marks = dao.getALLMarks();
        for (Mark mark : marks) {
            System.out.println(mark);
        }
        System.out.println("Nokia mark get test");
        Mark mark = dao.getPhoneByMark("nokia");
        System.out.println(mark);

        System.out.println("Delete nokia");
        if (dao.deleteMarkFromData("nokia")){
            marks.clear();
            marks = dao.getALLMarks();
            for (Mark mark1 : marks) {
                System.out.println(mark1);
            }
        }
        System.out.println("Add nokia test");
        if(dao.addMark("nokia")){
            marks.clear();
            marks = dao.getALLMarks();
            for (Mark mark1 : marks) {
                System.out.println(mark1);
            }
        }

        System.out.println("change name nokia to nokia111");
        if(dao.changeMarkName("nokia", "nokia1")){
            marks.clear();
            marks = dao.getALLMarks();
            for (Mark mark1 : marks) {
                System.out.println(mark1);
            }
        }
    }
}
