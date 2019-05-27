# -*- coding: utf-8 -*-
# Copyright 2018 ICON Foundation
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

from .providers.provider import Provider
from .data.jsonrpc_request import JsonRpcRequest
from .data.jsonrpc_response import JsonRpcResponse
from .data.transaction_result import TransactionResult


class IconClient(object):
    """
    The IconService class contains a set of API methods.
    It accepts a HTTPProvider which serves the purpose of 
    connecting to HTTP and HTTPS based JSON-RPC servers.
    """

    def __init__(self, provider: Provider):
        self.__provider = provider

    def send(self, request: JsonRpcRequest) -> JsonRpcResponse:
        pass
