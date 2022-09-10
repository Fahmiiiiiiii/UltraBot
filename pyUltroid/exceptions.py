#!/usr/bin/env bash
# UltraBot - UserBot
# Copyright (C) 2022-2023 UltraBot
#
# This file is a part of < https://github.com/Fahmiiiiiiii/UltraBot/ >
# PLease read the GNU Affero General Public License in <https://www.github.com/Fahmiiiiiiii/UltraBot/blob/main/LICENSE/>.

"""
Exceptions which can be raised by py-Ultroid Itself.
"""


class pyUltroidError(Exception):
    ...


class TelethonMissingError(ImportError):
    ...


class DependencyMissingError(ImportError):
    ...


class RunningAsFunctionLibError(pyUltroidError):
    ...
