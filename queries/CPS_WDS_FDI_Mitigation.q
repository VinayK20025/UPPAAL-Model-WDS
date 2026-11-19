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

// D1: FDI can corrupt a fresh sensor reading
E<> (fdi_active && sensor_fresh && sensor_level != tank_level)

// D2: FDI and IDS alarm can coexist
E<> (fdi_active && intrusion_detected)

// M1: Defensive isolation is reachable after an attack
E<> (attack_occurred && fdi_isolated && !fdi_active)

// M2: Mitigation completion is reachable
E<> (attack_occurred && mitigation_completed)

// R1: Trusted data can be restored after mitigation
E<> (attack_occurred && mitigation_completed && !fdi_active && data_valid)

// R2: IDS alarm can be cleared after mitigation
E<> (attack_occurred && mitigation_completed && !fdi_active && !intrusion_detected)

// R3: Normal trusted operation can be restored after mitigation
E<> (attack_occurred && mitigation_completed && fdi_isolated && !fdi_active && !intrusion_detected && data_valid && tank_level == NORMAL)