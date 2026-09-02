# Firmware pin map and bring-up requirements

Target module: ESP32-S3-WROOM-1-N16R8 (16 MB flash, 8 MB octal PSRAM).

| Function | ESP32-S3 signal |
|---|---|
| microSD CS / MISO / MOSI / SCK / card detect | GPIO4 / 5 / 6 / 7 / 15 |
| Previous / next / menu-wake buttons | GPIO16 / 17 / 18 |
| Status LED | GPIO8 |
| Ambient sensor interrupt / SCL / SDA | GPIO3 / 9 / 10 |
| Display backlight PWM / TE / reset | GPIO11 / 12 / 13 |
| Display CS / D-C / WR / RD | GPIO14 / 21 / 47 / 48 |
| Display DB0..DB7 | GPIO35..GPIO42 |
| Native USB | GPIO19 D- / GPIO20 D+ (module pins USB_D-/USB_D+) |
| UART0 | U0RXD / U0TXD |
| Boot / enable | GPIO0 / EN |

GPIO45 is pulled low for 3.3 V VDD_SPI selection and GPIO46 is pulled low for
normal boot. GPIO0 and EN are pulled high and each has a service button to
ground. Firmware must not repurpose these strap pins.

## Required staged bring-up

1. With display and microSD disconnected, current-limit the certified 5 V
   supply and verify +5V_RAW, protected +5V and +3V3 for shorts, ripple and
   startup sequencing.
2. Confirm TPS62132 switch-node waveform, converter temperature and load-step
   response before enabling Wi-Fi peaks.
3. Validate native USB and UART recovery paths, then confirm boot strapping from
   cold start and reset.
4. Probe all eight display data lines plus CS, D/C, RD, WR, RESET, TE and BL at
   the labelled connector/test points. Start with backlight disabled.
5. Confirm the exact ER-TFTM070-4V3 ordered configuration, interface-mode
   straps, 3.3 V logic acceptance, reset polarity, backlight PWM polarity and
   SSD1963 initialization before writing a framebuffer.
6. Exercise PSRAM and both framebuffer buffers under simultaneous Wi-Fi load.
7. Validate microSD insertion detect, card power transients and sustained writes.
8. Calibrate LTR-303ALS-01 brightness mapping and apply rate limits/hysteresis.
9. Verify button polarity/debounce and ensure the rear-facing status LED cannot
   leak through the display stack.
10. Measure worst-case total input current, display inrush, radio stability,
    enclosure temperatures and connector accessibility in the assembled unit.

Production firmware, OTA security policy, photo-transfer protocol, filesystem
recovery and display colour calibration are out of scope.
