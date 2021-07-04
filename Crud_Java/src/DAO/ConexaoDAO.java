package DAO;


import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author Jefferson Tavares
 */
public class ConexaoDAO {
    
    public Connection conectaBD(){
        Connection conn = null;
        
        try {
           String url = "jdbc:mysql://localhost:3306/agenda?user=root&password="; 
           conn = DriverManager.getConnection(url);
        } catch (SQLException e) {
            JOptionPane.showMessageDialog(null,"ConexaoDAO" + e.getMessage());
        }
        return conn;
    }
    
}
