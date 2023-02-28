`timescale 1ns/1ns
module and_gate( a, b, y);
  input a,b;
  output reg y;
  always @ (*) begin
    y = a&&b;end
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars(1);
  end
endmodule

