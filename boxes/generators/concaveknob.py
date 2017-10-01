#!/usr/bin/env python3
# Copyright (C) 2013-2017 Florian Festi
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

from boxes import *

class ConcaveKnob(Boxes):
    """Round knob serraded outside for better gripping"""
    
    ui_group = "Part"

    def __init__(self):
        Boxes.__init__(self)

        # Add non default cli params if needed (see argparse std lib)
        self.argparser.add_argument(
            "--diameter",  action="store", type=float, default=50.,
            help="Diameter of the knob")
        self.argparser.add_argument(
            "--serrations",  action="store", type=int, default=3,
            help="Number of serrations")
        self.argparser.add_argument(
            "--rounded",  action="store", type=float, default=.2,
            help="Amount of circumference used for non convex parts")
        self.argparser.add_argument(
            "--angle",  action="store", type=float, default=70.,
            help="Angle between convex and concave parts")        
        self.argparser.add_argument(
            "--bolthole",  action="store", type=float, default=6.,
            help="Diameter of the bolt hole")
        self.argparser.add_argument(
            "--hexhead",  action="store", type=float, default=10.,
            help="Width of the hex bolt head")

    def render(self):
        t = self.thickness
        # Initialize canvas
        self.open()
        self.parts.concaveKnob(self.diameter, self.serrations,
                               self.rounded, self.angle,
                               hole=self.bolthole, move="right")
        self.parts.concaveKnob(self.diameter, self.serrations,
                               self.rounded, self.angle,
                               callback=lambda: self.nutHole(self.hexhead),
                               move="right")
        self.parts.concaveKnob(self.diameter, self.serrations,
                               self.rounded, self.angle)

        self.close()
