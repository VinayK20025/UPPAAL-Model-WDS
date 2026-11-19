// Universal sensor integrity
A[] sensor_level == tank_level

// Pump command mutual exclusion
A[] not (pump_cmd_on && pump_cmd_off)

// Pump deactivation is reachable
E<> !pump_state
