OPENQASM 2.0;
include "qelib1.inc";

qreg q[3];

h q[0];
cx q[0], q[1];
cx q[0], q[2];

creg c[3];
measure q->c;