/**
 * Exclusive-or gate:
 * out = not (a == b)
 */

`default_nettype none
module Xor(
	input a,
	input b,
	output out
);
  wire nota;        //new wire must be declared (as wire)
  wire notb;
  Not NOT1(.in(a), .out(nota));    //Every chip has an instance name (NOT1)
  Not NOT2(.in(b), .out(notb));    //this chip is named NOT2

  wire w1;
  wire w2;
  And AND1(.a(a),.b(notb),.out(w1));
  And AND2(.a(nota),.b(b),.out(w2));

  Or OR(.a(w1),.b(w2),.out(out));
endmodule
