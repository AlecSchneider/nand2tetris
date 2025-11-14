 /**
 * Or gate:
 * out = 1 if (a == 1 or b == 1)
 *       0 otherwise
 */

`default_nettype none
module Or(
	input a,
	input b,
	output out
);
  wire nota;
  Not NOT1(.in(a), .out(nota));

  wire notb;
  Not NOT2(.in(b), .out(notb));

  wire notab;
  And AND(.a(nota), .b(notb), .out(notab));

  Not NOT3(.in(notab), .out(out));

endmodule
