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

import os, platform
import SCons.Script
import SConfig

class Platform(SConfig.Node):
    def __init__(self, scons_env, scons_opts, required=False):
        SConfig.Node.__init__(self, scons_env, scons_opts, required)
        self.checks = [self.print_results]

        # Will be set after successful configuration.
        self.system = ''
        self.bits = 0

        # We need to do these now.
        self.check_system()
        self.check_bits()
        self.check_CC()

    def setup_options(self):
        self.opts.AddOptions(
            SCons.Script.BoolOption('with_32bit', 'Generate 32bit code', 0),
            SCons.Script.BoolOption('with_64bit', 'Generate 64bit code', 0),
            )

    def check_system(self):
        self.system = platform.system()
        if not self.system or self.system in ['Linux', 'Unix']:
            self.system = '*ix'

        # Need to modify building shared libraries when on Mac OS X.
        if self.system == 'Darwin':
            self.env.AppendUnique(SHLINKFLAGS=['-flat_namespace',
                                          '-single_module',
                                          '-undefined', 'suppress'])
            import SCons.Util # And fix RPATHs.
            self.env['LINKFLAGS'] = SCons.Util.CLVar('')
            self.env['RPATHPREFIX'] = ''
            self.env['RPATHSUFFIX'] = ''
            self.env['_RPATH'] = ''

            # Use 'install_name' instead.
            self.env.Append(SHLINKFLAGS=['-install_name', '${_abspath(TARGET)}'])

            self.env.AppendUnique(CONFIGVARS=['SHLINKFLAGS', 'LINKFLAGS',
                                              'RPATHPREFIX', 'RPATHSUFFIX', '_RPATH'])

    def check_bits(self):
        if (platform.platform().find('x86_64') != -1 or \
                platform.platform().find('ppc64') != -1 or \
                platform.architecture()[0].find('64') != -1 or \
                self.env['with_64bit']) and \
                not self.env['with_32bit']:
            self.bits = 64
        else:
            self.bits = 32

    def check_CC(self):
        if 'CC' in self.env['ENV']:
            self.env['CC'] = self.env['ENV']['CC']
            self.CC = self.env['CC']

    def print_results(self):
        self.ctx.Display("  Building on a %s platform\n" % self.system)
        self.ctx.Display("  Building for %d bit architecture\n" % self.bits)
        if hasattr(self, 'CC'):
            self.ctx.Display("  Using environment specified C compiler: %s\n" % self.CC)
        return True
