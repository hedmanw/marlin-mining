# Case I
Base
```cpp
#if (PS_ON_PIN > -1)
  case 80: // M80 - Turn on Power Supply
    SET_OUTPUT(PS_ON_PIN); //GND
    WRITE(PS_ON_PIN, PS_ON_AWAKE);
  break;
#endif
```
Remote
```cpp
#if defined(PS_ON_PIN) && PS_ON_PIN > -1
  case 80: // M80 - ATX Power On
    SET_OUTPUT(PS_ON_PIN); //GND
    WRITE(PS_ON_PIN, PS_ON_AWAKE);
  break;
#endif
```
Result
```cpp
#if defined(PS_ON_PIN) && PS_ON_PIN > -1
  case 80: // M80 - Turn on Power Supply
    SET_OUTPUT(PS_ON_PIN); //GND
    WRITE(PS_ON_PIN, PS_ON_AWAKE);
  break;
#endif
```
## Manual resolution
```
<BASE
- #if (PS_ON_PIN > -1)
+  case 80: // M80 - Turn on Power Supply
=============
+ #if defined(PS_ON_PIN) && PS_ON_PIN > -1 // Move this block up so that it precedes its predecessor
-  case 80: // M80 - ATX Power On
REMOTE>
    SET_OUTPUT(PS_ON_PIN); //GND
    WRITE(PS_ON_PIN, PS_ON_AWAKE);
  break;
#endif
```

* 2 x Kept blocks
* 2 x Deleted blocks
* 1 x Moved blocks

## Intentions resolution
```cpp
// Keep&remove if-statement in mainline/clone views respectively
#if (defined(FORK) || (PS_ON_PIN > -1)) && (!defined(FORK) || defined(PS_ON_PIN) && PS_ON_PIN > -1)
#ifndef FORK
+  case 80: // M80 - Turn on Power Supply
#else
-  case 80: // M80 - ATX Power On
#endif /* !defined(FORK) */
    SET_OUTPUT(PS_ON_PIN); //GND
    WRITE(PS_ON_PIN, PS_ON_AWAKE);
  break;
#endif /* (defined(FORK) || (PS_ON_PIN > -1)) && (!defined(FORK) || defined(PS_ON_PIN) && PS_ON_PIN > -1) */
```

* 2 x Keep block
* 2 x Remove block
Note also that the intentions should implicitly trigger their counterparts. With this, two intentions are explicitly declared in the mainline/clone view, and the mirror intent is implicitly applied in the other view.
