/*
**  Copyright 2008 Luke Hodkinson
**
**  This file is part of pcu.
**
**  pcu is free software: you can redistribute it and/or modify
**  it under the terms of the GNU General Public License as published by
**  the Free Software Foundation, either version 3 of the License, or
**  (at your option) any later version.
**
**  pcu is distributed in the hope that it will be useful,
**  but WITHOUT ANY WARRANTY; without even the implied warranty of
**  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
**  GNU General Public License for more details.
**
**  You should have received a copy of the GNU General Public License
**  along with pcu.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <stdlib.h>
#include <mpi.h>
#include <pcu/pcu.h>

/* Include the test suite header files. */
#include "samplea_suite.h"
#include "sampleb_suite.h"

/* Begin execution. */
int main( int argc, char* argv[] ) {
   pcu_listener_t* lsnr;

   /* Initialise the MPI libraries. */
   MPI_Init( &argc, &argv );

   /* Initialise the test runner. */
   pcu_runner_init( argc, argv );

   /* Add the suites. */
   pcu_runner_addSuite( samplea, samplea_init );
   pcu_runner_addSuite( sampleb, sampleb_init );

   /* Create a listener to respond to test signals. */
   lsnr = pcu_textoutput_create();

   /* Run all suites. */
   pcu_runner_run( lsnr );

   /* Clean up the runner and listeners. */
   pcu_runner_finalise();
   pcu_textoutput_destroy( lsnr );

   /* Shutdown MPI. */
   MPI_Finalize();

   return EXIT_SUCCESS;
}
