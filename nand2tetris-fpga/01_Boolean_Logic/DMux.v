/**
 * Demultiplexor:
 * {a, b} = {in, 0} if sel == 0
 *          {0, in} if sel == 1
 */

`default_nettype none
module DMux(
	input in,
	input sel,
  output a,
	output b
);
  wire notsel;
  Not NOT(.in(sel), .out(notsel));

  And AND1(.a(in), .b(notsel), .out(a));
  And AND2(.a(in), .b(sel), .out(b));
endmodule
