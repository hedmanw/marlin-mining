//Marlin_main.cpp
//Merging jcrocholl/Marlin b1071ac with MarlinFirmware/Marlin 5f55514

//MERGE EXCERPT LINES 314-335
<<<<<<< HEAD
#ifdef NONLINEAR_BED_LEVELING
float bed_level[ACCURATE_BED_LEVELING_POINTS][ACCURATE_BED_LEVELING_POINTS];
=======
#ifdef SCARA                              // Build size scaling
float axis_scaling[3]={1,1,1};  // Build size scaling, default to 1
#endif

bool cancel_heatup = false ;

#ifdef FILAMENT_SENSOR
  //Variables for Filament Sensor input
  float filament_width_nominal=DEFAULT_NOMINAL_FILAMENT_DIA;  //Set nominal filament width, can be changed with M404
  bool filament_sensor=false;  //M405 turns on filament_sensor control, M406 turns it off
  float filament_width_meas=DEFAULT_MEASURED_FILAMENT_DIA; //Stores the measured filament diameter
  signed char measurement_delay[MAX_MEASUREMENT_DELAY+1];  //ring buffer to delay measurement  store extruder factor after subtracting 100
  int delay_index1=0;  //index into ring buffer
  int delay_index2=-1;  //index into ring buffer - set to -1 on startup to indicate ring buffer needs to be initialized
  float delay_dist=0; //delay distance counter
  int meas_delay_cm = MEASUREMENT_DELAY_CM;  //distance delay setting
>>>>>>> 5f555140be4231fb3ffea8a407414e245cfc12ec
#endif

//RESULT EXCERPT LINES 314-333
#ifdef NONLINEAR_BED_LEVELING
float bed_level[ACCURATE_BED_LEVELING_POINTS][ACCURATE_BED_LEVELING_POINTS];
#endif
#ifdef SCARA                              // Build size scaling
float axis_scaling[3]={1,1,1};  // Build size scaling, default to 1
#endif

bool cancel_heatup = false ;

#ifdef FILAMENT_SENSOR
  //Variables for Filament Sensor input
  float filament_width_nominal=DEFAULT_NOMINAL_FILAMENT_DIA;  //Set nominal filament width, can be changed with M404
  bool filament_sensor=false;  //M405 turns on filament_sensor control, M406 turns it off
  float filament_width_meas=DEFAULT_MEASURED_FILAMENT_DIA; //Stores the measured filament diameter
  signed char measurement_delay[MAX_MEASUREMENT_DELAY+1];  //ring buffer to delay measurement  store extruder factor after subtracting 100
  int delay_index1=0;  //index into ring buffer
  int delay_index2=-1;  //index into ring buffer - set to -1 on startup to indicate ring buffer needs to be initialized
  float delay_dist=0; //delay distance counter
  int meas_delay_cm = MEASUREMENT_DELAY_CM;  //distance delay setting
#endif

