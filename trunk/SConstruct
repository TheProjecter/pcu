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
#  Foobar is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), 'config')))
import SConfig
SConscript('config/SConfig/SConscript')

#
# CUSTOMISE THE ENVIRONMENT HERE.
#

env = Environment(ENV=os.environ)
env['_abspath'] = lambda x: File(x).abspath # Needed by Darwin.

# Determine whether we are configuring, helping or building.
if 'config' in COMMAND_LINE_TARGETS or 'help' in COMMAND_LINE_TARGETS:

    #
    # INSERT CONFIGURATION HERE.
    #

    proj = env.Package(SConfig.Project, True)
    proj.dependency(SConfig.packages.MPI)
    env.configure_packages()

    # Save results.
    env.save_config()

else:
    # Load configuration.
    env.load_config()

    #
    # INSERT TARGETS HERE.
    #

    SConscript('SConscript', exports='env')
