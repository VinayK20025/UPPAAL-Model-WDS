# Query register: advanced 16-process model

**Source:** `CPS_WDS_Industry5_AI_Human_Timed_Verification_Advanced.xml`

**Embedded query count:** 30. **Numbering:** Q1–Q8 and Q10–Q31. Q9 is absent. “Stored outcome” below means only that an XML result annotation exists. “Not recorded” does not mean success or failure.

| ID | Formula | Stored outcome | XML comment |
|---|---|---|---|
| Q1 | `E<> (fdi_active && intrusion_detected)` | success | FDI attack produces a detectable IDS signal |
| Q2 | `E<> (replay_active && twin_error[0])` | success | Replay attack causes observable twin inconsistency (tank 0) |
| Q3 | `E<> (replay_active && twin_error[1])` | success | Replay attack causes observable twin inconsistency (tank 1) |
| Q4 | `E<> (dos_active && ai_alarm)` | success | DoS-induced communication disruption triggers AI alarm |
| Q5 | `E<> (cmdinj_active && intrusion_detected)` | success | Command injection is detectable |
| Q6 | `E<> ((fdi_active || replay_active || dos_active || cmdinj_active) && ai_alarm)` | success | Detection pipeline reachable under an attack vector (as stated in XML) |
| Q7 | `E<> ((fdi_active || replay_active) && (twin_error[0] || twin_error[1]))` | success | Twin consistency check identifies integrity violations |
| Q8 | `E<> ((fdi_active && dos_active) && ai_alarm)` | success | Hybrid FDI+DoS attack is detectable |
| Q9 | **Absent** | — | No Q9 entry |
| Q10 | `E<> (tank_level[1]==OVERFLOW && backup_shutdown)` | not recorded | Backup shutdown under critical overflow on tank 1 |
| Q11 | `E<> (safe_mode && !pump_state[0] && !pump_state[1])` | not recorded | Safe mode halts all pump actuation |
| Q12 | `E<> (tank_level[0]==OVERFLOW && (safe_mode || backup_shutdown))` | not recorded | Overflow and mitigation can coexist |
| Q13 | `E<> (cmdinj_active && tank_level[0]==OVERFLOW)` | not recorded | Command injection can drive tank 0 to overflow |
| Q14 | `E<> (safe_mode==false && !fdi_active && !replay_active && !dos_active && !cmdinj_active)` | not recorded | Clean recovery state reachable once attacks cease |
| Q15 | `E<> safe_mode` | not recorded | Safe mode reachable |
| Q16 | `E<> (safe_mode && clean_count>=1)` | not recorded | Recovery reaches stabilisation phase |
| Q17 | `E<> (safe_mode==false && clean_count==0 && !intrusion_detected)` | not recorded | Full clean recovery state reachable |
| Q18 | `E<> ((fdi_active || replay_active || dos_active || cmdinj_active) && safe_mode)` | not recorded | Attack and safe mode jointly reachable |
| Q19 | `E<> (ai_alarm && operator_ack)` | not recorded | AI alarm and operator acknowledgement jointly reachable |
| Q20 | `E<> (intrusion_detected && operator_ack)` | not recorded | Detection signal reaches operator |
| Q21 | `E<> (operator_ack && safe_mode)` | not recorded | Operator acknowledgement and safe mode jointly reachable |
| Q22 | `E<> (operator_ack && backup_shutdown)` | not recorded | Operator acknowledgement and backup shutdown jointly reachable |
| Q23 | `E<> (ai_alarm && operator_ack && safe_mode)` | not recorded | AI alarm, human acknowledgement and safe mode jointly reachable |
| Q24 | `E<> (watchdog_miss>=WD_LIMIT && backup_shutdown)` | not recorded | Watchdog escalation reachable |
| Q25 | `E<> (backup_shutdown && !pump_state[0] && !pump_state[1])` | not recorded | Backup shutdown and pumps off jointly reachable |
| Q26 | `A[] not deadlock` | not recorded | Deadlock freedom |
| Q27 | `E<> (safe_mode==false)` | success | Safe-mode exit reachable |
| Q28 | `E<> pump_state[0]` | success | Pump 0 can be ON |
| Q29 | `E<> !pump_state[0]` | success | Pump 0 can be OFF |
| Q30 | `safe_mode --> !safe_mode` | not recorded | Safe-mode entry is eventually followed by exit, per XML comment |
| Q31 | `ai_alarm --> operator_ack` | failure | Every AI alarm is eventually acknowledged, per XML comment |

## Query classes

- Q1–Q25 and Q27–Q29 use existential reachability. These formulas establish possibility/witness states, not universal security guarantees.
- Q26 is a universal deadlock-freedom invariant.
- Q30 and Q31 are leads-to/liveness properties.
- Q9 is absent and must not be invented or counted without an authoritative source.

## Reporting caution

Do not infer an outcome from a query comment, timestamp, number or manuscript narrative. Rerun each formula and retain the actual tool output. In particular, Q31 is marked “failure” in the current XML while the manuscript reports it as established; Q30 has no embedded result annotation.
