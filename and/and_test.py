import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure
  
@cocotb.test()
def and_test(dut):
   dut._log.info("......start of the test....")
   yield Timer(10, 'ns')
   dut._log.info("Drive 0&0 to inputs of an and gate")
   dut.a.value = 0
   dut.b.value = 0
   yield Timer(10, 'ns')

   if dut.y.value!=0:
     raise TestFailure("incorrect:%s!=0"%str(dut.y.value))
   else:
     dut._log.info("pass")
     print("......value of output y when a=0 and b=0....",dut.y.value)
     
  
   dut._log.info("Drive 0&1 to inputs of an and gate")
   dut.a.value = 0
   dut.b.value = 1

   yield Timer(10,'ns')

   if dut.y.value!=0:
     raise TestFailure("incorrect:%s!=0"%str(dut.y.value))
   else:
     dut._log.info("pass")
     print("......value of output y when a=0 and b=1....",dut.y.value)
  
    
   dut._log.info("Drive 1&0 to inputs of an and gate")
   dut.a.value = 1
   dut.b.value = 0
   yield Timer(10,'ns')

   if dut.y.value!=0:
     raise TestFailure("incorrect:%s!=0"%str(dut.y.value))
   else:
     dut._log.info("pass")
     print("......value of output y when a=1 and b=0....",dut.y.value)
    
   dut._log.info("Drive 1&1 to inputs of an and gate")
   dut.a.value = 1
   dut.b.value = 1
   yield Timer(10,'ns')

   if dut.y.value!=1:
     raise TestFailure("incorrect:%s!=1"%str(dut.y.value))
   else:
     dut._log.info("pass")
     print("......value of output y when a=1 and b=1....",dut.y.value)  
   dut._log.info(".....end of the test......")
    
    
