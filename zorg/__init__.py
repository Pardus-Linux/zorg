#-*- coding: utf-8 -*-
#
# Copyright (C) 2007-2009, TUBITAK/UEKAE
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation; either version 2 of the License, or (at your option)
# any later version.
#
# Please read the COPYING file.
#

__version__ = "1.2.2"

__all__ = ["config",
           "consts",
           "ddc",
           "hwdata",
           "modeline",
           "parser",
           "probe",
           "utils"]


def versionString():
    return __version__
