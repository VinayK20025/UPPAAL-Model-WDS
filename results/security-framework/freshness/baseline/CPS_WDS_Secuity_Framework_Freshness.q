// Q1: Tank overflow is unreachable
A[] not tank.Overflow

// Q2: Tank depletion is unreachable
A[] not tank.Depleted

// Q3: Normal operation is reachable
E<> tank.Normal

// Q4: Uncorrupted fresh sensor readings are consistent
A[] (sensor_fresh && !fdi_active imply sensor_level == tank_level)

// Q5: Valid delivered measurements are fresh and consistent
A[] (data_valid imply (measurement_fresh && secure_sensor_level == tank_level && !fdi_active))

// Q6: Pump commands are mutually exclusive
A[] !(pump_cmd_on && pump_cmd_off)

// Q7: FDI intrusion detection is reachable
E<> intrusion_detected

// D1: FDI can successfully corrupt a fresh sensor reading
E<> (fdi_active && sensor_fresh && sensor_level != tank_level)

// D2: An active FDI attack can coexist with an IDS alarm
E<> (fdi_active && intrusion_detected)

// R1: An attack episode can terminate
E<> (attack_occurred && !fdi_active)

// R2: Trusted data can be restored after an attack
E<> (attack_occurred && !fdi_active && data_valid)

// R3: The IDS alarm can be cleared after an attack
E<> (attack_occurred && !fdi_active && !intrusion_detected)

// R4: Normal operation can be restored after an attack
E<> (attack_occurred && !fdi_active && !intrusion_detected && data_valid && tank_level == NORMAL)