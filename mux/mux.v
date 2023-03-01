
module mux(input a, b ,sel , output y);
 assign y=sel ? a:b;
 
 initial begin
	 $dumpfile("mux.vcd");
	 $dumpvars;
 end
 endmodule
