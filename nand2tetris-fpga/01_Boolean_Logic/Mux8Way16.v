/**
 * 16-bit multiplexor: 
 * for i = 0..15 out[i] = a[i] if sel == 0 
 *                        b[i] if sel == 1
 */

`default_nettype none
module Mux8Way16(
	input [15:0] a,
	input [15:0] b,
	input [15:0] c,
	input [15:0] d,
	input [15:0] e,
	input [15:0] f,
	input [15:0] g,
	input [15:0] h,
  input [2:0] sel,
	output [15:0] out
);

  wire [15:0] selabcd;
  Mux4Way16 MUX1(.a(a), .b(b), .c(c), .d(d), .sel(sel[1:0]), .out(selabcd));

  wire [15:0] selefgh;
  Mux4Way16 MUX2(.a(e), .b(f), .c(g), .d(h), .sel(sel[1:0]), .out(selefgh));

  Mux16 MUX3(.a(selabcd), .b(selefgh), .sel(sel[2]), .out(out));

endmodule
