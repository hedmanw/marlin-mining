//Marlin.h
//Merging jcrocholl/Marlin b1071ac with MarlinFirmware/Marlin 5f55514

//MERGE EXCERPT LINES 182-189
<<<<<<< HEAD
void prepare_move_raw();
=======
#ifdef SCARA
void calculate_delta(float cartesian[3]);
void calculate_SCARA_forward_Transform(float f_scara[3]);
#endif
>>>>>>> 5f555140be4231fb3ffea8a407414e245cfc12ec

//RESULT EXCERPT LINES 182-186
void prepare_move_raw();
#ifdef SCARA
void calculate_delta(float cartesian[3]);
void calculate_SCARA_forward_Transform(float f_scara[3]);
#endif

