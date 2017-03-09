# Keep as feature
Code taken from `373f3ec/Marlin_main.cpp`.

Expected outcome: Integrate Delta-specific changes from fork as features.

**Integrated view**
```cpp
static float destination[NUM_AXIS] = {  0.0, 0.0, 0.0, 0.0};
#if defined(FORK)
  static float delta[3] = {0.0, 0.0, 0.0};
#endif
static float offset[3] = {0.0, 0.0, 0.0};
```

**Mainline view:**
```cpp
static float destination[NUM_AXIS] = {  0.0, 0.0, 0.0, 0.0};
static float offset[3] = {0.0, 0.0, 0.0};
```

**Clone view:**
```cpp
static float destination[NUM_AXIS] = {  0.0, 0.0, 0.0, 0.0};
static float delta[3] = {0.0, 0.0, 0.0};
static float offset[3] = {0.0, 0.0, 0.0};
```

### Resolution:
In order to achieve the expected outcome of integrating this change as a feature, there are two possible actions, both involving `KeepAsFeature`, but applied on two different views.
Below we will show the Clone view only, but the exact same principle applies for the Integrated view also. Let `F` denote that the `KeepAsFeature` intention is applied to the node.
The presence condition used for the applied intention is `defined(DELTA)`.

**KeepAsFeature on Clone view**
```cpp
static float destination[NUM_AXIS] = {  0.0, 0.0, 0.0, 0.0};
F static float delta[3] = {0.0, 0.0, 0.0}; // PC: defined(DELTA)
static float offset[3] = {0.0, 0.0, 0.0};
```

**Outcome:**
```cpp
static float destination[NUM_AXIS] = {  0.0, 0.0, 0.0, 0.0};
#if defined(DELTA)
  static float delta[3] = {0.0, 0.0, 0.0};
#endif
static float offset[3] = {0.0, 0.0, 0.0};
```