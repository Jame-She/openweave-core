#!/usr/bin/env python3


#
#    Copyright (c) 2016-2017 Nest Labs, Inc.
#    All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#

#
#    @file
#       A01: Calls Weave Echo with udp over tunnel between mock device and real service.
#

from __future__ import absolute_import
from __future__ import print_function
import unittest
from test_weave_echo_base import test_weave_echo_base


class test_weave_echo_01(test_weave_echo_base):
    def test_weave_echo_01(self):
        echo_args = {}
        echo_args["udp"] = True
        echo_args["endpoint"] = 'Echo'
        echo_args['test_tag'] = self.__class__.__name__
        echo_args['test_case_name'] = ['Echo-NestService-A01: Calls Weave Echo with udp over tunnel between mock device and real service.']
        print('test file: ' + self.__class__.__name__)
        print("weave echo test A01")
        super(test_weave_echo_01, self).weave_echo_base(echo_args)


if __name__ == "__main__":
    unittest.main()

