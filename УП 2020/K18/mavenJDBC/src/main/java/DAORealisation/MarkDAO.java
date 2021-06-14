package DAORealisation;


import DAOInterfaces.PhonesReadDAO;
import logicClasses.Mark;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;


public class MarkDAO implements PhonesReadDAO {

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/phoneshop";

    @Override
    public List<Mark> getALLMarks() {
        List<Mark> list = new ArrayList<>(10);
        try (Connection connection = DriverManager.getConnection(url, user, pass)) {//create connection
            try (PreparedStatement statement = connection.prepareStatement("SELECT * from Phone")) {//create Statement
                final ResultSet resultSet = statement.executeQuery();
                while (resultSet.next()) {
                    Mark tmpMark = new Mark();
                    tmpMark.setMarkName(resultSet.getString("Mark"));
                    tmpMark.setId(resultSet.getInt("Id"));
                    list.add(tmpMark);
                }
            }catch (SQLException e){
                e.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        if (list.isEmpty()) {
            Mark tmpMark = new Mark();
            tmpMark.setId(-1);
            tmpMark.setMarkName("default");
            list.add(tmpMark);
        }
        return list;
    }


    @Override
    public Mark getPhoneByMark(String phoneMarkName) {
        Mark tmpMark = new Mark();
        try (Connection connection = DriverManager.getConnection(url, user, pass)) {//create connection
            try (PreparedStatement statement = connection.prepareStatement("SELECT * from Phone WHERE Mark = (?)" )) {//create Statement
                statement.setString(1,phoneMarkName);
                final ResultSet resultSet = statement.executeQuery();
                resultSet.next();
                tmpMark.setMarkName(resultSet.getString("Mark"));
                tmpMark.setId(resultSet.getInt("Id"));
            }catch (SQLException e){
                e.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }

        return tmpMark;
    }

    @Override
    public boolean deleteMarkFromData(String PhoneMarkName) {
        try (Connection connection = DriverManager.getConnection(url, user, pass)) {//create connection
            try (PreparedStatement statement = connection.prepareStatement("DELETE FROM Phone WHERE Mark = (?)" )) {//create Statement
                statement.setString(1, PhoneMarkName);
                statement.executeUpdate();
                return true;
            }catch (SQLException e){
                e.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    @Override
    public boolean changeMarkName(String prevName, String nextName) {
        try (Connection connection = DriverManager.getConnection(url, user, pass)) {//create connection
            try (PreparedStatement statement = connection.prepareStatement("UPDATE Phone SET Mark = (?) WHERE Mark = (?)" )) {//create Statement
                statement.setString(1, nextName);
                statement.setString(2, prevName);
                statement.executeUpdate();
                return true;
            }catch (SQLException e){
                e.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }

    public boolean addMark(String markName){
        try (Connection connection = DriverManager.getConnection(url, user, pass)) {//create connection
            try (PreparedStatement statement = connection.prepareStatement("INSERT INTO Phone (Mark) VALUES (?)" )) {//create Statement
                statement.setString(1, markName);
                statement.executeUpdate();
                return true;
            }catch (SQLException e){
                e.printStackTrace();
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
        return false;
    }
}
