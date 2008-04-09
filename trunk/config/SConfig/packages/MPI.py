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

import os
import SConfig

class MPI(SConfig.Package):
    def __init__(self, scons_env, scons_opts, required=False):
        SConfig.Package.__init__(self, scons_env, scons_opts, required)
        self.dependency(SConfig.packages.CompilerFlags)
        self.base_patterns = ['mpich*', 'MPICH*']
        self.header_sub_dir = 'mpi'
        self.headers = [['mpi.h']]
        self.libraries = [['mpich'],
                          ['mpich', 'pmpich'],
                          ['mpich', 'rt'],
                          ['mpich', 'pmpich', 'rt'],
                          ['mpi'],
                          ['lam', 'mpi']]
        self.shared_libraries = ['mpich', 'pmpich', 'mpi', 'lam']
        self.require_shared = True
        self.symbols = [(['MPI_Init', 'MPI_Finalize'], '')]
        self.symbol_calls = ['%s(&argc, &argv);', '%s();']

    def generate_locations(self):
        for loc in SConfig.Package.generate_locations(self):
            for lib_dir in loc[2]:
                shared_dir = os.path.join(lib_dir, 'shared')
                path = os.path.join(loc[0], shared_dir)
                if os.path.exists(path):
                    loc[2] = [shared_dir] + loc[2]
            yield loc
