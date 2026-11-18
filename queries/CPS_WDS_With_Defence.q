A[] safe_mode imply tank_level != OVERFLOW
E<> safe_mode
E<> alarm_integrity
// Q4: Recovery from safe mode is reachable
E<> (!safe_mode && clean_count == 0)

// Q5: Attack termination is reachable
E<> !fdi_active
// Q6: Recovery is reachable after an attack has been detected
E<> (attack_detected_once && recovery_completed && !safe_mode)
