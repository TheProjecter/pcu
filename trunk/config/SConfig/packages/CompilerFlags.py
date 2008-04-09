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

import os, platform
import SCons.Script
import SConfig

class CompilerFlags(SConfig.Node):
    def __init__(self, scons_env, scons_opts, required=False):
        SConfig.Node.__init__(self, scons_env, scons_opts, required)
        self.checks = [self.check_bit_flags,
                       self.check_architecture]

    def setup_options(self):
        SConfig.Node.setup_options(self)
        self.opts.AddOptions(
            SCons.Script.BoolOption('with_32bit', 'Generate 32bit code', 0),
            SCons.Script.BoolOption('with_64bit', 'Generate 64bit code', 0)
            )

    def check_architecture(self):
        if (platform.platform().find('x86_64') != -1 or \
            platform.platform().find('ppc64') != -1 or \
            platform.architecture()[0].find('64') != -1 or \
            self.env['with_64bit']) and \
            not self.env['with_32bit']:
            self.bits = 64
            if self.flag_64bit:
                self.env.MergeFlags(self.flag_64bit)
                if self.env.subst('$CC') == self.env.subst('$LINK'):
                    self.env.AppendUnique(LINKFLAGS=[self.flag_64bit])
        else:
            self.bits = 32
            if self.flag_32bit:
                self.env.MergeFlags(self.flag_32bit)
                if self.env.subst('$CC') == self.env.subst('$LINK'):
                    self.env.AppendUnique(LINKFLAGS=[self.flag_32bit])
        return True

    def check_bit_flags(self):
        if self.try_flag('-m32')[0]:
            self.flag_32bit = '-m32'
        elif self.try_flag('-q32')[0]:
            self.flag_32bit = '-q32'
        else:
            self.flag_32bit = ''
        if self.try_flag('-m64')[0]:
            self.flag_64bit = '-m64'
        elif self.try_flag('-q64')[0]:
            self.flag_64bit = '-q64'
        else:
            self.flag_64bit = ''
        return True

    def try_flag(self, flag):
        state = self.env.ParseFlags(flag)
        old = self.push_state(state)
        result = self.run_scons_cmd(self.ctx.TryCompile, '', '.c')
        self.pop_state(old)
        if result[0] and (result[1].find('not recognized') != -1 or
                          result[1].find('not recognised') != -1 or
                          result[1].find('unknown option') != -1):
            result[0] = 0
        return [result[0], result[1], '']
