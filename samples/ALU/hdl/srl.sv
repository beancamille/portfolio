`timescale 1ns / 1ps
// shift right logical 
// inputs x, y. output z.
module srl(
    input logic [31:0] x,
    input logic [31:0] y,
    output logic [31:0] z
    );
    logic temp;
    assign temp = 1'b0;
    // call right-shifter with code '0'.
    rshifter srl_shift (.x(x), .y(y), .arith1_log0(temp), .z(z));
    
endmodule
