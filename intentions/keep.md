# Keep
Code taken from `temperature_47c1ea7_integrated.cpp`.

See also `Remove`.

## Case I: Explicit keep
Expected outcome: accept change as evolution.

**Integrated view:**
```cpp
#include "watchdog.h"
#if !defined(FORK)
  #include "language.h"
#endif
#include "Sd2PinMap.h"
```

**Mainline view:**
```cpp
#include "watchdog.h"
#include "language.h"
#include "Sd2PinMap.h"
```

**Clone view:**
```cpp
#include "watchdog.h"
#include "Sd2PinMap.h"
```

### Resolutions:
In order to achieve the expected outcome of integrating this change as evolution, there are two possible actions, both involving `Keep`, but applied on two different views.
Let `K` denote that the `Keep` intention is applied to the node. Only one of a) and b) below are required, but they are equal.

**a) Keep on Integrated view**
```cpp
#include "watchdog.h"
#if !defined(FORK)
K  #include "language.h"
#endif
#include "Sd2PinMap.h"
```

**b) Keep on Mainline view**
```cpp
#include "watchdog.h"
K#include "language.h"
#include "Sd2PinMap.h"
```

**Outcome:**
```cpp
#include "watchdog.h"
#include "language.h"
#include "Sd2PinMap.h"
```

## Case II: Implicit keep
Expected outcome: Discard the changes from the fork, accept the changes in the mainline as evolution.

**Integrated view:**
```cpp
#if !defined(FORK)
  int cycles = 0;
#else
  int cycles=0;
#endif
```

**Mainline view:**
```cpp
int cycles = 0;
```

**Clone view:**
```cpp
int cycles=0;
```

### Resolutions:
Note that the actual applied intention is `Remove`, denoted by `R`.
The `K` is added by the tool after prompting the user.
This is triggered because all the children of the if/else-block has a `Remove` intention applied - therefore the user is asked whether they want to automatically apply `Keep` to all children of the sibling if/else-block.

To reach the expected outcome, we can apply the `Remove` intention in either the integrated view or the clone view. For view clarity, we only show the integrated view here, but the same principle as above still stands.

**Integrated view:**
```cpp
#if !defined(FORK)
K  int cycles = 0; // All nodes in this block get Keep because we apply the remove intention below!
#else
R  int cycles=0; // Apply Remove to all nodes in this block - prompt user for Keep on all nodes in if-block.
#endif
```

**Outcome:**
```cpp
int cycles = 0;
```