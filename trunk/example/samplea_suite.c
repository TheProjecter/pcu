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
#include <pcu/pcu.h>
#include "samplea_suite.h"
#include "samplec_suite.h"


/* Define an arbitrary data structure that this
   suite may use for fixtures. */
typedef struct {
      int a;
      int b;
      int* set;
} sampleadata_t;


/*
** Here we define our tests.
*/

void samplea_testa( sampleadata_t* data ) {
   pcu_assert_true( 1 );
   pcu_assert_true( 1 );
}

void samplea_testb( sampleadata_t* data ) {
   pcu_assert_true( 1 );
   pcu_assert_true( 1 );
}

/*
** Functions for setting up tests.
*/

/* The setup fixture. */
void samplea_setup( sampleadata_t* data ) {
   data->a = 10;
   data->b = 20;
   data->set = (int*)malloc( 5 * sizeof(int) );
}

/* The teardown fixture. */
void samplea_teardown( sampleadata_t* data ) {
   free( data->set );
}

/* Here we need to setup the suite. */
void samplea_init( pcu_suite_t* suite ) {
   /* Inform the suite of our fixture data structure. */
   pcu_suite_setData( suite, sampleadata_t );

   /* Set the fixture functions. */
   pcu_suite_setFixtures( suite, samplea_setup, samplea_teardown );

   /* Add our tests. */
   pcu_suite_addTest( suite, samplea_testa );
   pcu_suite_addTest( suite, samplea_testb );

   /* Add sub-suites. */
   pcu_suite_addSubSuite( suite, samplec );
}
