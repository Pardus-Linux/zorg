# -*- coding: utf-8 -*-

import os

from zorg.config import *
from zorg.probe import *
from zorg.utils import *

def selectOutput(device):
    output = ""
    mode = ""

    outs = device.probe_result["outputs"].split(",")
    for out in outs:
        modes = device.probe_result.get("%s-modes" % out, "").split(",")
        if modes:
            output = out
            mode = modes[0]
            break

    if not output:
        output = outs[0]
        mode = "800x600"

    device.active_outputs = [output]
    device.modes[output] = mode

def initialConfig():
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        return

    device.query()
    selectOutput(device)

    saveXorgConfig(device)
    saveDeviceInfo(device)

def safeConfig():
    bus = getPrimaryCard()

    if bus:
        device = VideoDevice(bus)
    else:
        return

    device.monitor_settings["default-hsync"] = "31.5-50"
    device.monitor_settings["default-vref"] = "50-70"

    saveXorgConfig(device)
    saveDeviceInfo(device)

def activeDeviceID():
    if not os.path.exists(xorgConf):
        return

    parser = XorgParser()
    parser.parseFile(xorgConf)

    devSec = parser.getSections("Device")[0]
    busId = devSec.get("BusId")

    return busId

def changeDriver(busId, driver):
    pass

def setupScreens(busId, options, firstScreen, secondScreen):
    device = getDeviceInfo(busId)

    if not device:
        return

    dsetup = options.get("desktop-setup", "single")

    if dsetup not in ("single", "clone", "horizontal", "vertical"):
        return

    device.desktop_setup = dsetup

    if options.has_key("depth"):
        device.depth = options["depth"]

    device.active_outputs = [firstScreen["output"]]
    device.modes[firstScreen["output"]] = firstScreen["mode"]

    if dsetup != "single":
        device.active_outputs.append(secondScreen["output"])
        device.modes[secondScreen["output"]] = secondScreen["mode"]

    device.requestDriverOptions()

    saveXorgConfig(device)
    saveDeviceInfo(device)
