// Code generated by Icestudio 0.9.2w202204260904
// Thu, 28 Apr 2022 10:12:59 GMT

// Testbench template

`default_nettype none
`timescale 10 ns / 1 ns


module main_tb
;
 
 // Simulation time: 100ns (10 * 10ns)
 parameter DURATION = 10;
 
 // Input/Output
 reg Button1;
 reg Button2;
 wire LED7;
 wire LED6;
 wire [3:0] LEDs;
 wire LED5;
 wire LED4;
 
 // Module instance
 main MAIN (
  .v17b894(Button1),
  .vf8383a(Button2),
  .v7b511e(LED7),
  .v6ef206(LED6),
  .v1469d9(LEDs),
  .v6898ff(LED5),
  .v1e39f8(LED4)
 );
 
 initial begin
  // Dump vars to the output .vcd file
  $dumpvars(0, main_tb);
 
  // TODO: initialize the registers here
  // e.g. value = 1;
  // e.g. #2 value = 0;
  Button1 = 0;
  Button2 = 0;

  #5 Button1 = 1;
     Button2 = 1;
 
  #(DURATION) $display("End of simulation");
  $finish;
 end
 
endmodule
