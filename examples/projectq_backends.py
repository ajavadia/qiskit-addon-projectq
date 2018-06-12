# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,anomalous-backslash-in-string

# Copyright 2017 IBM RESEARCH. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================
"""
Example use of the symbolic simulator backends, which keep precise forms of
amplitudes.
"""

import os
from qiskit_addon_projectq import QasmSimulatorProjectQ
from qiskit import execute, load_qasm_file


def use_projectq_backends():
    q_circuit = load_qasm_file('ghz.qasm')
   
    # ProjectQ simulator
    result = execute(q_circuit, backend=QasmSimulatorProjectQ(), shots=100).result()
    print("counts: ")
    print(result.get_counts(q_circuit))

if __name__ == "__main__":
    use_projectq_backends()
