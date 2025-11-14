/**
 * 16-bit multiplexor: 
 * for i = 0..15 out[i] = a[i] if sel == 0 
 *                        b[i] if sel == 1
 */

`default_nettype none
module Mux4Way16(
	input [15:0] a,
	input [15:0] b,
	input [15:0] c,
	input [15:0] d,
  input [1:0] sel,
	output [15:0] out
);

  wire [15:0] selab;
  Mux16 MUX161(.a(a), .b(b), .sel(sel[0]), .out(selab));

  wire [15:0] selcd;
  Mux16 MUX162(.a(c), .b(d), .sel(sel[0]), .out(selcd));

  Mux16 MUX163(.a(selab), .b(selcd), .sel(sel[1]), .out(out));

endmodule
