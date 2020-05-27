`timescale 1ns / 1ps

// takes in x, y. outputs z. 
module sll(
    input logic [31:0] x,
    input logic [31:0] y,
    output logic [31:0] z
    );
    
    logic [27:0] grt_32;
    logic toomuch;
    logic [31:0][31:0] all_opts;
    logic [31:0] finres;
    logic [31:0] chosen_opt;
    logic [31:0] empty;
    logic [15:0][31:0] newlook1;
    logic [7:0][31:0] newlook2;
    logic [3:0][31:0] newlook3;
    logic [1:0][31:0] newlook4;
    logic [0:0][31:0] newlook5;
    
    // all 0s if shifting by too much
    assign empty = 32'b0;
    
    // look at 6-32 bits of y to see if by more than 32 places
    assign grt_32[27] = 0;
    generate
        genvar k;
        for (k = 31; k > 4; k--) begin
            or toogreat (grt_32[k-5], y[k], grt_32[k-4]);
        end
    endgenerate
    assign toomuch = grt_32[0];
        
    generate
        genvar m;
        genvar n;
        for (m = 0; m < 31; m++) begin
            // get the shift values
            for (n = 31; n >= m; n--)
                assign all_opts[m][n] = x[n-m];
            // finish through w/ all 0s
            for (n = 0; n < m; n++)
                assign all_opts[m][n] = 0;
        end
    endgenerate
    
    assign newlook1 = y[4] ? all_opts[31:16] : all_opts[15:0];
    assign newlook2 = y[3] ? newlook1[15:8] : newlook1[7:0];
    assign newlook3 = y[2] ? newlook2[7:4] : newlook2[3:0];
    assign newlook4 = y[1] ? newlook3[3:2] : newlook3[1:0];
    assign newlook5 = y[0] ? newlook4[1:1] : newlook4[0:0];
    
    assign chosen_opt = newlook5;
    
    // check if toomuch was true, and assign all zeros if so
    assign finres = toomuch ? empty : chosen_opt;
    assign z = finres;
endmodule
