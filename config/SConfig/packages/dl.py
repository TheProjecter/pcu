#
#  Copyright 2008 Luke Hodkinson
#
#  This file is part of pcu.
#
#  pcu is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  pcu is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with pcu.  If not, see <http://www.gnu.org/licenses/>.
#

import os
import SConfig

class dl(SConfig.Package):
    def __init__(self, scons_env, scons_opts, required=False):
        SConfig.Package.__init__(self, scons_env, scons_opts, required)
        self.dependency(SConfig.packages.CompilerFlags)
        self.headers = [['dlfcn.h']]
        self.libraries = [['dl']]

    def setup(self):
        SConfig.Node.setup(self)
