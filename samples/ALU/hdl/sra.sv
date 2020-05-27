`timescale 1ns / 1ps
// shift right arithmetic 
// inputs x, y. output z.
module sra(
    input logic [31:0] x,
    input logic [31:0] y,
    output logic [31:0] z
    );
    
    // call right-shifter helper. use code "1". 
    rshifter sra_shift (.x(x), .y(y), .arith1_log0(1'b1), .z(z));

endmodule
