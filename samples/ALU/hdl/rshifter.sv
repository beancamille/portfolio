`timescale 1ns / 1ps

// takes in x, y, shift code. outputs z. 
module rshifter(
    input logic [31:0] x,
    input logic [31:0] y,
    input logic arith1_log0,
    output logic [31:0] z
    );

    // logic used within module.
    logic [27:0] grt_32;
    logic toomuch;
    logic [31:0][31:0] all_opts;
    logic [31:0] finres;
    logic [31:0] chosen_opt;
    logic [31:0] empty;
    logic [31:0] arith_empty;
    logic [15:0][31:0] newlook1;
    logic [7:0][31:0] newlook2;
    logic [3:0][31:0] newlook3;
    logic [1:0][31:0] newlook4;
    logic [0:0][31:0] newlook5;
    logic firbit;
    
    // create "empty" for use with too many shift places
    assign arith_empty = x[31] ? 32'b11111111111111111111111111111111: 32'b00000000000000000000000000000000;
    assign empty = arith1_log0 ? arith_empty:32'b00000000000000000000000000000000;

    // see if shift is too large. assign "too much" if shift exceeds places.
    assign grt_32[27] = 0;
    generate
        genvar k;
        for (k = 31; k > 4; k--) begin
            or toogreat (grt_32[k-5], y[k], grt_32[k-4]);
        end
    endgenerate
    assign toomuch = grt_32[0];
    
    assign firbit = arith1_log0 ? x[31] : 0;
    
    // execute shifting
    generate
        genvar m;
        genvar n;
        for (m = 0; m < 31; m++) begin
            // get the shift values
            for (n = 0; n < 32 - m; n++)
                assign all_opts[m][n] = x[n+m];
            // finish through w/ all 0s
            for (n = 31 - m; n < 32; n++)
                assign all_opts[m][n] = firbit;
        end
    endgenerate
    
    assign newlook1 = y[4] ? all_opts[31:16] : all_opts[15:0];
    assign newlook2 = y[3] ? newlook1[15:8] : newlook1[7:0];
    assign newlook3 = y[2] ? newlook2[7:0] : newlook2[3:0];
    assign newlook4 = y[1] ? newlook3[3:2] : newlook3[1:0];
    assign newlook5 = y[0] ? newlook4[1:1] : newlook4[0:0];
    
    assign chosen_opt = newlook5;
    
    // check if toomuch was true, and assign all zeros if so
    assign finres = toomuch ? empty : chosen_opt;
    assign z = finres;
endmodule
