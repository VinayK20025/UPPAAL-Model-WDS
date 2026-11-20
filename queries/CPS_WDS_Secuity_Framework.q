// Q1: Safety: overflow is prevented by the physical interlock
A[] tank_level != OVERFLOW

// Q2: Safety: depletion is prevented by the physical interlock
A[] tank_level != DEPLETED

// Q3: Liveness: normal tank level is reachable
E<> tank_level == NORMAL

// Q4: Attack: an integrity attack can be launched
E<> attack_success

// Q5: Defence: rejected data cannot alter the protected reading
A[] (attack_blocked imply secure_sensor_level == trusted_sensor_level)

// Q6: Detection/response: an alarm is associated with a mitigation state
A[] (intrusion_detected imply response_active || recovery_active || system_degraded)

// Q7: Response: safe mode requests pump shutdown
A[] (response_active imply !pump_state || pump_cmd_off)

// Q8: Recovery: recovery qualification is reachable
E<> recovery_active

// Q9: Recovery: a normal operating state is reachable after qualification
E<> (!intrusion_detected && !response_active && !recovery_active)

// Q10: Actuation: conflicting commands are excluded
A[] !(pump_cmd_on && pump_cmd_off)

// Q11: Attack / execution: attacker reaches the injecting state
E<> attack_active

// Q12: Attack / integrity: manipulated sensor data differs from the trusted reference
E<> (attack_active && sensor_level != trusted_sensor_level)

// Q13: Defence / effectiveness: the gateway blocks manipulated data
E<> attack_blocked

// Q14: Defence / data handling: filtered data is marked valid
A[] (attack_blocked imply data_valid)

// Q15: Detection / reachability: an intrusion alarm can be raised
E<> intrusion_detected

// Q16: Detection / handover: every active alarm is accompanied by degraded/mitigation status
A[] (intrusion_detected imply system_degraded)

// Q17: Response / automaton: response controller reaches SafeMode
E<> response.SafeMode

// Q18: Response / actuation: pump-on command is inhibited during response
A[] (response_active imply !pump_cmd_on)

// Q19: Recovery / automaton: recovery monitor reaches its qualification state
E<> recovery.Qualifying

// Q20: Recovery / completion integrity: recovered state has cleared the intrusion alarm
A[] (recovery.Recovered imply !intrusion_detected)

// Q21: Plant / range: tank-level abstraction remains within its declared range
A[] (tank_level >= DEPLETED && tank_level <= OVERFLOW)

// Q22: Sensor / range: raw sensor value remains within its declared range
A[] (sensor_level >= DEPLETED && sensor_level <= OVERFLOW)

// Q23: Trusted sensing / range: trusted reference remains within its declared range
A[] (trusted_sensor_level >= DEPLETED && trusted_sensor_level <= OVERFLOW)

// Q24: Defence / range: protected sensor value remains within its declared range
A[] (secure_sensor_level >= DEPLETED && secure_sensor_level <= OVERFLOW)

// Q25: Plant / reachability: low tank state is reachable
E<> tank_level == LOW

// Q26: Plant / reachability: high tank state is reachable
E<> tank_level == HIGH

// Q27: Actuation / reachability: pump can enter the ON state
E<> pump_state

// Q30: Control / reachability: PLC can issue a pump-ON command
E<> pump_cmd_on

// Q31: Control / reachability: PLC or response can issue a pump-OFF command
E<> pump_cmd_off

// Q32: Global / progress: the composed timed automata are deadlock-free
A[] not deadlock
