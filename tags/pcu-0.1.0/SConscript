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

Import('env')

# Move headers to our build directory.
headers = env.glob('src/*.h')
for hdr in headers:
    env.Install(env.get_build_path('include/pcu'), hdr)

# Build our source files.
sources = env.glob('src/*.c')
src_objs = []
for src in sources:
    src_objs += env.SharedObject(env.get_target_name('pcu/' + src, '.c'), src)

# Build a library (if needed) and register destination.
if env['static_libraries']:
    env.Library(env.get_target_name('lib/pcu'), src_objs)
if env['shared_libraries']:
    env.SharedLibrary(env.get_target_name('lib/pcu'), src_objs)

# Build the example/test.
sources = env.glob('example/*.c')
objs = []
for src in sources:
    objs += env.SharedObject(env.get_target_name('pcu/' + src, '.c'), src)

env.Program(env.get_build_path('bin/test_pcu'), objs,
            LIBS=['pcu'] + env.get('LIBS', []))

# Copy the script to the build directory.
env.Install(env.get_build_path('script/pcu'), 'script/scons.py')
