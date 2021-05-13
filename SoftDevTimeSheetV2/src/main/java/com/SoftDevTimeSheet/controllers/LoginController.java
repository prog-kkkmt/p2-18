package com.SoftDevTimeSheet.controllers;

import com.SoftDevTimeSheet.restService.AuthService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LoginController {

    @GetMapping("/login")
    public String greeting(@RequestParam(value = "name", defaultValue = "kostya") String name) {
        AuthService auth = new AuthService();
        return auth.auth(name).toString();

    }
}