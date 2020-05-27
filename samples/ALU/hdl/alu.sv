module alu
    // two 32-bit inputs, 3-bit op-code, 32-bit output and 3 1-bit flags
    (
        input logic [31:0] x,
        input logic [31:0] y,
        input logic [2:0] op,
        output logic [31:0] z,
        output logic zero, equal, overflow
    );
    
    // logic used within the code
    logic [32:0] c;
    logic [31:0] ynew;
    logic [31:0] and_res;
    logic [31:0] add_res;
    logic [31:0] sub_res;
    logic [31:0] slt_res;
    logic [31:0] srl_res;
    logic [31:0] sra_res;
    logic [31:0] sll_res;
    logic [31:0] res_res;
    logic [4:0] res_tmp;
    logic [31:0] eq_tmp0;
    logic eq_tmp1;
    logic zer_tmp;
    logic oflw;
    logic [32:0] oflw1;
    logic temp;
	
    // values ending in "res" are used as reserved values before z is selected 
	//assigning empties for reserved value
    assign res_res = 32'b0;
    
    // find c[0] for use in adder
    assign c[0] = op[0] ? 1'b0 : 1'b1;

    // assign whether y is flipped or not based on if subtraction or addition is used
    assign ynew = op[0] ? y : ~y;
    
    // and 
    assign and_res = x & y;
    
    
    
    // use the ripple-carry adder for addition and subtraction
    add add_call (.x(x),.y(ynew), .c_in(c[0]),.z(add_res),.c(oflw1));

    
    // call module for set less than
    slt slt_call (.x(x), .y(y), .z(slt_res));
    // shift right logical
    srl srl_call (.x(x), .y(y), .z(srl_res));
    // shift right arithmetic
    sra sra_call (.x(x), .y(y), .z(sra_res));
    // shift left logical
    sll sll_call (.x(x), .y(y), .z(sll_res));
    
    
    // select z from found values 
    assign z = op[2] ? (op[1] ? (op[0] ? res_res: sll_res) : (op[0] ? sra_res : srl_res)) : (op[1] ? (op[0] ? slt_res: add_res) : (op[0] ? add_res: and_res));
    
    // check if op code is 111, which has no function
    assign temp = op[0] && op[1] && op[2];
    // reserve checker for 000, 001, 010
    assign res_tmp[0] = op[0] && op[1];
    assign res_tmp[1] = res_tmp[0] || op[2];
    // check if op is capable of overflow
    assign res_tmp[2] = !op[0] && !op[1];
    assign res_tmp[3] = !(res_tmp[1] || res_tmp[2]);
    
    // equal flag. check if all values are equal, and op-code is not reserved
    assign eq_tmp0 = ~(x ^ y);
    assign eq_tmp1 = &eq_tmp0;
    assign equal = eq_tmp1 && !temp;
    
    // zero flag. check if z is all zeros, and op-code is not reserved.
    assign zer_tmp = ~| z;
    assign zero = zer_tmp && !temp;
    
    // overflow flag. check if overflow has occurred, and op can overflow.
    assign res_tmp[4] = oflw1[31] ^ oflw1[32];
    assign overflow = res_tmp[4] && res_tmp[3];

endmodule
