EESchema Schematic File Version 4
LIBS:PhotoFrame
EELAYER 29 0
EELAYER END
$Descr A2 23386 16535
encoding utf-8
Sheet 1 1
Title "Seven-inch Digital Photo Frame Controller"
Date "2026-09-03"
Rev "A / DIGITAL PRE-BUILD"
Comp "Cleanroom Burr experiment — not production ready"
Comment1 "ESP32-S3 + SSD1963 8-bit 8080 display"
Comment2 "External certified 5 V USB-C adapter only"
Comment3 "Touch, audio, camera, and battery omitted by definition"
Comment4 "Exact parts and assumptions in reports"
$EndDescr
Text Notes 1800 1200 0    120  ~ 24
POWER INPUT / PROTECTION / 3V3
Text Notes 9300 1200 0    120  ~ 24
ESP32-S3 CONTROLLER / DEBUG
Text Notes 15800 1200 0    120  ~ 24
DISPLAY — 8-BIT 8080, NO TOUCH
Text Notes 5000 10100 0    120  ~ 24
STORAGE / CONTROLS / AMBIENT LIGHT
$Comp
L PhotoFrame:USB4105_GF_A J1
U 1 1 65030000
P 2800 2600
F 0 "J1" H 2800 2350 50  0000 C CNN
F 1 "USB4105-GF-A" H 2800 2850 50  0000 C CNN
F 2 "Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal" H 2800 2600 50  0001 C CNN
F 3 "https://gct.co/files/drawings/usb4105.pdf" H 2800 2600 50  0001 C CNN
F 4 "USB4105-GF-A" H 2800 2600 50  0001 C CNN "MPN"
F 5 "GCT" H 2800 2600 50  0001 C CNN "Manufacturer"
F 6 "USB-C 16-position receptacle; power-only sink" H 2800 2600 50  0001 C CNN "Description"
	1    2800 2600
	1    0    0    -1
$EndComp
Text Label 1900 2200 0    40   ~ 0
GND
Text Label 1900 2300 0    40   ~ 0
+5V_RAW
Text Label 1900 2400 0    40   ~ 0
CC1
NoConn ~ 1900 2500
NoConn ~ 1900 2600
NoConn ~ 1900 2700
Text Label 1900 2800 0    40   ~ 0
+5V_RAW
Text Label 1900 2900 0    40   ~ 0
GND
Text Label 1900 3000 0    40   ~ 0
GND
Text Label 3700 2200 0    40   ~ 0
+5V_RAW
Text Label 3700 2300 0    40   ~ 0
CC2
NoConn ~ 3700 2400
NoConn ~ 3700 2500
NoConn ~ 3700 2600
Text Label 3700 2700 0    40   ~ 0
+5V_RAW
Text Label 3700 2800 0    40   ~ 0
GND
Text Label 3700 2900 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R1
U 1 1 65030001
P 4300 2200
F 0 "R1" H 4300 1950 50  0000 C CNN
F 1 "5.1k 1%" H 4300 2450 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4300 2200 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 4300 2200 50  0001 C CNN
F 4 "RC0603FR-075K1L" H 4300 2200 50  0001 C CNN "MPN"
F 5 "Yageo" H 4300 2200 50  0001 C CNN "Manufacturer"
F 6 "USB-C CC1 Rd sink resistor" H 4300 2200 50  0001 C CNN "Description"
	1    4300 2200
	1    0    0    -1
$EndComp
Text Label 3400 2150 0    40   ~ 0
CC1
Text Label 5200 2150 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R2
U 1 1 65030002
P 4300 3000
F 0 "R2" H 4300 2750 50  0000 C CNN
F 1 "5.1k 1%" H 4300 3250 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 4300 3000 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 4300 3000 50  0001 C CNN
F 4 "RC0603FR-075K1L" H 4300 3000 50  0001 C CNN "MPN"
F 5 "Yageo" H 4300 3000 50  0001 C CNN "Manufacturer"
F 6 "USB-C CC2 Rd sink resistor" H 4300 3000 50  0001 C CNN "Description"
	1    4300 3000
	1    0    0    -1
$EndComp
Text Label 3400 2950 0    40   ~ 0
CC2
Text Label 5200 2950 0    40   ~ 0
GND
$Comp
L PhotoFrame:USBLC6_2SC6 U4
U 1 1 65030003
P 5300 2600
F 0 "U4" H 5300 2350 50  0000 C CNN
F 1 "USBLC6-2SC6" H 5300 2850 50  0000 C CNN
F 2 "Package_TO_SOT_SMD:SOT-23-6" H 5300 2600 50  0001 C CNN
F 3 "https://www.st.com/resource/en/datasheet/usblc6-2.pdf" H 5300 2600 50  0001 C CNN
F 4 "USBLC6-2SC6" H 5300 2600 50  0001 C CNN "MPN"
F 5 "STMicroelectronics" H 5300 2600 50  0001 C CNN "Manufacturer"
F 6 "ESD protection for both USB-C CC pins and VBUS reference" H 5300 2600 50  0001 C CNN "Description"
	1    5300 2600
	1    0    0    -1
$EndComp
Text Label 4400 2500 0    40   ~ 0
CC1
Text Label 4400 2600 0    40   ~ 0
GND
Text Label 4400 2700 0    40   ~ 0
CC2
Text Label 6200 2500 0    40   ~ 0
CC2
Text Label 6200 2600 0    40   ~ 0
+5V_RAW
Text Label 6200 2700 0    40   ~ 0
CC1
$Comp
L PhotoFrame:FUSE_EXACT F1
U 1 1 65030004
P 6500 2600
F 0 "F1" H 6500 2350 50  0000 C CNN
F 1 "2.0A resettable" H 6500 2850 50  0000 C CNN
F 2 "Fuse:Fuse_1206_3216Metric" H 6500 2600 50  0001 C CNN
F 3 "https://www.bourns.com/docs/product-datasheets/mf-msmf.pdf" H 6500 2600 50  0001 C CNN
F 4 "MF-MSMF200-2" H 6500 2600 50  0001 C CNN "MPN"
F 5 "Bourns" H 6500 2600 50  0001 C CNN "Manufacturer"
F 6 "Resettable input current limiter" H 6500 2600 50  0001 C CNN "Description"
	1    6500 2600
	1    0    0    -1
$EndComp
Text Label 5600 2550 0    40   ~ 0
+5V_RAW
Text Label 7400 2550 0    40   ~ 0
+5V
$Comp
L PhotoFrame:DIODE_EXACT D1
U 1 1 65030005
P 7600 2600
F 0 "D1" H 7600 2350 50  0000 C CNN
F 1 "SMAJ5.0A" H 7600 2850 50  0000 C CNN
F 2 "Diode_SMD:D_SMA" H 7600 2600 50  0001 C CNN
F 3 "https://www.littelfuse.com/assetdocs/littelfuse-tvs-diode-smaj-datasheet" H 7600 2600 50  0001 C CNN
F 4 "SMAJ5.0A" H 7600 2600 50  0001 C CNN "MPN"
F 5 "Littelfuse" H 7600 2600 50  0001 C CNN "Manufacturer"
F 6 "Unidirectional 5 V rail TVS" H 7600 2600 50  0001 C CNN "Description"
	1    7600 2600
	1    0    0    -1
$EndComp
Text Label 6700 2550 0    40   ~ 0
+5V
Text Label 8500 2550 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C1
U 1 1 65030006
P 8500 2600
F 0 "C1" H 8500 2350 50  0000 C CNN
F 1 "22uF 10V X5R" H 8500 2850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 8500 2600 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A226ME44-01.pdf" H 8500 2600 50  0001 C CNN
F 4 "GRM21BR61A226ME44L" H 8500 2600 50  0001 C CNN "MPN"
F 5 "Murata" H 8500 2600 50  0001 C CNN "Manufacturer"
F 6 "Protected 5 V bulk capacitor; 10 V rating" H 8500 2600 50  0001 C CNN "Description"
	1    8500 2600
	1    0    0    -1
$EndComp
Text Label 7600 2550 0    40   ~ 0
+5V
Text Label 9400 2550 0    40   ~ 0
GND
$Comp
L PhotoFrame:TPS62132RGTR U2
U 1 1 65030007
P 5200 4800
F 0 "U2" H 5200 4550 50  0000 C CNN
F 1 "TPS62132RGTR 3.3V" H 5200 5050 50  0000 C CNN
F 2 "Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias" H 5200 4800 50  0001 C CNN
F 3 "https://www.ti.com/lit/ds/symlink/tps62132.pdf" H 5200 4800 50  0001 C CNN
F 4 "TPS62132RGTR" H 5200 4800 50  0001 C CNN "MPN"
F 5 "Texas Instruments" H 5200 4800 50  0001 C CNN "Manufacturer"
F 6 "3 A fixed 3.3 V synchronous buck" H 5200 4800 50  0001 C CNN "Description"
	1    5200 4800
	1    0    0    -1
$EndComp
Text Label 4300 4400 0    40   ~ 0
SW
Text Label 4300 4500 0    40   ~ 0
SW
Text Label 4300 4600 0    40   ~ 0
SW
Text Label 4300 4700 0    40   ~ 0
PGOOD
NoConn ~ 4300 4800
Text Label 4300 4900 0    40   ~ 0
GND
Text Label 4300 5000 0    40   ~ 0
GND
Text Label 4300 5100 0    40   ~ 0
GND
Text Label 4300 5200 0    40   ~ 0
SS
Text Label 6100 4400 0    40   ~ 0
+5V
Text Label 6100 4500 0    40   ~ 0
+5V
Text Label 6100 4600 0    40   ~ 0
+5V
Text Label 6100 4700 0    40   ~ 0
+5V
Text Label 6100 4800 0    40   ~ 0
+3V3
Text Label 6100 4900 0    40   ~ 0
GND
Text Label 6100 5000 0    40   ~ 0
GND
Text Label 6100 5100 0    40   ~ 0
GND
$Comp
L PhotoFrame:L_EXACT L1
U 1 1 65030008
P 6800 4400
F 0 "L1" H 6800 4150 50  0000 C CNN
F 1 "1.0uH 20%" H 6800 4650 50  0000 C CNN
F 2 "Inductor_SMD:L_Bourns-SRU8028_8.0x8.0mm" H 6800 4400 50  0001 C CNN
F 3 "https://www.coilcraft.com/getmedia/5e5308cc-2480-4f52-be4a-cbbfc5c2eb1f/xal4020.pdf" H 6800 4400 50  0001 C CNN
F 4 "XAL4020-102MEC" H 6800 4400 50  0001 C CNN "MPN"
F 5 "Coilcraft" H 6800 4400 50  0001 C CNN "Manufacturer"
F 6 "Shielded buck inductor; Isat 7.6 A" H 6800 4400 50  0001 C CNN "Description"
	1    6800 4400
	1    0    0    -1
$EndComp
Text Label 5900 4350 0    40   ~ 0
SW
Text Label 7700 4350 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:C_EXACT C2
U 1 1 65030009
P 6500 5200
F 0 "C2" H 6500 4950 50  0000 C CNN
F 1 "10nF 25V X7R" H 6500 5450 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 6500 5200 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM188R71E103KA01-01.pdf" H 6500 5200 50  0001 C CNN
F 4 "GRM188R71E103KA01D" H 6500 5200 50  0001 C CNN "MPN"
F 5 "Murata" H 6500 5200 50  0001 C CNN "Manufacturer"
F 6 "Buck soft-start capacitor" H 6500 5200 50  0001 C CNN "Description"
	1    6500 5200
	1    0    0    -1
$EndComp
Text Label 5600 5150 0    40   ~ 0
SS
Text Label 7400 5150 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C3
U 1 1 6503000A
P 7600 4600
F 0 "C3" H 7600 4350 50  0000 C CNN
F 1 "22uF 10V X5R" H 7600 4850 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 7600 4600 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A226ME44-01.pdf" H 7600 4600 50  0001 C CNN
F 4 "GRM21BR61A226ME44L" H 7600 4600 50  0001 C CNN "MPN"
F 5 "Murata" H 7600 4600 50  0001 C CNN "Manufacturer"
F 6 "3.3 V output capacitor; 10 V rating" H 7600 4600 50  0001 C CNN "Description"
	1    7600 4600
	1    0    0    -1
$EndComp
Text Label 6700 4550 0    40   ~ 0
+3V3
Text Label 8500 4550 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C4
U 1 1 6503000B
P 7600 5200
F 0 "C4" H 7600 4950 50  0000 C CNN
F 1 "22uF 10V X5R" H 7600 5450 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 7600 5200 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A226ME44-01.pdf" H 7600 5200 50  0001 C CNN
F 4 "GRM21BR61A226ME44L" H 7600 5200 50  0001 C CNN "MPN"
F 5 "Murata" H 7600 5200 50  0001 C CNN "Manufacturer"
F 6 "3.3 V output capacitor; 10 V rating" H 7600 5200 50  0001 C CNN "Description"
	1    7600 5200
	1    0    0    -1
$EndComp
Text Label 6700 5150 0    40   ~ 0
+3V3
Text Label 8500 5150 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C5
U 1 1 6503000C
P 7600 5800
F 0 "C5" H 7600 5550 50  0000 C CNN
F 1 "10uF 10V X5R" H 7600 6050 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 7600 5800 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A106KE19-01.pdf" H 7600 5800 50  0001 C CNN
F 4 "GRM21BR61A106KE19L" H 7600 5800 50  0001 C CNN "MPN"
F 5 "Murata" H 7600 5800 50  0001 C CNN "Manufacturer"
F 6 "Buck input capacitor" H 7600 5800 50  0001 C CNN "Description"
	1    7600 5800
	1    0    0    -1
$EndComp
Text Label 6700 5750 0    40   ~ 0
+5V
Text Label 8500 5750 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R3
U 1 1 6503000D
P 6500 5800
F 0 "R3" H 6500 5550 50  0000 C CNN
F 1 "100k 1%" H 6500 6050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6500 5800 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 6500 5800 50  0001 C CNN
F 4 "RC0603FR-07100KL" H 6500 5800 50  0001 C CNN "MPN"
F 5 "Yageo" H 6500 5800 50  0001 C CNN "Manufacturer"
F 6 "Power-good pull-up" H 6500 5800 50  0001 C CNN "Description"
	1    6500 5800
	1    0    0    -1
$EndComp
Text Label 5600 5750 0    40   ~ 0
PGOOD
Text Label 7400 5750 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:ESP32_S3_WROOM_1_N16R8 U1
U 1 1 6503000E
P 11200 6500
F 0 "U1" H 11200 6250 50  0000 C CNN
F 1 "ESP32-S3-WROOM-1-N16R8" H 11200 6750 50  0000 C CNN
F 2 "RF_Module:ESP32-S3-WROOM-1" H 11200 6500 50  0001 C CNN
F 3 "https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf" H 11200 6500 50  0001 C CNN
F 4 "ESP32-S3-WROOM-1-N16R8" H 11200 6500 50  0001 C CNN "MPN"
F 5 "Espressif Systems" H 11200 6500 50  0001 C CNN "Manufacturer"
F 6 "Wi-Fi MCU module; 16 MB flash and 8 MB octal PSRAM" H 11200 6500 50  0001 C CNN "Description"
	1    11200 6500
	1    0    0    -1
$EndComp
Text Label 10300 5500 0    40   ~ 0
GND
Text Label 10300 5600 0    40   ~ 0
+3V3
Text Label 10300 5700 0    40   ~ 0
EN
Text Label 10300 5800 0    40   ~ 0
SD_CS
Text Label 10300 5900 0    40   ~ 0
SD_MISO
Text Label 10300 6000 0    40   ~ 0
SD_MOSI
Text Label 10300 6100 0    40   ~ 0
SD_SCK
Text Label 10300 6200 0    40   ~ 0
SD_CD
Text Label 10300 6300 0    40   ~ 0
BTN_PREV
Text Label 10300 6400 0    40   ~ 0
BTN_NEXT
Text Label 10300 6500 0    40   ~ 0
BTN_MENU
Text Label 10300 6600 0    40   ~ 0
STATUS_LED
Text Label 10300 6700 0    40   ~ 0
USB_D-
Text Label 10300 6800 0    40   ~ 0
USB_D+
Text Label 10300 6900 0    40   ~ 0
ALS_INT
Text Label 10300 7000 0    40   ~ 0
STRAP46
Text Label 10300 7100 0    40   ~ 0
I2C_SCL
Text Label 10300 7200 0    40   ~ 0
I2C_SDA
Text Label 10300 7300 0    40   ~ 0
LCD_BL
Text Label 10300 7400 0    40   ~ 0
LCD_TE
Text Label 10300 7500 0    40   ~ 0
LCD_RST
Text Label 12100 5500 0    40   ~ 0
LCD_CS
Text Label 12100 5600 0    40   ~ 0
LCD_DC
Text Label 12100 5700 0    40   ~ 0
LCD_WR
Text Label 12100 5800 0    40   ~ 0
LCD_RD
Text Label 12100 5900 0    40   ~ 0
STRAP45
Text Label 12100 6000 0    40   ~ 0
BOOT
Text Label 12100 6100 0    40   ~ 0
LCD_D0
Text Label 12100 6200 0    40   ~ 0
LCD_D1
Text Label 12100 6300 0    40   ~ 0
LCD_D2
Text Label 12100 6400 0    40   ~ 0
LCD_D3
Text Label 12100 6500 0    40   ~ 0
LCD_D4
Text Label 12100 6600 0    40   ~ 0
LCD_D5
Text Label 12100 6700 0    40   ~ 0
LCD_D6
Text Label 12100 6800 0    40   ~ 0
LCD_D7
Text Label 12100 6900 0    40   ~ 0
U0RXD
Text Label 12100 7000 0    40   ~ 0
U0TXD
NoConn ~ 12100 7100
NoConn ~ 12100 7200
Text Label 12100 7300 0    40   ~ 0
GND
Text Label 12100 7400 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C6
U 1 1 6503000F
P 9200 5200
F 0 "C6" H 9200 4950 50  0000 C CNN
F 1 "10uF 10V X5R" H 9200 5450 50  0000 C CNN
F 2 "Capacitor_SMD:C_0805_2012Metric" H 9200 5200 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/owa/CATALOG.showcatalog" H 9200 5200 50  0001 C CNN
F 4 "GRM21BR61A106KE19L" H 9200 5200 50  0001 C CNN "MPN"
F 5 "Murata" H 9200 5200 50  0001 C CNN "Manufacturer"
F 6 "ESP32 local decoupling" H 9200 5200 50  0001 C CNN "Description"
	1    9200 5200
	1    0    0    -1
$EndComp
Text Label 8300 5150 0    40   ~ 0
+3V3
Text Label 10100 5150 0    40   ~ 0
GND
$Comp
L PhotoFrame:C_EXACT C7
U 1 1 65030010
P 9200 5700
F 0 "C7" H 9200 5450 50  0000 C CNN
F 1 "100nF 16V X7R" H 9200 5950 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 9200 5700 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/owa/CATALOG.showcatalog" H 9200 5700 50  0001 C CNN
F 4 "GRM188R71C104KA01D" H 9200 5700 50  0001 C CNN "MPN"
F 5 "Murata" H 9200 5700 50  0001 C CNN "Manufacturer"
F 6 "ESP32 local decoupling" H 9200 5700 50  0001 C CNN "Description"
	1    9200 5700
	1    0    0    -1
$EndComp
Text Label 8300 5650 0    40   ~ 0
+3V3
Text Label 10100 5650 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R4
U 1 1 65030011
P 9200 6400
F 0 "R4" H 9200 6150 50  0000 C CNN
F 1 "10k 1%" H 9200 6650 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 6400 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 9200 6400 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 9200 6400 50  0001 C CNN "MPN"
F 5 "Yageo" H 9200 6400 50  0001 C CNN "Manufacturer"
F 6 "ESP32 enable pull-up" H 9200 6400 50  0001 C CNN "Description"
	1    9200 6400
	1    0    0    -1
$EndComp
Text Label 8300 6350 0    40   ~ 0
EN
Text Label 10100 6350 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:R_EXACT R5
U 1 1 65030012
P 9200 7000
F 0 "R5" H 9200 6750 50  0000 C CNN
F 1 "10k 1%" H 9200 7250 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 7000 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 9200 7000 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 9200 7000 50  0001 C CNN "MPN"
F 5 "Yageo" H 9200 7000 50  0001 C CNN "Manufacturer"
F 6 "ESP32 GPIO0 boot pull-up" H 9200 7000 50  0001 C CNN "Description"
	1    9200 7000
	1    0    0    -1
$EndComp
Text Label 8300 6950 0    40   ~ 0
BOOT
Text Label 10100 6950 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:R_EXACT R6
U 1 1 65030013
P 9200 7600
F 0 "R6" H 9200 7350 50  0000 C CNN
F 1 "10k 1%" H 9200 7850 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 7600 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 9200 7600 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 9200 7600 50  0001 C CNN "MPN"
F 5 "Yageo" H 9200 7600 50  0001 C CNN "Manufacturer"
F 6 "GPIO45 strap pull-down for 3.3 V VDD_SPI" H 9200 7600 50  0001 C CNN "Description"
	1    9200 7600
	1    0    0    -1
$EndComp
Text Label 8300 7550 0    40   ~ 0
STRAP45
Text Label 10100 7550 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R7
U 1 1 65030014
P 9200 8200
F 0 "R7" H 9200 7950 50  0000 C CNN
F 1 "10k 1%" H 9200 8450 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 9200 8200 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 9200 8200 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 9200 8200 50  0001 C CNN "MPN"
F 5 "Yageo" H 9200 8200 50  0001 C CNN "Manufacturer"
F 6 "GPIO46 strap pull-down for normal boot" H 9200 8200 50  0001 C CNN "Description"
	1    9200 8200
	1    0    0    -1
$EndComp
Text Label 8300 8150 0    40   ~ 0
STRAP46
Text Label 10100 8150 0    40   ~ 0
GND
$Comp
L PhotoFrame:SW_KMR2 SW4
U 1 1 65030015
P 9200 8800
F 0 "SW4" H 9200 8550 50  0000 C CNN
F 1 "KMR221GLFS" H 9200 9050 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG" H 9200 8800 50  0001 C CNN
F 3 "https://www.ckswitches.com/media/1479/kmr2.pdf" H 9200 8800 50  0001 C CNN
F 4 "KMR221GLFS" H 9200 8800 50  0001 C CNN "MPN"
F 5 "C&K" H 9200 8800 50  0001 C CNN "Manufacturer"
F 6 "Reset access" H 9200 8800 50  0001 C CNN "Description"
	1    9200 8800
	1    0    0    -1
$EndComp
Text Label 8300 8750 0    40   ~ 0
EN
Text Label 8300 8850 0    40   ~ 0
GND
Text Label 10100 8750 0    40   ~ 0
GND
$Comp
L PhotoFrame:SW_KMR2 SW5
U 1 1 65030016
P 9200 9400
F 0 "SW5" H 9200 9150 50  0000 C CNN
F 1 "KMR221GLFS" H 9200 9650 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG" H 9200 9400 50  0001 C CNN
F 3 "https://www.ckswitches.com/media/1479/kmr2.pdf" H 9200 9400 50  0001 C CNN
F 4 "KMR221GLFS" H 9200 9400 50  0001 C CNN "MPN"
F 5 "C&K" H 9200 9400 50  0001 C CNN "Manufacturer"
F 6 "Bootloader access" H 9200 9400 50  0001 C CNN "Description"
	1    9200 9400
	1    0    0    -1
$EndComp
Text Label 8300 9350 0    40   ~ 0
BOOT
Text Label 8300 9450 0    40   ~ 0
GND
Text Label 10100 9350 0    40   ~ 0
GND
$Comp
L PhotoFrame:HEADER_1X6 J4
U 1 1 65030017
P 9200 10400
F 0 "J4" H 9200 10150 50  0000 C CNN
F 1 "DEBUG 1x6" H 9200 10650 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical" H 9200 10400 50  0001 C CNN
F 3 "https://cdn.harwin.com/pdfs/M20-999.pdf" H 9200 10400 50  0001 C CNN
F 4 "M20-9990646" H 9200 10400 50  0001 C CNN "MPN"
F 5 "Harwin" H 9200 10400 50  0001 C CNN "Manufacturer"
F 6 "Internal programming and debug header" H 9200 10400 50  0001 C CNN "Description"
	1    9200 10400
	1    0    0    -1
$EndComp
Text Label 8300 10300 0    40   ~ 0
+3V3
Text Label 8300 10400 0    40   ~ 0
GND
Text Label 8300 10500 0    40   ~ 0
USB_D+
Text Label 10100 10300 0    40   ~ 0
USB_D-
Text Label 10100 10400 0    40   ~ 0
U0TXD
Text Label 10100 10500 0    40   ~ 0
U0RXD
$Comp
L PhotoFrame:ER_TFTM070_4V3 J2
U 1 1 65030018
P 17400 6500
F 0 "J2" H 17400 6250 50  0000 C CNN
F 1 "ER-TFTM070-4V3 8-bit 8080 5V no-touch" H 17400 6750 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical" H 17400 6500 50  0001 C CNN
F 3 "https://www.buydisplay.com/download/manual/ER-TFTM070-4V3_Datasheet.pdf" H 17400 6500 50  0001 C CNN
F 4 "ER-TFTM070-4V3" H 17400 6500 50  0001 C CNN "MPN"
F 5 "EastRising" H 17400 6500 50  0001 C CNN "Manufacturer"
F 6 "7-inch 800x480 SSD1963 display module; pin-header configuration" H 17400 6500 50  0001 C CNN "Description"
	1    17400 6500
	1    0    0    -1
$EndComp
Text Label 16500 5550 0    40   ~ 0
GND
Text Label 16500 5650 0    40   ~ 0
+5V
Text Label 16500 5750 0    40   ~ 0
LCD_CS
Text Label 16500 5850 0    40   ~ 0
LCD_DC
Text Label 16500 5950 0    40   ~ 0
LCD_RD
Text Label 16500 6050 0    40   ~ 0
LCD_WR
Text Label 16500 6150 0    40   ~ 0
LCD_RST
Text Label 16500 6250 0    40   ~ 0
LCD_TE
Text Label 16500 6350 0    40   ~ 0
LCD_D0
Text Label 16500 6450 0    40   ~ 0
LCD_D1
Text Label 16500 6550 0    40   ~ 0
LCD_D2
Text Label 16500 6650 0    40   ~ 0
LCD_D3
Text Label 16500 6750 0    40   ~ 0
LCD_D4
Text Label 16500 6850 0    40   ~ 0
LCD_D5
Text Label 16500 6950 0    40   ~ 0
LCD_D6
Text Label 16500 7050 0    40   ~ 0
LCD_D7
NoConn ~ 16500 7150
NoConn ~ 16500 7250
NoConn ~ 16500 7350
NoConn ~ 16500 7450
NoConn ~ 18300 5550
NoConn ~ 18300 5650
NoConn ~ 18300 5750
NoConn ~ 18300 5850
NoConn ~ 18300 5950
NoConn ~ 18300 6050
NoConn ~ 18300 6150
NoConn ~ 18300 6250
NoConn ~ 18300 6350
NoConn ~ 18300 6450
NoConn ~ 18300 6550
NoConn ~ 18300 6650
NoConn ~ 18300 6750
NoConn ~ 18300 6850
NoConn ~ 18300 6950
NoConn ~ 18300 7050
NoConn ~ 18300 7150
NoConn ~ 18300 7250
Text Label 18300 7350 0    40   ~ 0
LCD_BL
NoConn ~ 18300 7450
$Comp
L PhotoFrame:MICROSD_104031_0811 J3
U 1 1 65030019
P 13200 11200
F 0 "J3" H 13200 10950 50  0000 C CNN
F 1 "104031-0811" H 13200 11450 50  0000 C CNN
F 2 "Connector_Card:microSD_HC_Molex_104031-0811" H 13200 11200 50  0001 C CNN
F 3 "https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/104/104031/PS-104031-001-001.pdf" H 13200 11200 50  0001 C CNN
F 4 "104031-0811" H 13200 11200 50  0001 C CNN "MPN"
F 5 "Molex" H 13200 11200 50  0001 C CNN "Manufacturer"
F 6 "Push-pull microSD socket with detect switch" H 13200 11200 50  0001 C CNN "Description"
	1    13200 11200
	1    0    0    -1
$EndComp
NoConn ~ 12300 10950
Text Label 12300 11050 0    40   ~ 0
SD_CS
Text Label 12300 11150 0    40   ~ 0
SD_MOSI
Text Label 12300 11250 0    40   ~ 0
+3V3
Text Label 12300 11350 0    40   ~ 0
SD_SCK
Text Label 12300 11450 0    40   ~ 0
GND
Text Label 14100 10950 0    40   ~ 0
SD_MISO
NoConn ~ 14100 11050
Text Label 14100 11150 0    40   ~ 0
SD_CD
Text Label 14100 11250 0    40   ~ 0
GND
Text Label 14100 11350 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R8
U 1 1 6503001A
P 14500 11200
F 0 "R8" H 14500 10950 50  0000 C CNN
F 1 "10k 1%" H 14500 11450 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 14500 11200 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 14500 11200 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 14500 11200 50  0001 C CNN "MPN"
F 5 "Yageo" H 14500 11200 50  0001 C CNN "Manufacturer"
F 6 "microSD card-detect pull-up" H 14500 11200 50  0001 C CNN "Description"
	1    14500 11200
	1    0    0    -1
$EndComp
Text Label 13600 11150 0    40   ~ 0
SD_CD
Text Label 15400 11150 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:LTR_303ALS_01 U3
U 1 1 6503001B
P 7800 11200
F 0 "U3" H 7800 10950 50  0000 C CNN
F 1 "LTR-303ALS-01" H 7800 11450 50  0000 C CNN
F 2 "OptoDevice:Lite-On_LTR-303ALS-01" H 7800 11200 50  0001 C CNN
F 3 "https://optoelectronics.liteon.com/upload/download/DS86-2013-0004/LTR-303ALS-01_DS_V1.1.PDF" H 7800 11200 50  0001 C CNN
F 4 "LTR-303ALS-01" H 7800 11200 50  0001 C CNN "MPN"
F 5 "Lite-On" H 7800 11200 50  0001 C CNN "Manufacturer"
F 6 "I2C ambient-light sensor" H 7800 11200 50  0001 C CNN "Description"
	1    7800 11200
	1    0    0    -1
$EndComp
Text Label 6900 11100 0    40   ~ 0
+3V3
NoConn ~ 6900 11200
Text Label 6900 11300 0    40   ~ 0
GND
Text Label 8700 11100 0    40   ~ 0
I2C_SCL
Text Label 8700 11200 0    40   ~ 0
ALS_INT
Text Label 8700 11300 0    40   ~ 0
I2C_SDA
$Comp
L PhotoFrame:R_EXACT R9
U 1 1 6503001C
P 6400 10800
F 0 "R9" H 6400 10550 50  0000 C CNN
F 1 "4.7k 1%" H 6400 11050 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6400 10800 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 6400 10800 50  0001 C CNN
F 4 "RC0603FR-074K7L" H 6400 10800 50  0001 C CNN "MPN"
F 5 "Yageo" H 6400 10800 50  0001 C CNN "Manufacturer"
F 6 "I2C pull-up" H 6400 10800 50  0001 C CNN "Description"
	1    6400 10800
	1    0    0    -1
$EndComp
Text Label 5500 10750 0    40   ~ 0
I2C_SCL
Text Label 7300 10750 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:R_EXACT R10
U 1 1 6503001D
P 6400 11400
F 0 "R10" H 6400 11150 50  0000 C CNN
F 1 "4.7k 1%" H 6400 11650 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 6400 11400 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 6400 11400 50  0001 C CNN
F 4 "RC0603FR-074K7L" H 6400 11400 50  0001 C CNN "MPN"
F 5 "Yageo" H 6400 11400 50  0001 C CNN "Manufacturer"
F 6 "I2C pull-up" H 6400 11400 50  0001 C CNN "Description"
	1    6400 11400
	1    0    0    -1
$EndComp
Text Label 5500 11350 0    40   ~ 0
I2C_SDA
Text Label 7300 11350 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:C_EXACT C8
U 1 1 6503001E
P 9000 11200
F 0 "C8" H 9000 10950 50  0000 C CNN
F 1 "100nF 16V X7R" H 9000 11450 50  0000 C CNN
F 2 "Capacitor_SMD:C_0603_1608Metric" H 9000 11200 50  0001 C CNN
F 3 "https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM188R71C104KA01-01.pdf" H 9000 11200 50  0001 C CNN
F 4 "GRM188R71C104KA01D" H 9000 11200 50  0001 C CNN "MPN"
F 5 "Murata" H 9000 11200 50  0001 C CNN "Manufacturer"
F 6 "Ambient sensor decoupling" H 9000 11200 50  0001 C CNN "Description"
	1    9000 11200
	1    0    0    -1
$EndComp
Text Label 8100 11150 0    40   ~ 0
+3V3
Text Label 9900 11150 0    40   ~ 0
GND
$Comp
L PhotoFrame:SW_KMR2 SW1
U 1 1 6503001F
P 10200 12400
F 0 "SW1" H 10200 12150 50  0000 C CNN
F 1 "KMR221GLFS" H 10200 12650 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG" H 10200 12400 50  0001 C CNN
F 3 "https://www.ckswitches.com/media/1479/kmr2.pdf" H 10200 12400 50  0001 C CNN
F 4 "KMR221GLFS" H 10200 12400 50  0001 C CNN "MPN"
F 5 "C&K" H 10200 12400 50  0001 C CNN "Manufacturer"
F 6 "Previous button" H 10200 12400 50  0001 C CNN "Description"
	1    10200 12400
	1    0    0    -1
$EndComp
Text Label 9300 12350 0    40   ~ 0
BTN_PREV
Text Label 9300 12450 0    40   ~ 0
GND
Text Label 11100 12350 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R11
U 1 1 65030020
P 11600 12400
F 0 "R11" H 11600 12150 50  0000 C CNN
F 1 "10k 1%" H 11600 12650 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 11600 12400 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 11600 12400 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 11600 12400 50  0001 C CNN "MPN"
F 5 "Yageo" H 11600 12400 50  0001 C CNN "Manufacturer"
F 6 "User-button pull-up" H 11600 12400 50  0001 C CNN "Description"
	1    11600 12400
	1    0    0    -1
$EndComp
Text Label 10700 12350 0    40   ~ 0
BTN_PREV
Text Label 12500 12350 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:SW_KMR2 SW2
U 1 1 65030021
P 10200 13200
F 0 "SW2" H 10200 12950 50  0000 C CNN
F 1 "KMR221GLFS" H 10200 13450 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG" H 10200 13200 50  0001 C CNN
F 3 "https://www.ckswitches.com/media/1479/kmr2.pdf" H 10200 13200 50  0001 C CNN
F 4 "KMR221GLFS" H 10200 13200 50  0001 C CNN "MPN"
F 5 "C&K" H 10200 13200 50  0001 C CNN "Manufacturer"
F 6 "Next button" H 10200 13200 50  0001 C CNN "Description"
	1    10200 13200
	1    0    0    -1
$EndComp
Text Label 9300 13150 0    40   ~ 0
BTN_NEXT
Text Label 9300 13250 0    40   ~ 0
GND
Text Label 11100 13150 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R12
U 1 1 65030022
P 11600 13200
F 0 "R12" H 11600 12950 50  0000 C CNN
F 1 "10k 1%" H 11600 13450 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 11600 13200 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 11600 13200 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 11600 13200 50  0001 C CNN "MPN"
F 5 "Yageo" H 11600 13200 50  0001 C CNN "Manufacturer"
F 6 "User-button pull-up" H 11600 13200 50  0001 C CNN "Description"
	1    11600 13200
	1    0    0    -1
$EndComp
Text Label 10700 13150 0    40   ~ 0
BTN_NEXT
Text Label 12500 13150 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:SW_KMR2 SW3
U 1 1 65030023
P 10200 14000
F 0 "SW3" H 10200 13750 50  0000 C CNN
F 1 "KMR221GLFS" H 10200 14250 50  0000 C CNN
F 2 "Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG" H 10200 14000 50  0001 C CNN
F 3 "https://www.ckswitches.com/media/1479/kmr2.pdf" H 10200 14000 50  0001 C CNN
F 4 "KMR221GLFS" H 10200 14000 50  0001 C CNN "MPN"
F 5 "C&K" H 10200 14000 50  0001 C CNN "Manufacturer"
F 6 "Menu/wake button" H 10200 14000 50  0001 C CNN "Description"
	1    10200 14000
	1    0    0    -1
$EndComp
Text Label 9300 13950 0    40   ~ 0
BTN_MENU
Text Label 9300 14050 0    40   ~ 0
GND
Text Label 11100 13950 0    40   ~ 0
GND
$Comp
L PhotoFrame:R_EXACT R13
U 1 1 65030024
P 11600 14000
F 0 "R13" H 11600 13750 50  0000 C CNN
F 1 "10k 1%" H 11600 14250 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 11600 14000 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 11600 14000 50  0001 C CNN
F 4 "RC0603FR-0710KL" H 11600 14000 50  0001 C CNN "MPN"
F 5 "Yageo" H 11600 14000 50  0001 C CNN "Manufacturer"
F 6 "User-button pull-up" H 11600 14000 50  0001 C CNN "Description"
	1    11600 14000
	1    0    0    -1
$EndComp
Text Label 10700 13950 0    40   ~ 0
BTN_MENU
Text Label 12500 13950 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:R_EXACT R14
U 1 1 65030025
P 15000 12400
F 0 "R14" H 15000 12150 50  0000 C CNN
F 1 "1.0k 1%" H 15000 12650 50  0000 C CNN
F 2 "Resistor_SMD:R_0603_1608Metric" H 15000 12400 50  0001 C CNN
F 3 "https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf" H 15000 12400 50  0001 C CNN
F 4 "RC0603FR-071KL" H 15000 12400 50  0001 C CNN "MPN"
F 5 "Yageo" H 15000 12400 50  0001 C CNN "Manufacturer"
F 6 "Status LED current limit" H 15000 12400 50  0001 C CNN "Description"
	1    15000 12400
	1    0    0    -1
$EndComp
Text Label 14100 12350 0    40   ~ 0
+3V3
Text Label 15900 12350 0    40   ~ 0
LED_A
$Comp
L PhotoFrame:LED_EXACT LED1
U 1 1 65030026
P 16400 12400
F 0 "LED1" H 16400 12150 50  0000 C CNN
F 1 "LTST-C191KGKT green" H 16400 12650 50  0000 C CNN
F 2 "LED_SMD:LED_0603_1608Metric" H 16400 12400 50  0001 C CNN
F 3 "https://optoelectronics.liteon.com/upload/download/DS22-2000-228/LTST-C191KGKT.pdf" H 16400 12400 50  0001 C CNN
F 4 "LTST-C191KGKT" H 16400 12400 50  0001 C CNN "MPN"
F 5 "Lite-On" H 16400 12400 50  0001 C CNN "Manufacturer"
F 6 "Rear-facing green status LED" H 16400 12400 50  0001 C CNN "Description"
	1    16400 12400
	1    0    0    -1
$EndComp
Text Label 15500 12350 0    40   ~ 0
STATUS_LED
Text Label 17300 12350 0    40   ~ 0
LED_A
$Comp
L PhotoFrame:TESTPOINT TP1
U 1 1 65030027
P 18500 10500
F 0 "TP1" H 18500 10250 50  0000 C CNN
F 1 "+5V" H 18500 10750 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 10500 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 10500 50  0001 C CNN
F 4 "5015" H 18500 10500 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 10500 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for +5V" H 18500 10500 50  0001 C CNN "Description"
	1    18500 10500
	1    0    0    -1
$EndComp
Text Label 17600 10450 0    40   ~ 0
+5V
$Comp
L PhotoFrame:TESTPOINT TP2
U 1 1 65030028
P 18500 10950
F 0 "TP2" H 18500 10700 50  0000 C CNN
F 1 "+3V3" H 18500 11200 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 10950 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 10950 50  0001 C CNN
F 4 "5015" H 18500 10950 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 10950 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for +3V3" H 18500 10950 50  0001 C CNN "Description"
	1    18500 10950
	1    0    0    -1
$EndComp
Text Label 17600 10900 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:TESTPOINT TP3
U 1 1 65030029
P 18500 11400
F 0 "TP3" H 18500 11150 50  0000 C CNN
F 1 "GND" H 18500 11650 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 11400 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 11400 50  0001 C CNN
F 4 "5015" H 18500 11400 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 11400 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for GND" H 18500 11400 50  0001 C CNN "Description"
	1    18500 11400
	1    0    0    -1
$EndComp
Text Label 17600 11350 0    40   ~ 0
GND
$Comp
L PhotoFrame:TESTPOINT TP4
U 1 1 6503002A
P 18500 11850
F 0 "TP4" H 18500 11600 50  0000 C CNN
F 1 "LCD_WR" H 18500 12100 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 11850 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 11850 50  0001 C CNN
F 4 "5015" H 18500 11850 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 11850 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for LCD_WR" H 18500 11850 50  0001 C CNN "Description"
	1    18500 11850
	1    0    0    -1
$EndComp
Text Label 17600 11800 0    40   ~ 0
LCD_WR
$Comp
L PhotoFrame:TESTPOINT TP5
U 1 1 6503002B
P 18500 12300
F 0 "TP5" H 18500 12050 50  0000 C CNN
F 1 "LCD_BL" H 18500 12550 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 12300 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 12300 50  0001 C CNN
F 4 "5015" H 18500 12300 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 12300 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for LCD_BL" H 18500 12300 50  0001 C CNN "Description"
	1    18500 12300
	1    0    0    -1
$EndComp
Text Label 17600 12250 0    40   ~ 0
LCD_BL
$Comp
L PhotoFrame:TESTPOINT TP6
U 1 1 6503002C
P 18500 12750
F 0 "TP6" H 18500 12500 50  0000 C CNN
F 1 "SD_CS" H 18500 13000 50  0000 C CNN
F 2 "TestPoint:TestPoint_Pad_D1.5mm" H 18500 12750 50  0001 C CNN
F 3 "https://www.keyelco.com/product.cfm/product_id/13981" H 18500 12750 50  0001 C CNN
F 4 "5015" H 18500 12750 50  0001 C CNN "MPN"
F 5 "Keystone Electronics" H 18500 12750 50  0001 C CNN "Manufacturer"
F 6 "Labeled test point for SD_CS" H 18500 12750 50  0001 C CNN "Description"
	1    18500 12750
	1    0    0    -1
$EndComp
Text Label 17600 12700 0    40   ~ 0
SD_CS
$Comp
L PhotoFrame:PWR_FLAG PF1
U 1 1 6503002D
P 2600 5200
F 0 "PF1" H 2600 4950 50  0000 C CNN
F 1 "PWR_FLAG" H 2600 5450 50  0000 C CNN
F 2 "" H 2600 5200 50  0001 C CNN
F 3 "" H 2600 5200 50  0001 C CNN
F 4 "" H 2600 5200 50  0001 C CNN "MPN"
F 5 "" H 2600 5200 50  0001 C CNN "Manufacturer"
F 6 "ERC power-driver marker" H 2600 5200 50  0001 C CNN "Description"
	1    2600 5200
	1    0    0    -1
$EndComp
Text Label 1700 5150 0    40   ~ 0
+5V
$Comp
L PhotoFrame:PWR_FLAG PF2
U 1 1 6503002E
P 2600 5900
F 0 "PF2" H 2600 5650 50  0000 C CNN
F 1 "PWR_FLAG" H 2600 6150 50  0000 C CNN
F 2 "" H 2600 5900 50  0001 C CNN
F 3 "" H 2600 5900 50  0001 C CNN
F 4 "" H 2600 5900 50  0001 C CNN "MPN"
F 5 "" H 2600 5900 50  0001 C CNN "Manufacturer"
F 6 "ERC power-driver marker" H 2600 5900 50  0001 C CNN "Description"
	1    2600 5900
	1    0    0    -1
$EndComp
Text Label 1700 5850 0    40   ~ 0
+3V3
$Comp
L PhotoFrame:PWR_FLAG PF3
U 1 1 6503002F
P 2600 6600
F 0 "PF3" H 2600 6350 50  0000 C CNN
F 1 "PWR_FLAG" H 2600 6850 50  0000 C CNN
F 2 "" H 2600 6600 50  0001 C CNN
F 3 "" H 2600 6600 50  0001 C CNN
F 4 "" H 2600 6600 50  0001 C CNN "MPN"
F 5 "" H 2600 6600 50  0001 C CNN "Manufacturer"
F 6 "ERC power-driver marker" H 2600 6600 50  0001 C CNN "Description"
	1    2600 6600
	1    0    0    -1
$EndComp
Text Label 1700 6550 0    40   ~ 0
GND
$Comp
L PhotoFrame:PWR_FLAG PF4
U 1 1 65030030
P 2600 7300
F 0 "PF4" H 2600 7050 50  0000 C CNN
F 1 "PWR_FLAG" H 2600 7550 50  0000 C CNN
F 2 "" H 2600 7300 50  0001 C CNN
F 3 "" H 2600 7300 50  0001 C CNN
F 4 "" H 2600 7300 50  0001 C CNN "MPN"
F 5 "" H 2600 7300 50  0001 C CNN "Manufacturer"
F 6 "ERC power-driver marker" H 2600 7300 50  0001 C CNN "Description"
	1    2600 7300
	1    0    0    -1
$EndComp
Text Label 1700 7250 0    40   ~ 0
+5V_RAW
$EndSCHEMATC
