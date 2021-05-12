package com.SoftDevTimeSheet.dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DAOConnectionFactory {


    public static Connection getConnection() throws SQLException {//connector creater
        final String userLogin = "postgres";
        final String pass = "admin";
        final String url = "jdbc:postgresql://localhost:5432/practice";
        return DriverManager.getConnection(url,userLogin,pass);

    }
}
