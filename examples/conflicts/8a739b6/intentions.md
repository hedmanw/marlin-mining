# Case I
Base
```cpp
int auto_bed_leveling_grid_points = AUTO_BED_LEVELING_GRID_POINTS;
#ifndef DELTA
  if (code_seen('P')) auto_bed_leveling_grid_points = code_value_long();
  if (auto_bed_leveling_grid_points < 2 || auto_bed_leveling_grid_points > AUTO_BED_LEVELING_GRID_POINTS) {
    SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
    return;
  }
#endif
```

Remote
```cpp
int auto_bed_leveling_grid_points = code_seen('P') ? code_value_long() : AUTO_BED_LEVELING_GRID_POINTS;
if (auto_bed_leveling_grid_points < 2) {
  SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
  return;
}

xy_travel_speed = code_seen('S') ? code_value_long() : XY_TRAVEL_SPEED;
```

Result
```cpp
int auto_bed_leveling_grid_points = AUTO_BED_LEVELING_GRID_POINTS;
#ifndef DELTA
  if (code_seen('P')) auto_bed_leveling_grid_points = code_value_long();
  if (auto_bed_leveling_grid_points < 2) {
    SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
    return;
  }
#endif

xy_travel_speed = code_seen('S') ? code_value_long() : XY_TRAVEL_SPEED;
```

## Manual resolution
```
<BASE
+ int auto_bed_leveling_grid_points = AUTO_BED_LEVELING_GRID_POINTS;
+ #ifndef DELTA
+   if (code_seen('P')) auto_bed_leveling_grid_points = code_value_long();
-   if (auto_bed_leveling_grid_points < 2 || auto_bed_leveling_grid_points > AUTO_BED_LEVELING_GRID_POINTS) {
+     SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
+     return;
+   }
+ #endif
=============
- int auto_bed_leveling_grid_points = code_seen('P') ? code_value_long() : AUTO_BED_LEVELING_GRID_POINTS;
+ if (auto_bed_leveling_grid_points < 2) {
-   SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
-   return;
- }
+
+ xy_travel_speed = code_seen('S') ? code_value_long() : XY_TRAVEL_SPEED;
REMOTE>
```

* 4 x Kept blocks
* 3 x Deleted blocks
* 1 x Moved blocks

## Intentions resolution
```cpp
#ifndef FORK
int auto_bed_leveling_grid_points = AUTO_BED_LEVELING_GRID_POINTS;
#ifndef DELTA
  if (code_seen('P')) auto_bed_leveling_grid_points = code_value_long();
  if (auto_bed_leveling_grid_points < 2 || auto_bed_leveling_grid_points > AUTO_BED_LEVELING_GRID_POINTS) {
    SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
    return;
  }
#endif /* !defined(DELTA) */
#else
int auto_bed_leveling_grid_points = code_seen('P') ? code_value_long() : AUTO_BED_LEVELING_GRID_POINTS;
if (auto_bed_leveling_grid_points < 2) {
  SERIAL_PROTOCOLPGM("?Number of probed (P)oints is implausible (2 minimum).\n");
  return;
}

xy_travel_speed = code_seen('S') ? code_value_long() : XY_TRAVEL_SPEED;
#endif /* !defined(FORK) */

```

Analogue to manual resolution.