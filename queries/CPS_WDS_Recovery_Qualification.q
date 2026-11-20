// Q1: Tank overflow is unreachable.
A[] not tank.Overflow

// Q2: Tank depletion is unreachable.
A[] not tank.Depleted

// Q3: Normal operation is reachable.
E<> tank.Normal

// Q4: A fresh, uncorrupted sensor sample agrees with the physical state.
A[] (sensor_fresh && !fdi_active imply sensor_level == tank_level)

// Q5: Data is marked valid only for a fresh, matching, attack-free measurement.
A[] (data_valid imply (measurement_fresh && secure_sensor_level == tank_level && !fdi_active))

// Q6: Actuator commands are mutually exclusive.
A[] !(pump_cmd_on && pump_cmd_off)

// Q7: IDS detection is reachable.
E<> intrusion_detected

// D1: FDI can corrupt a current fresh sample.
E<> (fdi_active && sensor_fresh && sensor_level != tank_level)

// D2: FDI and IDS alarm can coexist.
E<> (fdi_active && intrusion_detected)

// R1: The attack episode can terminate.
E<> (attack_occurred && !fdi_active)

// R2: Trusted data can be restored after the attack.
E<> (attack_occurred && !fdi_active && data_valid)

// R3: The IDS alarm can clear after an attack.
E<> (attack_occurred && !fdi_active && !intrusion_detected)

// R4: Normal operation can be reached after attack termination and data restoration.
E<> (attack_occurred && !fdi_active && !intrusion_detected && data_valid && tank_level == NORMAL)

// CI1: Defensive control inhibition is reachable.
E<> control_inhibit

// CI2: The plant can be running while inhibition is active (diagnostic; expected false after interlock).
E<> (control_inhibit && pump_state)

// CI3: A pending pump-on command can coexist with inhibition (diagnostic; expected false after interlock).
E<> (control_inhibit && pump_cmd_on)

// CI4: The pump is never running while inhibition is active.
A[] (control_inhibit imply !pump_state)

// CI5: No pump-on command remains pending while inhibition is active.
A[] (control_inhibit imply !pump_cmd_on)

// REC1: A clean-sample count of one is reachable during inhibition.
E<> (control_inhibit && clean_count == 1)

// REC2: A clean-sample count of two is reachable during inhibition.
E<> (control_inhibit && clean_count == 2)

// REC3: Three consecutive clean samples can complete recovery and clear inhibition.
E<> (attack_occurred && recovery_completed && clean_count == RECOVERY_THRESHOLD && !control_inhibit)

// REC4: Recovery cannot complete before the required clean-sample threshold.
A[] (recovery_completed imply clean_count == RECOVERY_THRESHOLD)

// REC5: An unclean measurement resets the recovery counter.
A[] (!recovery_sample_clean && clean_count > 0 imply clean_count == 0)
