# Change PC
Code taken from `373f3ec/Marlin_main.cpp`.

## Case I: Mutex changes to feature
Expected outcome: Integrate Delta-specific changes from fork as features, and make non-delta-compatible code features.
This is facilitated by the fact that PPMerge has already turned these blocks into mutually exclusive on the pc `!defined(FORK)`.
In order to make them mutually exclusive under the feature `DELTA`, we simply need to change the presence condition.

See also the equivalent case `Exclusive: Case I`.

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
We apply `ChangePC` denoted by `C` on the Integrated view.
The presence condition used for the applied intention `C` is `!defined(DELTA)`.
It could be useful with an intention that swaps the order of the if and else block and inverts the condition.

**ChangePC on Integrated view**
```cpp
C #if !defined(FORK) // Change to !defined(DELTA)
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

## Case II: PC evolution
Code taken from a slightly altered version of XXXXX.

The presence conditions have been changed between the mainline and the fork. Expected outcome: accept the fork PC as evolution.

**Integrated view**
```cpp
#if (defined(FORK) || (PS_ON_PIN > -1)) && (!defined(FORK) || (defined(PS_ON_PIN) && PS_ON_PIN > -1))
  case 80: // M80 - Turn on Power Supply
  SET_OUTPUT(PS_ON_PIN); //GND
  WRITE(PS_ON_PIN, PS_ON_AWAKE);
#endif
```

**Mainline view:**
```cpp
#if PS_ON_PIN > -1
  case 80: // M80 - Turn on Power Supply
  SET_OUTPUT(PS_ON_PIN); //GND
  WRITE(PS_ON_PIN, PS_ON_AWAKE);
#endif
```

**Clone view:**
```cpp
#if defined(PS_ON_PIN) && PS_ON_PIN > -1
  case 80: // M80 - Turn on Power Supply
  SET_OUTPUT(PS_ON_PIN); //GND
  WRITE(PS_ON_PIN, PS_ON_AWAKE);
#endif
```

### Resolution:
In order to keep the PC from the clone, we need to apply `ChangePC`, denoted by `C`, with the new presence condition `defined(PS_ON_PIN) && PS_ON_PIN > -1`.

**ChangePC on Integrated view:**
```cpp
C #if (defined(FORK) || (PS_ON_PIN > -1)) && (!defined(FORK) || (defined(PS_ON_PIN) && PS_ON_PIN > -1))
  case 80: // M80 - Turn on Power Supply
  SET_OUTPUT(PS_ON_PIN); //GND
  WRITE(PS_ON_PIN, PS_ON_AWAKE);
#endif
```

**Outcome:**
```cpp
#if defined(PS_ON_PIN) && PS_ON_PIN > -1
  case 80: // M80 - Turn on Power Supply
  SET_OUTPUT(PS_ON_PIN); //GND
  WRITE(PS_ON_PIN, PS_ON_AWAKE);
#endif
```
