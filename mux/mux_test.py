import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()

async def mux_test(dut):

    dut._log.info("...start of the test...")
    await Timer(10,'ns')
    dut.a.value = 0
    dut.b.value = 0
    dut._log.info("..drive the a and b  value as 0...")
    await Timer(10,'ns')
    dut.a.value = 1
    dut.sel.value = 1
    dut._log.info('...drive the value of sel and a as 1...')
    await Timer(10,'ns')
    if dut.y.value!=1:
        raise TestFailure("....result is incorrect expected as 1 but got %d....",dut.y.value)
    else:
        dut._log.info("...pass....")
