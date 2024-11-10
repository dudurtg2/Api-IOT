package com.iot.monitor.controllers;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.context.annotation.RequestScope;

import com.iot.monitor.entities.Monitor;
import com.iot.monitor.repositories.MonitorRepository;

@RestController
@RequestScope
@RequestMapping("/monitor")
public class MonitorController {

    private MonitorRepository monitorRepository;

    @Autowired
    public MonitorController(MonitorRepository monitorRepository) {
        this.monitorRepository = monitorRepository;
    }

    
    @GetMapping("/findAll")
    public ResponseEntity<List<Monitor>> findAll() {
        List<Monitor> monitor = monitorRepository.findAll();

        return new ResponseEntity<List<Monitor>>(monitor, HttpStatus.OK);
    }

    @PostMapping("/save")
    public ResponseEntity<Monitor> save(@RequestBody Monitor monitor) {
        Monitor monitors = monitorRepository.save(monitor);

        return new ResponseEntity<Monitor>(monitors, HttpStatus.CREATED);

    }

    @GetMapping("/findById/{id}")
    public ResponseEntity<Monitor> findById(@PathVariable int id) {
        Monitor monitor = monitorRepository.findById(id);

        return new ResponseEntity<Monitor>(monitor, HttpStatus.OK);
    }


}
