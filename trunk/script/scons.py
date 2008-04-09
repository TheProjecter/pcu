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

def build_suite_runner(target, source, env):
    suites = ""
    hdrs = env.get('PCURUNNERHEADERS', '')
    init = env.get('PCURUNNERINIT', '_init')
    setup = env.get('PCURUNNERSETUP', '')
    if setup: setup = '\n' + setup
    teardown = env.get('PCURUNNERTEARDOWN', '')
    if teardown: teardown = '\n' + teardown
    for node in source:
        name = os.path.basename(node.path[:node.path.rfind('.')])
        suites += "   pcu_runner_addSuite( %s, %s );\n" % (name, name + init)
        name = node.abspath[:node.abspath.rfind('.')]
        hdrs += "#include \"%s.h\"\n" % name
    src = """#include <stdlib.h>
#include <mpi.h>
#include <pcu/pcu.h>
%s

int main( int argc, char* argv[] ) {
   pcu_listener_t* lsnr;

   MPI_Init( &argc, &argv );
   pcu_runner_init( argc, argv );%s

%s
   lsnr = pcu_textoutput_create();
   pcu_runner_run( lsnr );
   pcu_textoutput_destroy( lsnr );
%s
   pcu_runner_finalise();
   MPI_Finalize();
   return EXIT_SUCCESS;
}
""" % (hdrs, setup, suites, teardown)
    if not os.path.exists(os.path.dirname(target[0].abspath)):
        os.makedirs(os.path.dirname(target[0].abspath))
    f = open(target[0].abspath, "w")
    f.write(src)
    f.close()

Import('env')
env['BUILDERS']['PCUSuiteRunner']=Builder(action=build_suite_runner)
