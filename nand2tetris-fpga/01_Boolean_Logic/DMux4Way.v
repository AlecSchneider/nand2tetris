/**
 * 4-way demultiplexor:
 * {a, b, c, d} = {in, 0, 0, 0} if sel == 00
 *                {0, in, 0, 0} if sel == 01
 *                {0, 0, in, 0} if sel == 10
 *                {0, 0, 0, in} if sel == 11
 */

`default_nettype none
module DMux4Way(
	input in,
	input [1:0] sel,
  output a,
	output b,
	output c,
	output d
);

  wire notsel1;
  Not NOT(.in(sel[1]), .out(notsel1));

  wire ab;
  And AND1(.a(in), .b(notsel1), .out(ab));
  DMux DMUX1(.in(ab), .sel(sel[0]), .a(a), .b(b));

  wire cd;
  And AND2(.a(in), .b(sel[1]), .out(cd));
  DMux DMUX2(.in(cd), .sel(sel[0]), .a(c), .b(d));

endmodule
