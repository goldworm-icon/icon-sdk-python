# -*- coding: utf-8 -*-

# Copyright 2019 ICON Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from iconsdk.data.dict import Dict, JsonRpcEncoder
from iconsdk.data.address import Address, AddressPrefix


class TestDict(unittest.TestCase):
    def test__str__(self):
        data = Dict()
        data["address"] = Address.from_string("hx8d94f443d4a0002ebd4b86634b4a8502a7d180d4")
        data["int"] = -100
        data["bool"] = False
        data["bytes"] = b"hello"

        req = Dict()
        req["address"] = Address.from_string("hx8d94f443d4a0002ebd4b86634b4a8502a7d180d4")
        req["int"] = 100
        req["bool"] = True
        # req["data"] = data

        print(req)

    def test_encoder(self):
        a = {
            "a": Address.from_string("hx8d94f443d4a0002ebd4b86634b4a8502a7d180d4"),
            "b": 100
        }
        print(JsonRpcEncoder().encode(a))
