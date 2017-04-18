#include "Marlin.h"
#ifndef FORK
#define VERSION_STRING "1.0.0"

#else
#define VERSION_STRING "0.9.0"

#endif /* !defined(FORK) */

float current_position[NUM_AXIS] = { 0.0, 0.0, 0.0, 0.0 };
#ifndef FORK
#ifdef BARICUDA
int ValvePressure=0;
int EtoPPressure=0;
#endif /* defined(BARICUDA) */
#endif /* !defined(FORK) */

static float destination[NUM_AXIS] = { 0.0, 0.0, 0.0, 0.0 };
#ifdef FORK
static float delta[3] = {0.0, 0.0, 0.0};
#endif /* defined(FORK) */

void process_commands() {
#ifndef FORK
plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
#else
calculate_delta(current_position);
plan_set_position(delta[X_AXIS], delta[Y_AXIS], delta[Z_AXIS], current_position[E_AXIS]);
#endif /* !defined(FORK) */
}
#ifdef FORK

void calculate_delta(float cartesian[3]) {
delta[X_AXIS] = sqrt(sq(DELTA_DIAGONAL_ROD)
- sq(DELTA_TOWER1_X-cartesian[X_AXIS])
- sq(DELTA_TOWER1_Y-cartesian[Y_AXIS])
) + cartesian[Z_AXIS];
delta[Y_AXIS] = sqrt(sq(DELTA_DIAGONAL_ROD)
- sq(DELTA_TOWER2_X-cartesian[X_AXIS])
- sq(DELTA_TOWER2_Y-cartesian[Y_AXIS])
) + cartesian[Z_AXIS];
delta[Z_AXIS] = sqrt(sq(DELTA_DIAGONAL_ROD)
- sq(DELTA_TOWER3_X-cartesian[X_AXIS])
- sq(DELTA_TOWER3_Y-cartesian[Y_AXIS])
) + cartesian[Z_AXIS];
}
#endif /* defined(FORK) */
