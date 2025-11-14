/**
 * 8-way Or: 
 * out = (in[0] or in[1] or ... or in[7])
 */

`default_nettype none
module Or8Way(
	input [7:0] in,
	output out
);

  wire or01;
  Or OR1(.a(in[0]), .b(in[1]), .out(or01));

  wire or23;
  Or OR2(.a(in[2]), .b(in[3]), .out(or23));

  wire or45;
  Or OR3(.a(in[4]), .b(in[5]), .out(or45));

  wire or67;
  Or OR4(.a(in[6]), .b(in[7]), .out(or67));
  
  wire or0123;
  Or OR5(.a(or01), .b(or23), .out(or0123));

  wire or4567;
  Or OR6(.a(or45), .b(or67), .out(or4567));

  Or OR7(.a(or0123), .b(or4567), .out(out));

endmodule
