package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.dao.UserDAO;
import com.SoftDevTimeSheet.entity.Userdao;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {

    @GetMapping("/getuser")
    public Userdao greeting(@RequestParam(value = "id", defaultValue = "0") Long id) {
        UserDAO dao = new UserDAO();
        Userdao userdao = dao.getUserFromById(id);
        if (userdao.getName() != null && userdao.getId() != null){
            return userdao;
        }else{
            userdao.setName("default");
            userdao.setId(0l);
            return userdao;
        }
    }
}