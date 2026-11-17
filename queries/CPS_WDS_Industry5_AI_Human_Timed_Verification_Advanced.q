E<> (fdi_active && intrusion_detected)
E<> (replay_active && twin_error[0])
E<> (replay_active && twin_error[1])
E<> (dos_active && ai_alarm)
E<> (cmdinj_active && intrusion_detected)
E<> ((fdi_active || replay_active || dos_active || cmdinj_active) && ai_alarm)
E<> ((fdi_active || replay_active) && (twin_error[0] || twin_error[1]))
E<> ((fdi_active && dos_active) && ai_alarm)
E<> (tank_level[1]==OVERFLOW && backup_shutdown)
E<> (safe_mode && !pump_state[0] && !pump_state[1])
E<> (tank_level[0]==OVERFLOW && (safe_mode || backup_shutdown))
E<> (cmdinj_active && tank_level[0]==OVERFLOW)
E<> (safe_mode==false && !fdi_active && !replay_active && !dos_active && !cmdinj_active)
E<> safe_mode
E<> (safe_mode && clean_count>=1)
E<> (safe_mode==false && clean_count==0 && !intrusion_detected)
E<> ((fdi_active || replay_active || dos_active || cmdinj_active) && safe_mode)
E<> (ai_alarm && operator_ack)
E<> (intrusion_detected && operator_ack)
E<> (operator_ack && safe_mode)
E<> (operator_ack && backup_shutdown)
E<> (ai_alarm && operator_ack && safe_mode)
E<> (watchdog_miss>=WD_LIMIT && backup_shutdown)
E<> (backup_shutdown && !pump_state[0] && !pump_state[1])
E<> (safe_mode==false)
E<> pump_state[0]
E<> !pump_state[0]
safe_mode --> !safe_mode
ai_alarm --> operator_ack
