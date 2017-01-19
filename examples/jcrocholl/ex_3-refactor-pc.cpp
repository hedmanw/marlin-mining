//Marlin_main.cpp
//Merging jcrocholl/Marlin b1071ac with MarlinFirmware/Marlin 5f55514

//MERGE EXCERPT LINES 1205-1225
<<<<<<< HEAD
#ifdef SERVO_ENDSTOPS
  engage_z_probe();   // Engage Z Servo endstop if available
#endif //SERVO_ENDSTOPS

  run_z_probe();
  float measured_z = current_position[Z_AXIS];

#ifdef SERVO_ENDSTOPS
  retract_z_probe();
#endif //SERVO_ENDSTOPS
=======
#ifndef Z_PROBE_SLED
  engage_z_probe();   // Engage Z Servo endstop if available
#endif // Z_PROBE_SLED
  run_z_probe();
  float measured_z = current_position[Z_AXIS];
#ifndef Z_PROBE_SLED
  retract_z_probe();
#endif // Z_PROBE_SLED
>>>>>>> 5f555140be4231fb3ffea8a407414e245cfc12ec

//RESULT EXCERPT LINES 1203-1210
#ifndef Z_PROBE_SLED
  engage_z_probe();   // Engage Z Servo endstop if available
#endif // Z_PROBE_SLED
  run_z_probe();
  float measured_z = current_position[Z_AXIS];
#ifndef Z_PROBE_SLED
  retract_z_probe();
#endif // Z_PROBE_SLED

