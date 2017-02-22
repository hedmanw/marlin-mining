# Case I
_NOTE THAT THIS IS AN ALTERED SCENARIO._
Here we pretend that the Delta functionality is implemented without regards for featurization.
Because of this, the integration requires mutually exclusion for Delta and regular.

Base
```cpp
calculate_delta(current_position);
plan_set_position(delta[X_AXIS], delta[Y_AXIS], delta[Z_AXIS], current_position[E_AXIS]);
```

Remote
```cpp
plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
```

Result
```cpp
#ifdef DELTA
  calculate_delta(current_position);
  plan_set_position(delta[X_AXIS], delta[Y_AXIS], delta[Z_AXIS], current_position[E_AXIS]);
#else
  plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
#endif
```

## Manual resolution
```
#ifdef DELTA
<BASE
+  calculate_delta(current_position);
+  plan_set_position(delta[X_AXIS], delta[Y_AXIS], delta[Z_AXIS], current_position[E_AXIS]);
=======
#else
+  plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
REMOTE>
#endif
```

* 2 x Kept blocks
* 0 x Deleted blocks
* 0 x Moved blocks
* 3 x Manual ifdef-statements (i.e. one complete ifdef-else-endif)

## Intentions resolution
```cpp
// Notation: x := Exclusive intention on block

#ifndef FORK // PC changed to DELTA in Exclusive intention application 
x  calculate_delta(current_position);
x  plan_set_position(delta[X_AXIS], delta[Y_AXIS], delta[Z_AXIS], current_position[E_AXIS]);
#else
x  plan_set_position(current_position[X_AXIS], current_position[Y_AXIS], current_position[Z_AXIS], current_position[E_AXIS]);
#endif /* !defined(FORK) */
```

* 1 x Exclusive blocks (with two sub-blocks)
