# Remove
Code taken from `temperature_47c1ea7_integrated.cpp`.

See also `Keep`.

## Case I: Explicit remove
Expected outcome: Discard the variable `ms`, as it is no longer required.

**Integrated view:**
```cpp
#if !defined(FORK)
  unsigned long ms = millis();
#endif
if (temp_meas_ready == true) {
  // stuff
}
```

**Mainline view:**
```cpp
unsigned long ms = millis();
if (temp_meas_ready == true) {
  // stuff
}
```

**Clone view:**
```cpp
if (temp_meas_ready == true) {
  // stuff
}
```

### Resolutions:
In order to achieve the expected outcome of integrating this change as evolution, there are two possible actions, both involving `Remove`, but applied on two different views.
Let `R` denote that the `Remove` intention is applied to the node. Only one of a) and b) below are required, but they are equal.

**a) Remove on Integrated view**
```cpp
#if !defined(FORK)
R  unsigned long ms = millis();
#endif
if (temp_meas_ready == true) {
  // stuff
}
```

**b) Remove on Mainline view**
```cpp
R unsigned long ms = millis();
if (temp_meas_ready == true) {
  // stuff
}
```

**Outcome:**
```cpp
if (temp_meas_ready == true) {
  // stuff
}
```

## Case II: Implicit remove
Expected outcome: Discard the changes from the fork, accept the changes in the mainline as evolution.

**Integrated view:**
```cpp
#if !defined(FORK)
  SERIAL_ECHOLN(MSG_PID_AUTOTUNE_START);
#else
  SERIAL_ECHOLN("PID Autotune start");
#endif
```

**Mainline view:**
```cpp
SERIAL_ECHOLN(MSG_PID_AUTOTUNE_START);
```

**Clone view:**
```cpp
SERIAL_ECHOLN("PID Autotune start");
```

### Resolutions:
Note that the actual applied intention is `Keep`, denoted by `K`.
The `R` is added by the tool after prompting the user.
This is triggered because all the children of the if/else-block has a `Keep` intention applied - therefore the user is asked whether they want to automatically apply `Remove` to all children of the sibling if/else-block.

To reach the expected outcome, we can apply the `Keep` intention in either the integrated view or the clone view. For view clarity, we only show the integrated view here, but the same principle as above still stands.

**Integrated view:**
```cpp
#if !defined(FORK)
K  SERIAL_ECHOLN(MSG_PID_AUTOTUNE_START);
#else
R  SERIAL_ECHOLN("PID Autotune start");
#endif
```

**Outcome:**
```cpp
SERIAL_ECHOLN(MSG_PID_AUTOTUNE_START);
```