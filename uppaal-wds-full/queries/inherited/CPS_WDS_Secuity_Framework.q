A[] not tank.Overflow
A[] not tank.Depleted
E<> tank.Normal
A[] sensor_level == tank_level
A[] (not intrusion_detected imply secure_sensor_level == tank_level)
A[] !(pump_cmd_on && pump_cmd_off)
E<> intrusion_detected
