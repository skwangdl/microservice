package com.alibaba.dubbo.demo.api;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class MainProvider {
    public static void main(String[] args) throws Exception {
        SpringApplication.run(MainProvider.class,args);
    }
}
