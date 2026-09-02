# Selected exact parts and manufacturer sources

These are the BOM selections embedded in the KiCad schematic. Availability,
life-cycle status, distributor stock and the display's orderable configuration
suffix were not verified; no purchasing claim is made.

| Function | Manufacturer / exact MPN | Package/footprint | Manufacturer source | Local source receipt |
|---|---|---|---|---|
| Display | EastRising ER-TFTM070-4V3, 5 V, 8-bit 8080, no-touch configuration | Module, 2x20 2.54 mm header | https://www.buydisplay.com/download/manual/ER-TFTM070-4V3_Datasheet.pdf | Direct download rejected; URL and rejection receipt retained |
| MCU module | Espressif ESP32-S3-WROOM-1-N16R8 | ESP32-S3-WROOM-1 | https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf | PDF saved |
| 3.3 V buck | Texas Instruments TPS62132RGTR | VQFN-16, 3 x 3 mm, exposed pad | https://www.ti.com/lit/ds/symlink/tps62132.pdf | TPS6213x family PDF saved |
| USB-C receptacle | GCT USB4105-GF-A | 16-position horizontal top mount | https://gct.co/files/drawings/usb4105.pdf | drawing and product specification saved |
| microSD socket | Molex 104031-0811 | Molex 104031 footprint | https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/104/104031/PS-104031-001-001.pdf | direct download unavailable |
| Ambient sensor | Lite-On LTR-303ALS-01 | 2 x 2 mm six-pin optical package | https://optoelectronics.liteon.com/upload/download/DS86-2013-0004/LTR-303ALS-01_DS_V1.1.PDF | request-rejection HTML retained, not mislabeled as PDF |
| USB ESD | STMicroelectronics USBLC6-2SC6 | SOT-23-6 | https://www.st.com/resource/en/datasheet/usblc6-2.pdf | direct download unavailable |
| Input PTC | Bourns MF-MSMF200-2 | 1206 | https://www.bourns.com/docs/product-datasheets/mf-msmf.pdf | URL in BOM |
| 5 V TVS | Littelfuse SMAJ5.0A | SMA | https://www.littelfuse.com/assetdocs/littelfuse-tvs-diode-smaj-datasheet | URL in BOM |
| Buck inductor | Coilcraft XAL4020-102MEC | XAL4020 | https://www.coilcraft.com/getmedia/5e5308cc-2480-4f52-be4a-cbbfc5c2eb1f/xal4020.pdf | URL in BOM |
| User/reset/boot switches | C&K KMR221GLFS | KMR2 SMD | https://www.ckswitches.com/media/1479/kmr2.pdf | URL in BOM |
| Status LED | Lite-On LTST-C191KGKT | 0603 | https://optoelectronics.liteon.com/upload/download/DS22-2000-228/LTST-C191KGKT.pdf | URL in BOM |
| Debug header | Harwin M20-9990646 | 1x6, 2.54 mm | https://cdn.harwin.com/pdfs/M20-999.pdf | URL in BOM |

The generated schematic BOM also fixes Murata capacitor and Yageo resistor MPNs
and Keystone 5015 test points. See `models/kicad/exports/photo_frame_bom.csv` for
the complete exact-part table and datasheet links.

## Display dimensional and pinout source facts used

- Resolution 800 x 480; SSD1963 controller; landscape module.
- Module outer envelope 180 x 100 mm; documented maximum thickness 12.8 mm.
- Active area 154.08 x 85.92 mm.
- Four 3.2 mm mounting holes on 174 x 98 mm centres.
- Maximum module current used for the budget: 480 mA at 5 V.
- Pin map: 1 GND, 2 5V, 3 /CS, 4 D/C, 5 /RD, 6 /WR, 7 RESET,
  8 TE, 9-32 DB0-DB23, 33-38 touch-related, 39 BL_ON/OFF/PWM, 40 NC.

The base MPN does not encode every selectable factory interface/no-touch option.
An order must quote and confirm the exact 5 V, 8-bit 8080, no-touch, pin-header
configuration with EastRising before procurement. That is an unresolved
ordering assumption, not an invented suffix.
