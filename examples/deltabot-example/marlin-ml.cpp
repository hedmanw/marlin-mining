#include "Marlin.h"
#define VERSION_STRING  "1.0.0"

float current_position[NUM_AXIS] = { 0.0, 0.0, 0.0, 0.0 };
#ifdef BARICUDA
int ValvePressure=0;
int EtoPPressure=0;
#endif

static float destination[NUM_AXIS] = { 0.0, 0.0, 0.0, 0.0 };

void process_commands() {
  plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
}
