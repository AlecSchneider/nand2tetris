/** 
 * Multiplexor:
 * out = a if sel == 0
 *       b otherwise
 */

`default_nettype none
module Mux(
	input a,
	input b,
	input sel,
	output out
);
  wire notsel;
  Not NOT(.in(sel), .out(notsel));

  wire sela;
  And AND1(.a(a), .b(notsel), .out(sela));
  
  wire selb;
  And AND2(.a(b), .b(sel), .out(selb));

  Or OR(.a(sela), .b(selb), .out(out));

endmodule
