package com.SoftDevTimeSheet.dao;

import com.SoftDevTimeSheet.entity.Userdao;

import java.sql.*;

public class UserDAO {

    public Userdao getUserFromById(Long id){//get user by id
        Connection connection = null;
        PreparedStatement statement = null;
        ResultSet resultSet = null;
        Userdao user = null;

        try{
            connection = DAOConnectionFactory.getConnection();
            {
                try{
                    statement = connection.prepareStatement("SELECT * FROM users where id = (?)");
                    statement.setLong(1, id);
                    resultSet = statement.executeQuery();
                    resultSet.next();
                    user = new Userdao();
                    user.setId(resultSet.getLong("id"));
                    user.setName(resultSet.getString("name"));
                }catch (SQLException e){
                    System.out.println("failed1");
                }finally {
                    if(resultSet != null) {
                        resultSet.close();
                    }
                    if(statement != null) {
                        statement.close();
                    }
                }
            }
        }catch (SQLException e){
            System.out.println("failed2");
        }finally {
            try {
                if(connection != null) {
                    connection.close();
                }

            } catch (SQLException e) {
                e.printStackTrace();
            }
        }
        return user;
    }
}
