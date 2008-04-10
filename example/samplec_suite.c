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
#include "samplec_suite.h"
#include "sampleb_suite.h"


void samplec_testa( void* data ) {
   pcu_assert_gt( 1, 2 );
   pcu_assert_gt( 2, 1 );
}

void samplec_testb( void* data ) {
   pcu_assert_le( 1, 1 );
   pcu_assert_le( 2, 1 );
}

void samplec_init( pcu_suite_t* suite ) {
   /* We have no fixtures, so just add the tests. */
   pcu_suite_addTest( suite, samplec_testa );
   pcu_suite_addTest( suite, samplec_testb );

   /* ... and the sub suites. */
   pcu_suite_addSubSuite( suite, sampleb );
}
