// ============================================================
// 30 PROPERTY QUERIES — AI–IoT–INDUSTRY 5.0–HUMAN-IN-THE-LOOP WDS
// Queries are grouped by verification category.
// Run against: CPS_WDS_Security_AI_Industry5IoT_Human.xml
// ============================================================

// CATEGORY 1 — PHYSICAL PROCESS AND TANK SAFETY (Q01–Q05)
A[] not tank.Overflow
A[] not tank.Depleted
E<> tank.Normal
A[] !(pump_cmd_on && pump_cmd_off)
A[] (safe_mode imply !pump_state)

// CATEGORY 2 — SENSOR, IoT CONNECTIVITY AND DATA VALIDITY (Q06–Q10)
// The current model has no transition that drops iot_connected.
A[] iot_network.Connected
A[] (!iot_connected imply !data_valid)
A[] (iot_sensor_fault imply !data_valid)
E<> (trusted_sensor_level == tank_level)
A[] (iot_packet_valid imply iot_connected)

// CATEGORY 3 — CYBERATTACK, INTRUSION AND DEFENCE (Q11–Q15)
E<> attack_success
E<> intrusion_detected
A[] (intrusion_detected imply system_degraded)
A[] (attack_active imply !recovery_complete)
// Attack injection precedes IDS detection; once detected, the system is degraded.
A[] (intrusion_detected imply system_degraded)

// CATEGORY 4 — AI ANALYTICS AND DECISION SUPPORT (Q16–Q19)
E<> ai_alert
E<> (ai_risk == RISK_HIGH)
A[] (ai_risk == RISK_HIGH imply ai_alert)
E<> ai_recommendation_ready

// CATEGORY 5 — HUMAN-IN-THE-LOOP (Q20–Q24)
E<> human_alert_received
E<> human_acknowledged
E<> human_approved
E<> human_rejected
E<> human_override

// CATEGORY 6 — RESPONSE, RECOVERY AND GLOBAL TIMED-AUTOMATA PROPERTIES (Q25–Q30)
E<> response.SafeMode
A[] (response_active imply safe_mode)
A[] (safe_mode imply (!pump_cmd_on && !pump_state))
E<> recovery.Qualifying
E<> recovery.Recovered
A[] not deadlock
