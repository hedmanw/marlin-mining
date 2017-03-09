# Exclusive
Code taken from `373f3ec/Marlin_main.cpp`.

## Case I: Mutually exclusive code
This case is equivalent to `ChangePC: Case I`. It is the same code, with the same objective, but a different path there, composing intentions.
Expected outcome: Integrate Delta-specific changes from fork as features, and make non-delta-compatible code features.

**Integrated view**
```cpp
#if !defined(FORK)
  // Do not use feedmultiply for E or Z only moves
  if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
    plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
  }
#else
  float difference[NUM_AXIS];
  for (int8_t i=0; i < NUM_AXIS; i++) {
    difference[i] = destination[i] - current_position[i];
  }
#endif
```

**Mainline view:**
```cpp
float difference[NUM_AXIS];
for (int8_t i=0; i < NUM_AXIS; i++) {
  difference[i] = destination[i] - current_position[i];
}
```

**Clone view:**
```cpp
// Do not use feedmultiply for E or Z only moves
if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
  plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
}
```

### Resolution:
Apply `Keep` on both branches, followed by making each block mutually exclusive under the condition `!defined(DELTA)`.
Let `K` denote `Keep` and `Xn` denote `Exclusive`, with `n={1,2}` to denote block.

**Integrated view:**
```cpp
#if !defined(FORK)
K  // Do not use feedmultiply for E or Z only moves
K  if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
K    plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
K  }
#else
K  float difference[NUM_AXIS];
K  for (int8_t i=0; i < NUM_AXIS; i++) {
K    difference[i] = destination[i] - current_position[i];
K  }
#endif
```

**Intermediary view (after Keep is applied):**
```cpp
  // Do not use feedmultiply for E or Z only moves
  if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
    plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
  }
  float difference[NUM_AXIS];
  for (int8_t i=0; i < NUM_AXIS; i++) {
    difference[i] = destination[i] - current_position[i];
  }
```

**Integrated view (apply Exclusive):**
```cpp
X1  // Do not use feedmultiply for E or Z only moves
X1  if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
X1    plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
X1  }
X2  float difference[NUM_AXIS];
X2  for (int8_t i=0; i < NUM_AXIS; i++) {
X2    difference[i] = destination[i] - current_position[i];
X2  }
```

**Outcome:**
```cpp
#if !defined(DELTA)
  // Do not use feedmultiply for E or Z only moves
  if( (current_position[X_AXIS] == destination [X_AXIS]) && (current_position[Y_AXIS] == destination [Y_AXIS])) {
    plan_buffer_line(destination[X_AXIS], destination[Y_AXIS], destination[Z_AXIS], destination[E_AXIS], feedrate/60, active_extruder);
  }
#else
  float difference[NUM_AXIS];
  for (int8_t i=0; i < NUM_AXIS; i++) {
    difference[i] = destination[i] - current_position[i];
  }
#endif
```