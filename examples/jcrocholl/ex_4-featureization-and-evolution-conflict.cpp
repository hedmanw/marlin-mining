//Marlin_main.cpp
//Merging jcrocholl/Marlin b1071ac with MarlinFirmware/Marlin 5f55514

//MERGE EXCERPT LINES 1313-1332
#ifndef Z_PROBE_SLED
    // Engage Servo endstop if enabled
    #ifdef SERVO_ENDSTOPS
      #if defined (ENABLE_AUTO_BED_LEVELING) && (PROBE_SERVO_DEACTIVATION_DELAY > 0)
        if (axis==Z_AXIS) {
          engage_z_probe();
        }
            else
      #endif
      if (servo_endstops[axis] > -1) {
        servos[servo_endstops[axis]].write(servo_endstop_angles[axis * 2]);
      }
    #endif
<<<<<<< HEAD

    current_position[axis] = 0;
    plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
=======
#endif // Z_PROBE_SLED
>>>>>>> 5f555140be4231fb3ffea8a407414e245cfc12ec

//RESULT EXCERPT LINES 1298-1314
#ifndef Z_PROBE_SLED
    // Engage Servo endstop if enabled
    #ifdef SERVO_ENDSTOPS
      #if defined (ENABLE_AUTO_BED_LEVELING) && (PROBE_SERVO_DEACTIVATION_DELAY > 0)
        if (axis==Z_AXIS) {
          engage_z_probe();
        }
	    else
      #endif
      if (servo_endstops[axis] > -1) {
        servos[servo_endstops[axis]].write(servo_endstop_angles[axis * 2]);
      }
    #endif
#endif // Z_PROBE_SLED

    current_position[axis] = 0;
    plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);

