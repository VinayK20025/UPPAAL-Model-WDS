// D1: overflow is never recorded during a control interlock.
A[] !overflow_during_interlock

// D2: a recovery-ready state is reachable after all represented attacks cease.
E<> (safe_mode && clean_count >= RECOVERY_THRESHOLD && !fdi_active && !replay_active && !dos_active)

// D3: recovery completion is reachable; this is existential, not inevitable.
E<> recovery_completed
