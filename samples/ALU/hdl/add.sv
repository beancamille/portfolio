// ripple carry adder

// takes in x, y, initial carry. outputs z, final carry. 
module add(
    input logic [31:0] x,
    input logic [31:0] y,
    input logic c_in,
    output logic [31:0] z,
    output logic [32:0] c
    );
    logic [31:0] t0;
    logic [31:0] t1;
    logic [31:0] t2;
    logic [31:0] t3;
    logic [31:0] t4;
    
    assign c[0] = c_in;

    // use generate to execute adder for every bit from the inputs
    generate
        genvar i;
        for (i = 0; i < 32; i = i + 1) begin
            xor mid1 (t0[i], x[i], y[i]);
            xor mid2 (z[i], c[i], t0[i]);
            and ca (t1[i], x[i], y[i]);
            and cb (t2[i], x[i], c[i]);
            and cc (t3[i], y[i], c[i]);
            or fin1 (t4[i], t1[i], t2[i]);
            or fin2 (c[i+1], t4[i], t3[i]);
            end
    endgenerate
endmodule
