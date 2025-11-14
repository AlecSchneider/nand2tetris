/**
 * 8-way demultiplexor:
 * {a, b, c, d, e, f, g, h} = {in, 0, 0, 0, 0, 0, 0, 0} if sel == 000
 *                            {0, in, 0, 0, 0, 0, 0, 0} if sel == 001
 *                            etc.
 *                            {0, 0, 0, 0, 0, 0, 0, in} if sel == 111
 */

`default_nettype none
module DMux8Way(
	input in,
	input [2:0] sel,
  output a,
	output b,
	output c,
	output d,
	output e,
	output f,
	output g,
	output h
);

  wire notsel2;
  Not NOT(.in(sel[2]), .out(notsel2));

  wire abcd;
  And AND1(.a(in), .b(notsel2), .out(abcd));
  DMux4Way DMUX1(.in(abcd), .sel(sel[1:0]), .a(a), .b(b), .c(c), .d(d));

  wire efgh;
  And AND2(.a(in), .b(sel[2]), .out(efgh));
  DMux4Way DMUX2(.in(efgh), .sel(sel[1:0]), .a(e), .b(f), .c(g), .d(h));

endmodule
