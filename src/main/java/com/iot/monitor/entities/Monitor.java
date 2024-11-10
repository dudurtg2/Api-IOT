package com.iot.monitor.entities;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;

@Table(name = "monitor")
@Entity
public class Monitor {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;

    @Column(name = "temperature")
    private float temperature;

    @Column(name = "humidity")
    private float humidity;
   
    @Column(name = "solidHumidity")
    private float solidhumidity;

    @Column(name = "date")
    private String date;

    @Column(name = "lightStatus")
    private boolean lightStatus;

    @Column(name = "pampStatus")
    private boolean pampStatus;


    public Monitor() {
    }

    public Monitor(int id, float temperature, float humidity, float solidhumidity, String date, boolean lightStatus, boolean pampStatus) {
        this.id = id;
        this.temperature = temperature;
        this.humidity = humidity;
        this.solidhumidity = solidhumidity;
        this.date = date;
        this.lightStatus = lightStatus;
        this.pampStatus = pampStatus;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public float getTemperature() {
        return this.temperature;
    }

    public void setTemperature(float temperature) {
        this.temperature = temperature;
    }

    public float getHumidity() {
        return this.humidity;
    }

    public void setHumidity(float humidity) {
        this.humidity = humidity;
    }

    public float getSolidhumidity() {
        return this.solidhumidity;
    }

    public void setSolidhumidity(float solidhumidity) {
        this.solidhumidity = solidhumidity;
    }

    public String getDate() {
        return this.date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public boolean getLightStatus() {
        return this.lightStatus;
    }

    public void setLightStatus(boolean lightStatus) {
        this.lightStatus = lightStatus;
    }

    public boolean getPampStatus() {
        return this.pampStatus;
    }

    public void setPampStatus(boolean pampStatus) {
        this.pampStatus = pampStatus;
    }
 
    
}