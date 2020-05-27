// set less than
// inputs x, y. outputs z. 
module slt(
    input logic [31:0] x,
    input logic [31:0] y,
    output logic [31:0] z
    );
    
    // logic used in module
    logic [32:0] oflw;
    logic [31:0] sum;
    logic [30:0] temp;
    logic new1;
    logic [31:0] y_new;
    
    // flip y
    assign y_new = ~y;
    
    // add x and y, with carry in
    add res1 (.x(x),.y(y_new),.z(sum),.c(oflw), .c_in(1));
    
    // use addition result to see if x < y
    assign temp = 31'b0;
    assign new1 = oflw[32] ? x[31] : sum[31];
    assign z = {temp,new1};
endmodule
