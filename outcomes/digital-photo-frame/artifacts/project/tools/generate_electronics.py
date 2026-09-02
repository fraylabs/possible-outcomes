#!/usr/bin/env python3
"""Generate the KiCad authority for the cleanroom photo-frame experiment.

The schematic is first emitted in KiCad's deterministic legacy text format and
then upgraded by kicad-cli.  The board is generated through KiCad's bundled
pcbnew Python API.  Both are driven by the same component/pad/net table below.
"""

from __future__ import annotations

import json
import math
import os
import shutil
import subprocess
import sys
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import pcbnew


ROOT = Path(__file__).resolve().parents[1]
KICAD_DIR = ROOT / "models" / "kicad" / "source"
LEGACY_SCH = KICAD_DIR / "photo_frame_legacy.sch"
SCH = KICAD_DIR / "photo_frame.kicad_sch"
PCB = KICAD_DIR / "photo_frame.kicad_pcb"
PRO = KICAD_DIR / "photo_frame.kicad_pro"
LIB = KICAD_DIR / "PhotoFrame.lib"
DCM = KICAD_DIR / "PhotoFrame.dcm"
KICAD_CLI = Path("/opt/homebrew/Caskroom/kicad/10.0.6/KiCad/KiCad.app/Contents/MacOS/kicad-cli")
SHARED = Path("/opt/homebrew/Caskroom/kicad/10.0.6/KiCad/KiCad.app/Contents/SharedSupport")


@dataclass(frozen=True)
class Pin:
    number: str
    name: str
    etype: str = "P"
    side: str = "L"


@dataclass
class SymbolDef:
    name: str
    pins: list[Pin]


@dataclass
class Component:
    ref: str
    symbol: str
    value: str
    footprint: str
    datasheet: str
    manufacturer: str
    mpn: str
    description: str
    nets: dict[str, str | None]
    sch_pos: tuple[int, int]
    pcb_pos: tuple[float, float]
    pcb_angle: float = 0.0
    board_only: bool = False


def pins_lr(entries: list[tuple[str, str, str]]) -> list[Pin]:
    midpoint = math.ceil(len(entries) / 2)
    return [
        Pin(number, name, etype, "L" if index < midpoint else "R")
        for index, (number, name, etype) in enumerate(entries)
    ]


SYMBOLS: dict[str, SymbolDef] = {}


def add_symbol(name: str, entries: list[tuple[str, str, str]]) -> None:
    SYMBOLS[name] = SymbolDef(name, pins_lr(entries))


add_symbol("R_EXACT", [("1", "1", "P"), ("2", "2", "P")])
add_symbol("C_EXACT", [("1", "1", "P"), ("2", "2", "P")])
add_symbol("L_EXACT", [("1", "1", "P"), ("2", "2", "P")])
add_symbol("FUSE_EXACT", [("1", "1", "P"), ("2", "2", "P")])
add_symbol("DIODE_EXACT", [("1", "K", "P"), ("2", "A", "P")])
add_symbol("LED_EXACT", [("1", "K", "P"), ("2", "A", "P")])
add_symbol("SW_KMR2", [("1", "A", "P"), ("2", "B", "P"), ("SH", "SHIELD", "P")])
add_symbol("TESTPOINT", [("1", "TP", "P")])
add_symbol("PWR_FLAG", [("1", "PWR", "w")])

add_symbol(
    "ESP32_S3_WROOM_1_N16R8",
    [
        ("1", "GND", "W"), ("2", "3V3", "W"), ("3", "EN", "I"),
        ("4", "IO4", "B"), ("5", "IO5", "B"), ("6", "IO6", "B"),
        ("7", "IO7", "B"), ("8", "IO15", "B"), ("9", "IO16", "B"),
        ("10", "IO17", "B"), ("11", "IO18", "B"), ("12", "IO8", "B"),
        ("13", "USB_D-", "B"), ("14", "USB_D+", "B"), ("15", "IO3", "B"),
        ("16", "IO46", "B"), ("17", "IO9", "B"), ("18", "IO10", "B"),
        ("19", "IO11", "B"), ("20", "IO12", "B"), ("21", "IO13", "B"),
        ("22", "IO14", "B"), ("23", "IO21", "B"), ("24", "IO47", "B"),
        ("25", "IO48", "B"), ("26", "IO45", "B"), ("27", "IO0", "B"),
        ("28", "IO35", "B"), ("29", "IO36", "B"), ("30", "IO37", "B"),
        ("31", "IO38", "B"), ("32", "IO39", "B"), ("33", "IO40", "B"),
        ("34", "IO41", "B"), ("35", "IO42", "B"), ("36", "RXD0", "B"),
        ("37", "TXD0", "B"), ("38", "IO2", "B"), ("39", "IO1", "B"),
        ("40", "GND", "W"), ("41", "EP_GND", "W"),
    ],
)

add_symbol(
    "ER_TFTM070_4V3",
    [
        ("1", "GND", "W"), ("2", "VDD5V", "W"), ("3", "~CS", "I"),
        ("4", "D_C", "I"), ("5", "~RD", "I"), ("6", "~WR", "I"),
        ("7", "RESET", "I"), ("8", "TE", "O"),
        *[(str(9 + i), f"DB{i}", "B") for i in range(24)],
        ("33", "TP_SCL", "B"), ("34", "TP_CS", "B"), ("35", "TP_SDA", "B"),
        ("36", "TP_DOUT", "B"), ("37", "TP_INT", "B"), ("38", "TP_GND", "W"),
        ("39", "BL_ON_PWM", "I"), ("40", "NC", "N"),
    ],
)

add_symbol(
    "TPS62132RGTR",
    [
        ("1", "SW", "O"), ("2", "SW", "P"), ("3", "SW", "P"),
        ("4", "PG", "C"), ("5", "FB_NC", "N"), ("6", "GND", "W"),
        ("7", "FSW", "I"), ("8", "DEF", "I"), ("9", "SS_TR", "I"),
        ("10", "VIN", "W"), ("11", "VIN", "P"), ("12", "VIN", "P"),
        ("13", "EN", "I"), ("14", "VOS", "I"), ("15", "GND", "W"),
        ("16", "GND", "W"), ("17", "EP_GND", "W"),
    ],
)

add_symbol(
    "USB4105_GF_A",
    [
        ("A1", "GND", "W"), ("A4", "VBUS", "P"), ("A5", "CC1", "B"),
        ("A6", "D+", "B"), ("A7", "D-", "B"), ("A8", "SBU1", "B"),
        ("A9", "VBUS", "P"), ("A12", "GND", "W"),
        ("B1", "GND", "W"), ("B4", "VBUS", "P"), ("B5", "CC2", "B"),
        ("B6", "D+", "B"), ("B7", "D-", "B"), ("B8", "SBU2", "B"),
        ("B9", "VBUS", "P"), ("B12", "GND", "W"), ("SH", "SHIELD", "P"),
    ],
)

add_symbol(
    "USBLC6_2SC6",
    [("1", "IO1A", "P"), ("2", "GND", "W"), ("3", "IO2A", "P"),
     ("4", "IO2B", "P"), ("5", "VBUS", "W"), ("6", "IO1B", "P")],
)

add_symbol(
    "MICROSD_104031_0811",
    [("1", "DAT2", "B"), ("2", "DAT3_CS", "B"), ("3", "CMD_DI", "I"),
     ("4", "VDD", "W"), ("5", "CLK", "I"), ("6", "VSS", "W"),
     ("7", "DAT0_DO", "O"), ("8", "DAT1", "B"), ("9", "CD", "P"),
     ("10", "CD_COMMON", "P"), ("SH", "SHIELD", "P")],
)

add_symbol(
    "LTR_303ALS_01",
    [("1", "VDD", "W"), ("2", "NC", "N"), ("3", "GND", "W"),
     ("4", "SCL", "I"), ("5", "INT", "C"), ("6", "SDA", "B")],
)

add_symbol(
    "HEADER_1X6",
    [(str(i), name, "P") for i, name in enumerate(["3V3", "GND", "USB_D+", "USB_D-", "TX", "RX"], 1)],
)


COMPONENTS: list[Component] = []


def comp(**kwargs) -> None:
    COMPONENTS.append(Component(**kwargs))


URL_DISPLAY = "https://www.buydisplay.com/download/manual/ER-TFTM070-4V3_Datasheet.pdf"
URL_ESP = "https://www.espressif.com/sites/default/files/documentation/esp32-s3-wroom-1_wroom-1u_datasheet_en.pdf"
URL_TPS = "https://www.ti.com/lit/ds/symlink/tps62132.pdf"


# Power input and protection.
comp(ref="J1", symbol="USB4105_GF_A", value="USB4105-GF-A", footprint="Connector_USB:USB_C_Receptacle_GCT_USB4105-xx-A_16P_TopMnt_Horizontal", datasheet="https://gct.co/files/drawings/usb4105.pdf", manufacturer="GCT", mpn="USB4105-GF-A", description="USB-C 16-position receptacle; power-only sink", nets={"A1":"GND","A4":"+5V_RAW","A5":"CC1","A6":None,"A7":None,"A8":None,"A9":"+5V_RAW","A12":"GND","B1":"GND","B4":"+5V_RAW","B5":"CC2","B6":None,"B7":None,"B8":None,"B9":"+5V_RAW","B12":"GND","SH":"GND"}, sch_pos=(2800,2600), pcb_pos=(130,32), pcb_angle=90)
comp(ref="R1", symbol="R_EXACT", value="5.1k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-075K1L", description="USB-C CC1 Rd sink resistor", nets={"1":"CC1","2":"GND"}, sch_pos=(4300,2200), pcb_pos=(119,25))
comp(ref="R2", symbol="R_EXACT", value="5.1k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-075K1L", description="USB-C CC2 Rd sink resistor", nets={"1":"CC2","2":"GND"}, sch_pos=(4300,3000), pcb_pos=(119,28))
comp(ref="U4", symbol="USBLC6_2SC6", value="USBLC6-2SC6", footprint="Package_TO_SOT_SMD:SOT-23-6", datasheet="https://www.st.com/resource/en/datasheet/usblc6-2.pdf", manufacturer="STMicroelectronics", mpn="USBLC6-2SC6", description="ESD protection for both USB-C CC pins and VBUS reference", nets={"1":"CC1","2":"GND","3":"CC2","4":"CC2","5":"+5V_RAW","6":"CC1"}, sch_pos=(5300,2600), pcb_pos=(114,31))
comp(ref="F1", symbol="FUSE_EXACT", value="2.0A resettable", footprint="Fuse:Fuse_1206_3216Metric", datasheet="https://www.bourns.com/docs/product-datasheets/mf-msmf.pdf", manufacturer="Bourns", mpn="MF-MSMF200-2", description="Resettable input current limiter", nets={"1":"+5V_RAW","2":"+5V"}, sch_pos=(6500,2600), pcb_pos=(108,30))
comp(ref="D1", symbol="DIODE_EXACT", value="SMAJ5.0A", footprint="Diode_SMD:D_SMA", datasheet="https://www.littelfuse.com/assetdocs/littelfuse-tvs-diode-smaj-datasheet", manufacturer="Littelfuse", mpn="SMAJ5.0A", description="Unidirectional 5 V rail TVS", nets={"1":"+5V","2":"GND"}, sch_pos=(7600,2600), pcb_pos=(102,29))
comp(ref="C1", symbol="C_EXACT", value="22uF 10V X5R", footprint="Capacitor_SMD:C_0805_2012Metric", datasheet="https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A226ME44-01.pdf", manufacturer="Murata", mpn="GRM21BR61A226ME44L", description="Protected 5 V bulk capacitor; 10 V rating", nets={"1":"+5V","2":"GND"}, sch_pos=(8500,2600), pcb_pos=(98,29))

# 3.3 V converter and local energy storage.
comp(ref="U2", symbol="TPS62132RGTR", value="TPS62132RGTR 3.3V", footprint="Package_DFN_QFN:VQFN-16-1EP_3x3mm_P0.5mm_EP1.68x1.68mm_ThermalVias", datasheet=URL_TPS, manufacturer="Texas Instruments", mpn="TPS62132RGTR", description="3 A fixed 3.3 V synchronous buck", nets={"1":"SW","2":"SW","3":"SW","4":"PGOOD","5":None,"6":"GND","7":"GND","8":"GND","9":"SS","10":"+5V","11":"+5V","12":"+5V","13":"+5V","14":"+3V3","15":"GND","16":"GND","17":"GND"}, sch_pos=(5200,4800), pcb_pos=(45,39))
comp(ref="L1", symbol="L_EXACT", value="1.0uH 20%", footprint="Inductor_SMD:L_Bourns-SRU8028_8.0x8.0mm", datasheet="https://www.coilcraft.com/getmedia/5e5308cc-2480-4f52-be4a-cbbfc5c2eb1f/xal4020.pdf", manufacturer="Coilcraft", mpn="XAL4020-102MEC", description="Shielded buck inductor; Isat 7.6 A", nets={"1":"SW","2":"+3V3"}, sch_pos=(6800,4400), pcb_pos=(52,39))
comp(ref="C2", symbol="C_EXACT", value="10nF 25V X7R", footprint="Capacitor_SMD:C_0603_1608Metric", datasheet="https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM188R71E103KA01-01.pdf", manufacturer="Murata", mpn="GRM188R71E103KA01D", description="Buck soft-start capacitor", nets={"1":"SS","2":"GND"}, sch_pos=(6500,5200), pcb_pos=(47,44))
for ref, pos in [("C3",(58,37)),("C4",(58,41))]:
    comp(ref=ref, symbol="C_EXACT", value="22uF 10V X5R", footprint="Capacitor_SMD:C_0805_2012Metric", datasheet="https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A226ME44-01.pdf", manufacturer="Murata", mpn="GRM21BR61A226ME44L", description="3.3 V output capacitor; 10 V rating", nets={"1":"+3V3","2":"GND"}, sch_pos=(7600,4600 if ref=="C3" else 5200), pcb_pos=pos)
comp(ref="C5", symbol="C_EXACT", value="10uF 10V X5R", footprint="Capacitor_SMD:C_0805_2012Metric", datasheet="https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM21BR61A106KE19-01.pdf", manufacturer="Murata", mpn="GRM21BR61A106KE19L", description="Buck input capacitor", nets={"1":"+5V","2":"GND"}, sch_pos=(7600,5800), pcb_pos=(39,39))
comp(ref="R3", symbol="R_EXACT", value="100k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-07100KL", description="Power-good pull-up", nets={"1":"PGOOD","2":"+3V3"}, sch_pos=(6500,5800), pcb_pos=(48,35))

# Processor and required boot, reset, decoupling, debug.
u1_nets = {"1":"GND","2":"+3V3","3":"EN","4":"SD_CS","5":"SD_MISO","6":"SD_MOSI","7":"SD_SCK","8":"SD_CD","9":"BTN_PREV","10":"BTN_NEXT","11":"BTN_MENU","12":"STATUS_LED","13":"USB_D-","14":"USB_D+","15":"ALS_INT","16":"STRAP46","17":"I2C_SCL","18":"I2C_SDA","19":"LCD_BL","20":"LCD_TE","21":"LCD_RST","22":"LCD_CS","23":"LCD_DC","24":"LCD_WR","25":"LCD_RD","26":"STRAP45","27":"BOOT","28":"LCD_D0","29":"LCD_D1","30":"LCD_D2","31":"LCD_D3","32":"LCD_D4","33":"LCD_D5","34":"LCD_D6","35":"LCD_D7","36":"U0RXD","37":"U0TXD","38":None,"39":None,"40":"GND","41":"GND"}
comp(ref="U1", symbol="ESP32_S3_WROOM_1_N16R8", value="ESP32-S3-WROOM-1-N16R8", footprint="RF_Module:ESP32-S3-WROOM-1", datasheet=URL_ESP, manufacturer="Espressif Systems", mpn="ESP32-S3-WROOM-1-N16R8", description="Wi-Fi MCU module; 16 MB flash and 8 MB octal PSRAM", nets=u1_nets, sch_pos=(11200,6500), pcb_pos=(82,51))
for ref, value, mpn, pos, sy in [("C6","10uF 10V X5R","GRM21BR61A106KE19L",(70,45),5200),("C7","100nF 16V X7R","GRM188R71C104KA01D",(70,49),5700)]:
    comp(ref=ref, symbol="C_EXACT", value=value, footprint="Capacitor_SMD:C_0603_1608Metric" if ref=="C7" else "Capacitor_SMD:C_0805_2012Metric", datasheet="https://search.murata.co.jp/Ceramy/owa/CATALOG.showcatalog", manufacturer="Murata", mpn=mpn, description="ESP32 local decoupling", nets={"1":"+3V3","2":"GND"}, sch_pos=(9200,sy), pcb_pos=pos)
for ref, net, other, desc, spos, ppos in [
    ("R4","EN","+3V3","ESP32 enable pull-up",(9200,6400),(69,53)),
    ("R5","BOOT","+3V3","ESP32 GPIO0 boot pull-up",(9200,7000),(69,57)),
    ("R6","STRAP45","GND","GPIO45 strap pull-down for 3.3 V VDD_SPI",(9200,7600),(69,61)),
    ("R7","STRAP46","GND","GPIO46 strap pull-down for normal boot",(9200,8200),(69,65)),
]:
    comp(ref=ref, symbol="R_EXACT", value="10k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-0710KL", description=desc, nets={"1":net,"2":other}, sch_pos=spos, pcb_pos=ppos)
for ref, net, desc, spos, ppos in [
    ("SW4","EN","Reset access",(9200,8800),(48,64)),
    ("SW5","BOOT","Bootloader access",(9200,9400),(56,64)),
]:
    comp(ref=ref, symbol="SW_KMR2", value="KMR221GLFS", footprint="Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG", datasheet="https://www.ckswitches.com/media/1479/kmr2.pdf", manufacturer="C&K", mpn="KMR221GLFS", description=desc, nets={"1":net,"2":"GND","SH":"GND"}, sch_pos=spos, pcb_pos=ppos)
comp(ref="J4", symbol="HEADER_1X6", value="DEBUG 1x6", footprint="Connector_PinHeader_2.54mm:PinHeader_1x06_P2.54mm_Vertical", datasheet="https://cdn.harwin.com/pdfs/M20-999.pdf", manufacturer="Harwin", mpn="M20-9990646", description="Internal programming and debug header", nets={"1":"+3V3","2":"GND","3":"USB_D+","4":"USB_D-","5":"U0TXD","6":"U0RXD"}, sch_pos=(9200,10400), pcb_pos=(39,74))

# Display interface.  DB8..DB23 and touch pins are intentionally NC for the selected no-touch 8-bit build.
j2_nets: dict[str, str | None] = {"1":"GND","2":"+5V","3":"LCD_CS","4":"LCD_DC","5":"LCD_RD","6":"LCD_WR","7":"LCD_RST","8":"LCD_TE"}
j2_nets.update({str(9+i): f"LCD_D{i}" if i < 8 else None for i in range(24)})
j2_nets.update({"33":None,"34":None,"35":None,"36":None,"37":None,"38":None,"39":"LCD_BL","40":None})
comp(ref="J2", symbol="ER_TFTM070_4V3", value="ER-TFTM070-4V3 8-bit 8080 5V no-touch", footprint="Connector_PinHeader_2.54mm:PinHeader_2x20_P2.54mm_Vertical", datasheet=URL_DISPLAY, manufacturer="EastRising", mpn="ER-TFTM070-4V3", description="7-inch 800x480 SSD1963 display module; pin-header configuration", nets=j2_nets, sch_pos=(17400,6500), pcb_pos=(118,84), pcb_angle=90)

# Storage, buttons, sensor, and status indication.
comp(ref="J3", symbol="MICROSD_104031_0811", value="104031-0811", footprint="Connector_Card:microSD_HC_Molex_104031-0811", datasheet="https://www.molex.com/content/dam/molex/molex-dot-com/products/automated/en-us/productspecificationpdf/104/104031/PS-104031-001-001.pdf", manufacturer="Molex", mpn="104031-0811", description="Push-pull microSD socket with detect switch", nets={"1":None,"2":"SD_CS","3":"SD_MOSI","4":"+3V3","5":"SD_SCK","6":"GND","7":"SD_MISO","8":None,"9":"SD_CD","10":"GND","SH":"GND"}, sch_pos=(13200,11200), pcb_pos=(126,70), pcb_angle=90)
comp(ref="R8", symbol="R_EXACT", value="10k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-0710KL", description="microSD card-detect pull-up", nets={"1":"SD_CD","2":"+3V3"}, sch_pos=(14500,11200), pcb_pos=(116,67))
comp(ref="U3", symbol="LTR_303ALS_01", value="LTR-303ALS-01", footprint="OptoDevice:Lite-On_LTR-303ALS-01", datasheet="https://optoelectronics.liteon.com/upload/download/DS86-2013-0004/LTR-303ALS-01_DS_V1.1.PDF", manufacturer="Lite-On", mpn="LTR-303ALS-01", description="I2C ambient-light sensor", nets={"1":"+3V3","2":None,"3":"GND","4":"I2C_SCL","5":"ALS_INT","6":"I2C_SDA"}, sch_pos=(7800,11200), pcb_pos=(63,80))
for ref, net, spos, ppos in [("R9","I2C_SCL",(6400,10800),(59,76)),("R10","I2C_SDA",(6400,11400),(63,76))]:
    comp(ref=ref, symbol="R_EXACT", value="4.7k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-074K7L", description="I2C pull-up", nets={"1":net,"2":"+3V3"}, sch_pos=spos, pcb_pos=ppos)
comp(ref="C8", symbol="C_EXACT", value="100nF 16V X7R", footprint="Capacitor_SMD:C_0603_1608Metric", datasheet="https://search.murata.co.jp/Ceramy/image/img/PDF/ENG/GRM188R71C104KA01-01.pdf", manufacturer="Murata", mpn="GRM188R71C104KA01D", description="Ambient sensor decoupling", nets={"1":"+3V3","2":"GND"}, sch_pos=(9000,11200), pcb_pos=(67,80))
for idx, (ref, net, y, x) in enumerate([("SW1","BTN_PREV",12400,86),("SW2","BTN_NEXT",13200,96),("SW3","BTN_MENU",14000,106)]):
    comp(ref=ref, symbol="SW_KMR2", value="KMR221GLFS", footprint="Button_Switch_SMD:SW_Push_1P1T-SH_NO_CK_KMR2xxG", datasheet="https://www.ckswitches.com/media/1479/kmr2.pdf", manufacturer="C&K", mpn="KMR221GLFS", description=["Previous button","Next button","Menu/wake button"][idx], nets={"1":net,"2":"GND","SH":"GND"}, sch_pos=(10200,y), pcb_pos=(x,74))
    comp(ref=f"R{11+idx}", symbol="R_EXACT", value="10k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-0710KL", description="User-button pull-up", nets={"1":net,"2":"+3V3"}, sch_pos=(11600,y), pcb_pos=(x,69))
comp(ref="R14", symbol="R_EXACT", value="1.0k 1%", footprint="Resistor_SMD:R_0603_1608Metric", datasheet="https://www.yageo.com/upload/media/product/productsearch/datasheet/rchip/PYu-RC_Group_51_RoHS_L_13.pdf", manufacturer="Yageo", mpn="RC0603FR-071KL", description="Status LED current limit", nets={"1":"+3V3","2":"LED_A"}, sch_pos=(15000,12400), pcb_pos=(71,76))
comp(ref="LED1", symbol="LED_EXACT", value="LTST-C191KGKT green", footprint="LED_SMD:LED_0603_1608Metric", datasheet="https://optoelectronics.liteon.com/upload/download/DS22-2000-228/LTST-C191KGKT.pdf", manufacturer="Lite-On", mpn="LTST-C191KGKT", description="Rear-facing green status LED", nets={"1":"STATUS_LED","2":"LED_A"}, sch_pos=(16400,12400), pcb_pos=(75,76))

# Labeled measurement points.  They are intentionally included in schematic parity and BOM-excluded later if desired.
for idx, (ref, net, pos) in enumerate([("TP1","+5V",(29,50)),("TP2","+3V3",(34,50)),("TP3","GND",(39,50)),("TP4","LCD_WR",(112,60)),("TP5","LCD_BL",(112,64)),("TP6","SD_CS",(112,68))]):
    comp(ref=ref, symbol="TESTPOINT", value=net, footprint="TestPoint:TestPoint_Pad_D1.5mm", datasheet="https://www.keyelco.com/product.cfm/product_id/13981", manufacturer="Keystone Electronics", mpn="5015", description=f"Labeled test point for {net}", nets={"1":net}, sch_pos=(18500,10500 + idx*450), pcb_pos=pos)

# ERC power drivers.
for idx, (ref, net, pos) in enumerate([("PF1","+5V",(2600,5200)),("PF2","+3V3",(2600,5900)),("PF3","GND",(2600,6600)),("PF4","+5V_RAW",(2600,7300))]):
    comp(ref=ref, symbol="PWR_FLAG", value="PWR_FLAG", footprint="", datasheet="", manufacturer="", mpn="", description="ERC power-driver marker", nets={"1":net}, sch_pos=pos, pcb_pos=(0,0), board_only=False)


def library_symbol_text(symbol: SymbolDef) -> str:
    count_left = sum(pin.side == "L" for pin in symbol.pins)
    count_right = len(symbol.pins) - count_left
    height = max(count_left, count_right, 2) * 100 + 300
    top = height // 2
    bottom = -top
    lines = [
        f"# {symbol.name}", f"#", f"DEF {symbol.name} U 0 40 Y Y 1 F N",
        'F0 "U" 0 150 50 H V C CNN', f'F1 "{symbol.name}" 0 -150 50 H V C CNN',
        "DRAW", f"S -700 {bottom} 700 {top} 0 1 12 f",
    ]
    left_index = 0
    right_index = 0
    for pin in symbol.pins:
        if pin.side == "L":
            y = top - 200 - left_index * 100
            left_index += 1
            x, orient = -900, "R"
        else:
            y = top - 200 - right_index * 100
            right_index += 1
            x, orient = 900, "L"
        lines.append(f"X {pin.name} {pin.number} {x} {y} 200 {orient} 45 45 1 1 {pin.etype}")
    lines += ["ENDDRAW", "ENDDEF"]
    return "\n".join(lines)


def write_library() -> None:
    content = ["EESchema-LIBRARY Version 2.4", "#encoding utf-8"]
    for symbol in SYMBOLS.values():
        content.append(library_symbol_text(symbol))
    content += ["#End Library", ""]
    LIB.write_text("\n".join(content), encoding="utf-8")
    DCM.write_text("EESchema-DOCLIB  Version 2.0\n#End Doc Library\n", encoding="utf-8")
    (KICAD_DIR / "sym-lib-table").write_text(
        '(sym_lib_table\n  (lib (name "PhotoFrame")(type "Legacy")(uri "${KIPRJMOD}/PhotoFrame.lib")(options "")(descr "Cleanroom project symbols"))\n)\n',
        encoding="utf-8",
    )


def symbol_pin_positions(symbol: SymbolDef) -> dict[str, tuple[int, int]]:
    count_left = sum(pin.side == "L" for pin in symbol.pins)
    count_right = len(symbol.pins) - count_left
    height = max(count_left, count_right, 2) * 100 + 300
    top = height // 2
    left_index = right_index = 0
    result = {}
    for pin in symbol.pins:
        if pin.side == "L":
            result[pin.number] = (-900, top - 200 - left_index * 100)
            left_index += 1
        else:
            result[pin.number] = (900, top - 200 - right_index * 100)
            right_index += 1
    return result


def emit_component(component: Component, timestamp: int) -> list[str]:
    x, y = component.sch_pos
    lines = [
        "$Comp", f"L PhotoFrame:{component.symbol} {component.ref}", f"U 1 1 {timestamp:08X}", f"P {x} {y}",
        f'F 0 "{component.ref}" H {x} {y-250} 50  0000 C CNN',
        f'F 1 "{component.value}" H {x} {y+250} 50  0000 C CNN',
        f'F 2 "{component.footprint}" H {x} {y} 50  0001 C CNN',
        f'F 3 "{component.datasheet}" H {x} {y} 50  0001 C CNN',
        f'F 4 "{component.mpn}" H {x} {y} 50  0001 C CNN "MPN"',
        f'F 5 "{component.manufacturer}" H {x} {y} 50  0001 C CNN "Manufacturer"',
        f'F 6 "{component.description}" H {x} {y} 50  0001 C CNN "Description"',
        f"\t1    {x} {y}", "\t1    0    0    -1", "$EndComp",
    ]
    pin_positions = symbol_pin_positions(SYMBOLS[component.symbol])
    for number, net in component.nets.items():
        if number not in pin_positions:
            continue
        px, py = pin_positions[number]
        ax, ay = x + px, y - py
        if net is None:
            lines.append(f"NoConn ~ {ax} {ay}")
        else:
            lines += [f"Text Label {ax} {ay} 0    40   ~ 0", net]
    return lines


def write_legacy_schematic() -> None:
    lines = [
        "EESchema Schematic File Version 4", "LIBS:PhotoFrame", "EELAYER 29 0", "EELAYER END",
        "$Descr A2 23386 16535", "encoding utf-8", "Sheet 1 1",
        'Title "Seven-inch Digital Photo Frame Controller"', 'Date "2026-09-03"', 'Rev "A / DIGITAL PRE-BUILD"',
        'Comp "Cleanroom Burr experiment — not production ready"', 'Comment1 "ESP32-S3 + SSD1963 8-bit 8080 display"',
        'Comment2 "External certified 5 V USB-C adapter only"', 'Comment3 "Touch, audio, camera, and battery omitted by definition"',
        'Comment4 "Exact parts and assumptions in reports"', "$EndDescr",
        "Text Notes 1800 1200 0    120  ~ 24", "POWER INPUT / PROTECTION / 3V3",
        "Text Notes 9300 1200 0    120  ~ 24", "ESP32-S3 CONTROLLER / DEBUG",
        "Text Notes 15800 1200 0    120  ~ 24", "DISPLAY — 8-BIT 8080, NO TOUCH",
        "Text Notes 5000 10100 0    120  ~ 24", "STORAGE / CONTROLS / AMBIENT LIGHT",
    ]
    timestamp = 0x65030000
    for index, component in enumerate(COMPONENTS):
        lines.extend(emit_component(component, timestamp + index))
    lines += ["$EndSCHEMATC", ""]
    LEGACY_SCH.write_text("\n".join(lines), encoding="utf-8")


def deterministic_uuid(name: str) -> str:
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"fray-cleanroom-photo-frame-v2/{name}"))


def write_modern_schematic() -> None:
    """Write a native KiCad schematic and project-local symbol library with kiutils."""
    sys.path.insert(0, str(ROOT / ".venv" / "lib" / "python3.12" / "site-packages"))
    from kiutils.schematic import Schematic
    from kiutils.symbol import Symbol, SymbolLib, SymbolPin
    from kiutils.items.common import Effects, Fill, Font, PageSettings, Position, Property, Stroke, TitleBlock
    from kiutils.items.schitems import LocalLabel, NoConnect, SchematicSymbol, SymbolProjectInstance, SymbolProjectPath, Text
    from kiutils.items.syitems import SyRect

    etypes = {
        "I": "input", "O": "output", "B": "bidirectional", "T": "tri_state",
        "P": "passive", "U": "free", "W": "power_in", "w": "power_out",
        "C": "open_collector", "N": "no_connect",
    }

    lib_defs: dict[str, Symbol] = {}
    pin_locations_mm: dict[str, dict[str, tuple[float, float]]] = {}
    for name, definition in SYMBOLS.items():
        parent = Symbol.create_new(f"PhotoFrame:{name}", "U", name)
        parent.pinNames = True
        parent.pinNamesOffset = 1.27
        parent.inBom = True
        parent.onBoard = True
        unit = Symbol()
        unit.libId = f"{name}_1_1"
        count_left = sum(pin.side == "L" for pin in definition.pins)
        count_right = len(definition.pins) - count_left
        height_mil = max(count_left, count_right, 2) * 100 + 300
        top_mm = height_mil / 2 * 0.0254
        bottom_mm = -top_mm
        unit.graphicItems.append(SyRect(
            start=Position(-17.78, bottom_mm), end=Position(17.78, top_mm),
            stroke=Stroke(width=0.3, type="default"), fill=Fill(type="background"),
        ))
        left_index = right_index = 0
        locations: dict[str, tuple[float, float]] = {}
        for pin in definition.pins:
            if pin.side == "L":
                y_mm = (height_mil / 2 - 200 - left_index * 100) * 0.0254
                left_index += 1
                x_mm, angle = -22.86, 0
            else:
                y_mm = (height_mil / 2 - 200 - right_index * 100) * 0.0254
                right_index += 1
                x_mm, angle = 22.86, 180
            locations[pin.number] = (x_mm, y_mm)
            unit.pins.append(SymbolPin(
                electricalType=etypes[pin.etype], graphicalStyle="line",
                position=Position(x_mm, y_mm, angle), length=5.08,
                name=pin.name, number=pin.number,
                nameEffects=Effects(font=Font(width=1.0, height=1.0)),
                numberEffects=Effects(font=Font(width=0.9, height=0.9)),
            ))
        parent.units.append(unit)
        lib_defs[name] = parent
        pin_locations_mm[name] = locations

    symbol_lib = SymbolLib(generator="fray_cleanroom_generator")
    symbol_lib.symbols = list(lib_defs.values())
    symbol_lib.to_file(str(KICAD_DIR / "PhotoFrame.kicad_sym"), encoding="utf-8")
    (KICAD_DIR / "sym-lib-table").write_text(
        '(sym_lib_table\n  (lib (name "PhotoFrame")(type "KiCad")(uri "${KIPRJMOD}/PhotoFrame.kicad_sym")(options "")(descr "Cleanroom project symbols"))\n)\n',
        encoding="utf-8",
    )

    schematic = Schematic.create_new()
    root_uuid = deterministic_uuid("schematic-root")
    schematic.uuid = root_uuid
    schematic.paper = PageSettings(paperSize="A2")
    schematic.titleBlock = TitleBlock(
        title="Seven-inch Digital Photo Frame Controller", date="2026-09-03",
        revision="A / DIGITAL PRE-BUILD", company="Cleanroom Burr experiment — not production ready",
        comments={1:"ESP32-S3 + SSD1963 8-bit 8080 display", 2:"External certified 5 V USB-C adapter only", 3:"Touch, audio, camera, and battery out of scope"},
    )
    schematic.libSymbols = list(lib_defs.values())
    note_effects = Effects(font=Font(width=2.2, height=2.2, bold=True))
    for idx, (text, x, y) in enumerate([
        ("POWER INPUT / PROTECTION / 3V3",46,30),
        ("ESP32-S3 CONTROLLER / DEBUG",236,30),
        ("DISPLAY — 8-BIT 8080, NO TOUCH",401,30),
        ("STORAGE / CONTROLS / AMBIENT LIGHT",127,257),
    ]):
        schematic.texts.append(Text(text=text, position=Position(x,y,0), effects=note_effects, uuid=deterministic_uuid(f"note-{idx}")))

    for index, component in enumerate(COMPONENTS):
        x = component.sch_pos[0] * 0.0254
        y = component.sch_pos[1] * 0.0254
        definition = SYMBOLS[component.symbol]
        count_left = sum(pin.side == "L" for pin in definition.pins)
        count_right = len(definition.pins) - count_left
        top = max(count_left, count_right, 2) * 100 * 0.0254 / 2 + 3.81
        visible = Effects(font=Font(width=1.1, height=1.1))
        hidden = Effects(font=Font(width=1.0, height=1.0), hide=True)
        properties = [
            Property(key="Reference", value=component.ref, id=0, position=Position(x, y-top-2.0, 0), effects=visible),
            Property(key="Value", value=component.value, id=1, position=Position(x, y+top+2.0, 0), effects=visible),
            Property(key="Footprint", value=component.footprint, id=2, position=Position(x, y, 0), effects=hidden),
            Property(key="Datasheet", value=component.datasheet, id=3, position=Position(x, y, 0), effects=hidden),
            Property(key="MPN", value=component.mpn, position=Position(x, y, 0), effects=hidden),
            Property(key="Manufacturer", value=component.manufacturer, position=Position(x, y, 0), effects=hidden),
            Property(key="Description", value=component.description, position=Position(x, y, 0), effects=hidden),
        ]
        symbol_uuid = deterministic_uuid(f"component-{component.ref}")
        pin_uuids = {number: deterministic_uuid(f"component-{component.ref}-pin-{number}") for number in component.nets}
        instance = SchematicSymbol(
            position=Position(x,y,0), unit=1,
            inBom=component.symbol != "PWR_FLAG", onBoard=bool(component.footprint),
            uuid=symbol_uuid, properties=properties, pins=pin_uuids,
            instances=[SymbolProjectInstance(name="photo_frame", paths=[SymbolProjectPath(sheetInstancePath=f"/{root_uuid}", reference=component.ref, unit=1)])],
        )
        instance.libId = f"PhotoFrame:{component.symbol}"
        schematic.schematicSymbols.append(instance)
        for number, net in component.nets.items():
            if number not in pin_locations_mm[component.symbol]:
                continue
            px, py = pin_locations_mm[component.symbol][number]
            # KiCad sheet coordinates are Y-down while embedded symbol coordinates are Y-up.
            absolute = Position(round(x + px, 4), round(y - py, 4), 0)
            if net is None:
                schematic.noConnects.append(NoConnect(position=absolute, uuid=deterministic_uuid(f"nc-{component.ref}-{number}")))
            else:
                schematic.labels.append(LocalLabel(
                    text=net, position=absolute,
                    effects=Effects(font=Font(width=0.8, height=0.8)),
                    uuid=deterministic_uuid(f"label-{component.ref}-{number}"),
                ))

    schematic.to_file(str(SCH), encoding="utf-8")


def load_footprint(lib_id: str) -> pcbnew.FOOTPRINT:
    lib_name, fp_name = lib_id.split(":", 1)
    path = SHARED / "footprints" / f"{lib_name}.pretty"
    footprint = pcbnew.FootprintLoad(str(path), fp_name)
    if footprint is None:
        raise RuntimeError(f"Unable to load {lib_id} from {path}")
    return footprint


def add_net(board: pcbnew.BOARD, cache: dict[str, pcbnew.NETINFO_ITEM], name: str) -> pcbnew.NETINFO_ITEM:
    if name not in cache:
        item = pcbnew.NETINFO_ITEM(board, name)
        board.Add(item)
        cache[name] = item
    return cache[name]


def add_track(board: pcbnew.BOARD, net: pcbnew.NETINFO_ITEM, start: pcbnew.VECTOR2I, end: pcbnew.VECTOR2I, layer: int, width_mm: float = 0.25) -> None:
    if start == end:
        return
    track = pcbnew.PCB_TRACK(board)
    track.SetStart(start)
    track.SetEnd(end)
    track.SetLayer(layer)
    track.SetWidth(pcbnew.FromMM(width_mm))
    track.SetNet(net)
    board.Add(track)


def add_via(board: pcbnew.BOARD, net: pcbnew.NETINFO_ITEM, position: pcbnew.VECTOR2I) -> None:
    via = pcbnew.PCB_VIA(board)
    via.SetPosition(position)
    via.SetWidth(pcbnew.FromMM(0.7))
    via.SetDrill(pcbnew.FromMM(0.3))
    via.SetLayerPair(pcbnew.F_Cu, pcbnew.B_Cu)
    via.SetNet(net)
    board.Add(via)


def segment_intersects(a1, a2, b1, b2) -> bool:
    def orient(p, q, r):
        return (q[0]-p[0])*(r[1]-p[1]) - (q[1]-p[1])*(r[0]-p[0])
    if a1 in (b1,b2) or a2 in (b1,b2):
        return False
    o1, o2, o3, o4 = orient(a1,a2,b1), orient(a1,a2,b2), orient(b1,b2,a1), orient(b1,b2,a2)
    return (o1 == 0 or o2 == 0 or (o1 > 0) != (o2 > 0)) and (o3 == 0 or o4 == 0 or (o3 > 0) != (o4 > 0))


def generate_board() -> None:
    board = pcbnew.BOARD()
    board.SetCopperLayerCount(4)
    board.SetLayerName(pcbnew.In1_Cu, "GND_PLANE")
    board.SetLayerName(pcbnew.In2_Cu, "POWER_PLANE")
    board.SetFileName(str(PCB))
    nets: dict[str, pcbnew.NETINFO_ITEM] = {}
    pad_locations: dict[str, list[tuple[pcbnew.PAD, pcbnew.VECTOR2I]]] = {}

    for component in COMPONENTS:
        if not component.footprint:
            continue
        footprint = load_footprint(component.footprint)
        footprint.SetReference(component.ref)
        footprint.SetValue(component.value)
        footprint.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(component.pcb_pos[0]), pcbnew.FromMM(component.pcb_pos[1])))
        footprint.SetOrientationDegrees(component.pcb_angle)
        footprint.SetField("MPN", component.mpn)
        footprint.SetField("Manufacturer", component.manufacturer)
        footprint.SetField("Datasheet", component.datasheet)
        board.Add(footprint)
        for pad in footprint.Pads():
            number = pad.GetNumber()
            net_name = component.nets.get(number)
            if net_name:
                net = add_net(board, nets, net_name)
                pad.SetNet(net)
                pad_locations.setdefault(net_name, []).append((pad, pad.GetPosition()))

    # Four board-only NPTH mounting holes aligned with the interface-control document.
    for index, (x,y) in enumerate([(24,24),(128,24),(24,86),(128,86)], 1):
        hole = load_footprint("MountingHole:MountingHole_3.2mm_M3")
        hole.SetReference(f"H{index}")
        hole.SetValue("M3 mounting hole")
        hole.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y)))
        hole.SetBoardOnly(True)
        board.Add(hole)

    # Board outline 112 x 70 mm; origin of product mapping is board center at (76,55).
    corners = [(20,20),(132,20),(132,90),(20,90),(20,20)]
    for first, second in zip(corners, corners[1:]):
        edge = pcbnew.PCB_SHAPE(board)
        edge.SetShape(pcbnew.SHAPE_T_SEGMENT)
        edge.SetStart(pcbnew.VECTOR2I(pcbnew.FromMM(first[0]), pcbnew.FromMM(first[1])))
        edge.SetEnd(pcbnew.VECTOR2I(pcbnew.FromMM(second[0]), pcbnew.FromMM(second[1])))
        edge.SetLayer(pcbnew.Edge_Cuts)
        edge.SetWidth(pcbnew.FromMM(0.1))
        board.Add(edge)

    # Mechanical keep-out and interface notes on User.Drawings.
    notes = [
        (24,22,"M3 (-52,-31)"),(128,22,"M3 (+52,-31)"),(24,88,"M3 (-52,+31)"),(128,88,"M3 (+52,+31)"),
        (121,22,"USB-C EDGE"),(121,87,"DISPLAY CABLE"),(116,77,"microSD EDGE"),
        (22,55,"BOARD 112 x 70 x 1.6 mm; four layers"),
    ]
    for x,y,text in notes:
        item = pcbnew.PCB_TEXT(board)
        item.SetText(text)
        item.SetPosition(pcbnew.VECTOR2I(pcbnew.FromMM(x), pcbnew.FromMM(y)))
        item.SetLayer(pcbnew.Dwgs_User)
        item.SetTextSize(pcbnew.VECTOR2I(pcbnew.FromMM(1.0), pcbnew.FromMM(1.0)))
        item.SetTextThickness(pcbnew.FromMM(0.15))
        board.Add(item)

    # Dedicated internal-layer trunks for the three high-fanout rails.  Via-in-pad
    # is deliberate in this digital pre-build and recorded in the report as a
    # fabrication review item; it keeps the deterministic pre-layout compact.
    power_layers = {"GND": pcbnew.In1_Cu, "+3V3": pcbnew.In2_Cu, "+5V": pcbnew.B_Cu, "+5V_RAW": pcbnew.B_Cu}
    for net_name, layer in power_layers.items():
        points = [position for _, position in pad_locations.get(net_name, [])]
        if not points:
            continue
        net = nets[net_name]
        for pad, position in pad_locations[net_name]:
            if not pad.IsOnLayer(layer):
                add_via(board, net, position)
        # Minimum spanning-like chain, sorted in X then Y, all one net.
        points = sorted(points, key=lambda p: (p.x, p.y))
        for p1, p2 in zip(points, points[1:]):
            midpoint = pcbnew.VECTOR2I(p2.x, p1.y)
            add_track(board, net, p1, midpoint, layer, 0.5 if net_name != "GND" else 0.65)
            add_track(board, net, midpoint, p2, layer, 0.5 if net_name != "GND" else 0.65)

    # Signal connections.  Two-pad nets are routed directly and greedily colored
    # across four copper layers to avoid track-track crossings.  Multi-pad signal
    # nets use a short same-net daisy chain.
    signal_layers = [pcbnew.F_Cu, pcbnew.B_Cu, pcbnew.In1_Cu, pcbnew.In2_Cu]
    routed_by_layer: dict[int, list[tuple[tuple[int,int],tuple[int,int]]]] = {layer:[] for layer in signal_layers}
    for net_name in sorted(pad_locations):
        if net_name in power_layers:
            continue
        pads = pad_locations[net_name]
        if len(pads) < 2:
            continue
        points = [position for _, position in pads]
        ordered = sorted(points, key=lambda p: (p.x, p.y))
        pairs = list(zip(ordered, ordered[1:]))
        for start, end in pairs:
            a1, a2 = (start.x,start.y), (end.x,end.y)
            chosen = signal_layers[-1]
            for layer in signal_layers:
                if not any(segment_intersects(a1,a2,b1,b2) for b1,b2 in routed_by_layer[layer]):
                    chosen = layer
                    break
            for pad, position in pads:
                if position in (start,end) and not pad.IsOnLayer(chosen):
                    add_via(board, nets[net_name], position)
            add_track(board, nets[net_name], start, end, chosen, 0.25)
            routed_by_layer[chosen].append((a1,a2))

    board.BuildListOfNets()
    pcbnew.SaveBoard(str(PCB), board)


def write_project() -> None:
    project = {
        "board": {}, "boards": [], "cvpcb": {}, "erc": {}, "libraries": {},
        "meta": {"filename": "photo_frame.kicad_pro", "version": 1},
        "net_settings": {"classes": [], "meta": {"version": 3}},
        "pcbnew": {}, "schematic": {}, "sheets": [], "text_variables": {},
    }
    PRO.write_text(json.dumps(project, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    KICAD_DIR.mkdir(parents=True, exist_ok=True)
    write_library()
    write_legacy_schematic()
    write_modern_schematic()
    write_project()
    generate_board()
    print(SCH)
    print(PCB)


if __name__ == "__main__":
    main()
