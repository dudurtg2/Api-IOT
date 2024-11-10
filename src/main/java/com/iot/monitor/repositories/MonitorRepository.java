package com.iot.monitor.repositories;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import com.iot.monitor.entities.Monitor;
@Repository
public interface MonitorRepository extends JpaRepository<Monitor, Integer> {
    Monitor findById(int id);
}
