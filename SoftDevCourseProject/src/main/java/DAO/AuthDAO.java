package DAO;

import java.sql.*;

public class AuthDAO implements IAuthDAO {

    final String user = "postgres";
    final String pass = "admin";
    final String url = "jdbc:postgresql://localhost:5432/softdev";

    @Override
    public String authorize(String workerName) {
        try(Connection connection = DriverManager.getConnection(url,user,pass)){
            try(PreparedStatement state = connection.prepareStatement("SELECT role FROM Workers WHERE name = (?)")){
                state.setString(1, workerName);
                ResultSet resultSet = state.executeQuery();
                resultSet.next();
                String workerRole = resultSet.getString("role");
                switch (workerRole){
                    case "freelancer":
                        return "freelancer";
                    case "state":
                        return "state";
                    case "director":
                        return "director";
                }
            }catch (SQLException e){
                System.out.println(e);
            }
        }catch (SQLException e){
            System.out.println(e);
        }
        return "failed";
    }
}
