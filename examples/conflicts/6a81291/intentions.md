# Case I
Base
```cpp
#if defined(RA_CONTROL_PANEL)
 #define ULTIPANEL
 #define NEWPANEL
 #define LCD_I2C_TYPE_PCA8574
 #define LCD_I2C_ADDRESS 0x27   // I2C Address of the port expander
#endif
```

Remote
```cpp
#if defined(REPRAPWORLD_KEYPAD)
  #define NEWPANEL
  #define ULTIPANEL
#endif
```

Result
```cpp
#if defined(REPRAPWORLD_KEYPAD)
  #define NEWPANEL
  #define ULTIPANEL
#endif
#if defined(RA_CONTROL_PANEL)
 #define ULTIPANEL
 #define NEWPANEL
 #define LCD_I2C_TYPE_PCA8574
 #define LCD_I2C_ADDRESS 0x27   // I2C Address of the port expander
#endif
```

## Manual resolution
```
<BASE
+ #if defined(RA_CONTROL_PANEL)
+  #define ULTIPANEL
+  #define NEWPANEL
+  #define LCD_I2C_TYPE_PCA8574
+  #define LCD_I2C_ADDRESS 0x27   // I2C Address of the port expander
+ #endif
=============
// Move this block up so that it precedes its predecessor
+ #if defined(REPRAPWORLD_KEYPAD)
+   #define NEWPANEL
+   #define ULTIPANEL
+ #endif
REMOTE>
```

* 2 x Kept blocks
* 0 x Deleted blocks
* 1 x Moved blocks

## Intentions resolution
```cpp
#if (defined(FORK) || defined(RA_CONTROL_PANEL)) && (!defined(FORK) || defined(REPRAPWORLD_KEYPAD))
#ifdef FORK
#define NEWPANEL
#endif /* defined(FORK) */
#define ULTIPANEL
#ifndef FORK
#define NEWPANEL
#define LCD_I2C_TYPE_PCA8574
#define LCD_I2C_ADDRESS 0x27
#endif /* !defined(FORK) */
#endif /* (defined(FORK) || defined(RA_CONTROL_PANEL)) && (!defined(FORK) || defined(REPRAPWORLD_KEYPAD)) */
```

* 0 x Keep block
* 0 x Remove block
* 3 x Change PC