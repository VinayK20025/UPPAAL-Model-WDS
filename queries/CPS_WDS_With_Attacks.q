E<> tank.Overflow
E<> intrusion_detected
A[] !(pump_cmd_on && pump_cmd_off)
A[] not tank.Overflow
A[] sensor_level == tank_level
