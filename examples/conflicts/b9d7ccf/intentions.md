# Case I
Base
```cpp
    destination[axis] = 2*home_retract_mm(axis) * home_dir(axis);
#ifdef DELTA
    feedrate = homing_feedrate[axis]/10;
#else
    feedrate = homing_feedrate[axis]/2 ;
#endif
```

Remote
```cpp
    destination[axis] = 2*home_retract_mm(axis) * axis_home_dir;
    feedrate = homing_feedrate[axis]/2 ;
```

Result
```cpp
    destination[axis] = 2*home_retract_mm(axis) * axis_home_dir;
#ifdef DELTA
    feedrate = homing_feedrate[axis]/10;
#else
    feedrate = homing_feedrate[axis]/2 ;
#endif
```

## Manual resolution
```
<BASE
-     destination[axis] = 2*home_retract_mm(axis) * home_dir(axis);
+ #ifdef DELTA
+     feedrate = homing_feedrate[axis]/10;
+ #else
=======
+    destination[axis] = 2*home_retract_mm(axis) * axis_home_dir; // Move this block up so that it precedes its predecessor
REMOTE>
    feedrate = homing_feedrate[axis]/2 ;
#endif

```

* 2 x Kept blocks
* 1 x Deleted blocks
* 1 x Moved blocks

## Intentions resolution
```cpp
#ifndef FORK
-    destination[axis] = 2*home_retract_mm(axis) * home_dir(axis);
#else
+    destination[axis] = 2*home_retract_mm(axis) * axis_home_dir;
#endif /* !defined(FORK) */
#if !defined(FORK) && defined(DELTA) // Change PC or keep node?
    feedrate = homing_feedrate[axis]/10;
#else
    feedrate = homing_feedrate[axis]/2 ;
#endif /* !defined(FORK) && defined(DELTA) */

```

* 1 x Keep block
* 1 x Remove block
* 1 x Change PC (or keep node instead)