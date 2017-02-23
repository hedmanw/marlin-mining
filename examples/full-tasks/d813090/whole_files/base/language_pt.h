/**
 * Portuguese
 *
 * LCD Menu Messages
 * Please note these are limited to 17 characters!
 *
 */
#ifndef LANGUAGE_PT_H
#define LANGUAGE_PT_H

#define WELCOME_MSG                         MACHINE_NAME " pronto."
#define MSG_SD_INSERTED                     "Cartao inserido"
#define MSG_SD_REMOVED                      "Cartao removido"
#define MSG_MAIN                            " Menu principal \003"
#define MSG_AUTOSTART                       "Autostart"
#define MSG_DISABLE_STEPPERS                " Desligar motores"
#define MSG_AUTO_HOME                       "Ir para home"
#define MSG_SET_HOME_OFFSETS                "Def. home offsets"
#define MSG_SET_ORIGIN                      "Estabelecer orig."
#define MSG_PREHEAT_PLA                     "Pre-aquecer PLA"
#define MSG_PREHEAT_PLA_N                   "Pre-aquecer PLA "
#define MSG_PREHEAT_PLA_ALL                 "Pre-aq. PLA Tudo"
#define MSG_PREHEAT_PLA_BEDONLY             "Pre-aq. PLA \002Base"
#define MSG_PREHEAT_PLA_SETTINGS            "PLA definicoes"
#define MSG_PREHEAT_ABS                     "Pre-aquecer ABS"
#define MSG_PREHEAT_ABS_N                   "Pre-aquecer ABS "
#define MSG_PREHEAT_ABS_ALL                 "Pre-aq. ABS Tudo"
#define MSG_PREHEAT_ABS_BEDONLY             "Pre-aq. ABS \002Base"
#define MSG_PREHEAT_ABS_SETTINGS            "ABS definicoes"
#define MSG_COOLDOWN                        "Arrefecer"
#define MSG_SWITCH_PS_ON                    "Ligar"
#define MSG_SWITCH_PS_OFF                   "Desligar"
#define MSG_EXTRUDE                         "Extrudir"
#define MSG_RETRACT                         "Retrair"
#define MSG_MOVE_AXIS                       "Mover eixo      \x7E"
#define MSG_MOVE_X                          "Mover X"
#define MSG_MOVE_Y                          "Mover Y"
#define MSG_MOVE_Z                          "Mover Z"
#define MSG_MOVE_E                          "Extrusor"
#define MSG_MOVE_01MM                       "Mover 0.1mm"
#define MSG_MOVE_1MM                        "Mover 1mm"
#define MSG_MOVE_10MM                       "Mover 10mm"
#define MSG_SPEED                           "Velocidade"
#define MSG_NOZZLE                          "\002Bico"
#define MSG_BED                             "\002Base"
#define MSG_FAN_SPEED                       "Velocidade do ar."
#define MSG_FLOW                            "Fluxo"
#define MSG_CONTROL                         "Controlo \003"
#define MSG_MIN                             "\002 Min"
#define MSG_MAX                             "\002 Max"
#define MSG_FACTOR                          "\002 Fact"
#define MSG_AUTOTEMP                        "Autotemp"
#define MSG_ON                              "On "
#define MSG_OFF                             "Off"
#define MSG_PID_P                           "PID-P"
#define MSG_PID_I                           "PID-I"
#define MSG_PID_D                           "PID-D"
#define MSG_PID_C                           "PID-C"
#define MSG_ACC                             "Acc"
#define MSG_VXY_JERK                        "Vxy-jerk"
#define MSG_VZ_JERK                         "Vz-jerk"
#define MSG_VE_JERK                         "Ve-jerk"
#define MSG_VMAX                            " Vmax "
#define MSG_X                               "x"
#define MSG_Y                               "y"
#define MSG_Z                               "z"
#define MSG_E                               "e"
#define MSG_VMIN                            "Vmin"
#define MSG_VTRAV_MIN                       "VTrav min"
#define MSG_AMAX                            "Amax "
#define MSG_A_RETRACT                       "A-retract"
#define MSG_XSTEPS                          "Xpasso/mm"
#define MSG_YSTEPS                          "Ypasso/mm"
#define MSG_ZSTEPS                          "Zpasso/mm"
#define MSG_ESTEPS                          "Epasso/mm"
#define MSG_TEMPERATURE                     "Temperatura"
#define MSG_MOTION                          "Movimento"
#define MSG_VOLUMETRIC                      "Filamento"
#define MSG_VOLUMETRIC_ENABLED		        "E in mm3"
#define MSG_FILAMENT_SIZE_EXTRUDER_0        "Fil. Diam. 1"
#define MSG_FILAMENT_SIZE_EXTRUDER_1        "Fil. Diam. 2"
#define MSG_FILAMENT_SIZE_EXTRUDER_2        "Fil. Diam. 3"
#define MSG_CONTRAST                        "Contraste"
#define MSG_STORE_EPROM                     "Guardar na memoria"
#define MSG_LOAD_EPROM                      "Carregar da memoria"
#define MSG_RESTORE_FAILSAFE                "Rest. de emergen."
#define MSG_REFRESH                         "\004Recarregar"
#define MSG_WATCH                           "Monitorar   \003"
#define MSG_PREPARE                         "Preparar \x7E"
#define MSG_TUNE                            "Afinar    \x7E"
#define MSG_PAUSE_PRINT                     "Pausar impressao"
#define MSG_RESUME_PRINT                    "Resumir impressao"
#define MSG_STOP_PRINT                      "Parar impressao"
#define MSG_CARD_MENU                       "Menu cartao SD"
#define MSG_NO_CARD                         "Sem cartao SD"
#define MSG_DWELL                           "Repouso..."
#define MSG_USERWAIT                        "A espera de ordem"
#define MSG_RESUMING                        "Resumir impressao"
#define MSG_PRINT_ABORTED                   "Impr. Cancelada"
#define MSG_NO_MOVE                         "Sem movimento"
#define MSG_KILLED                          "INTRRP. DE EMERG."
#define MSG_STOPPED                         "PARADO. "
#define MSG_CONTROL_RETRACT                 " Retrair mm"
#define MSG_CONTROL_RETRACT_SWAP            "Troca Retrair mm"
#define MSG_CONTROL_RETRACTF                " Retrair  V"
#define MSG_CONTROL_RETRACT_ZLIFT           " Levantar mm"
#define MSG_CONTROL_RETRACT_RECOVER         " DesRet +mm"
#define MSG_CONTROL_RETRACT_RECOVER_SWAP    "Troca DesRet +mm"
#define MSG_CONTROL_RETRACT_RECOVERF        " DesRet  V"
#define MSG_AUTORETRACT                     " AutoRetr."
#define MSG_FILAMENTCHANGE                  "Trocar filamento"
#define MSG_INIT_SDCARD                     "Inic. SD-Card"
#define MSG_CNG_SDCARD                      "Trocar SD-Card"
#define MSG_ZPROBE_OUT                      "Sens. fora da Base"
#define MSG_POSITION_UNKNOWN                "XY antes de Z"
#define MSG_ZPROBE_ZOFFSET                  "Z Offset"
#define MSG_BABYSTEP_X                      "Babystep X"
#define MSG_BABYSTEP_Y                      "Babystep Y"
#define MSG_BABYSTEP_Z                      "Babystep Z"
#define MSG_ENDSTOP_ABORT                   "Endstop abort."

#ifdef DELTA_CALIBRATION_MENU
    #define MSG_DELTA_CALIBRATE             "Delta Calibracao"
    #define MSG_DELTA_CALIBRATE_X           "Calibrar X"
    #define MSG_DELTA_CALIBRATE_Y           "Calibrar Y"
    #define MSG_DELTA_CALIBRATE_Z           "Calibrar Z"
    #define MSG_DELTA_CALIBRATE_CENTER      "Calibrar Centro"
#endif // DELTA_CALIBRATION_MENU

#endif // LANGUAGE_PT_H
