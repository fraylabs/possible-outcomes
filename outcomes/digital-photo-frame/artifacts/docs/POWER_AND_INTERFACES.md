# Power budget and electrical interfaces

Status: design estimate only; not measured on hardware.

## Input and rails

J1 is a GCT USB4105-GF-A USB-C receptacle used as a power-only sink. R1 and R2
are independent 5.1 kohm Rd resistors from CC1 and CC2 to ground. USB data and
SBU pins are intentionally unconnected. U4 (USBLC6-2SC6) protects CC1/CC2 and
uses VBUS as its reference. VBUS passes through F1, a Bourns MF-MSMF200-2
2.0 A resettable protector, to +5V; D1 is an SMAJ5.0A shunt TVS on protected
+5V. This architecture requires a certified regulated 5 V USB-C supply that
advertises sufficient Type-C current; it has no USB PD negotiation.

U2 is TPS62132RGTR, fixed 3.3 V, rated 3 A. It uses a 1.0 uH Coilcraft
XAL4020-102MEC, 10 uF input, two 22 uF output capacitors, 10 nF soft-start, and
the datasheet's fixed-output pin treatment. Exact loop layout is not accepted:
the PCB currently fails DRC.

## Pre-build current budget

| Load | Rail | Budgeted current | Basis |
|---|---:|---:|---|
| ER-TFTM070-4V3 module including backlight | 5 V | 0.480 A max | module datasheet maximum |
| ESP32-S3 module/Wi-Fi peaks | 3.3 V | 0.550 A | conservative bring-up allowance; must be measured |
| microSD write/transient | 3.3 V | 0.200 A | design allowance; card-dependent |
| Ambient sensor, LED, pull networks, margin | 3.3 V | 0.020 A | design allowance |
| 3.3 V total | 3.3 V | 0.770 A | below converter rating |
| 3.3 V input equivalent at 90% efficiency | 5 V | 0.565 A | calculated |
| Combined nominal maximum estimate | 5 V | 1.045 A | display plus converter input |
| Recommended adapter | 5 V | >=2.0 A | transient/thermal headroom |

TPS62132 output loading is approximately 26% of its 3 A rating under this
budget. The input protector is not a precision current limiter, and temperature
derating of the PTC must be checked. Display inrush, Wi-Fi bursts, storage
writes, converter temperature, rail droop and EMI require bench measurement.

## Display interface

J2 implements the documented 40-pin ER-TFTM070-4V3 interface in 8-bit 8080,
5 V, no-touch configuration:

- 1 GND; 2 VDD5V; 3 /CS; 4 D/C; 5 /RD; 6 /WR; 7 RESET; 8 TE.
- 9-16 are DB0-DB7 and connect to ESP32-S3 GPIO35-GPIO42.
- 17-32 (DB8-DB23) are intentionally no-connect for the selected 8-bit mode.
- 33-38 are touch-related pins and are intentionally no-connect for no-touch.
- 39 BL_ON/OFF/PWM is driven by GPIO11 (`LCD_BL`); 40 is NC.

The module's integrated SSD1963 controller and backlight circuitry are the
reason it was selected. The logic-level compatibility and reset/backlight
polarity still require physical confirmation on the exact ordered
configuration; the saved public datasheet could not be downloaded directly in
this environment, although the official URL is recorded.

## Storage, sensing and debug

The Molex 104031-0811 microSD socket is wired in SPI mode with card detect.
LTR-303ALS-01 uses I2C with 4.7 kohm pull-ups, 100 nF local decoupling and an
interrupt line. Three KMR221GLFS buttons pull GPIO inputs to ground with 10 kohm
pull-ups. Reset and boot buttons are separately accessible after rear-cover
removal. J4 exposes 3V3, GND, native USB D+/D-, U0TXD and U0RXD. Test points
cover +5V, +3V3, GND, LCD_WR, LCD_BL and SD_CS.
