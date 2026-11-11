import sys
import unittest

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Import test modules
import tests.test_machine as tm
import tests.test_analyzer as ta
import tests.test_diagonal as td
import tests.test_tm as ttm
import tests.test_soundness_sweep as tss

class TestMachine(unittest.TestCase):
    def test_compiler_basic(self): tm.test_compiler_basic()
    def test_machine_countdown(self): tm.test_machine_countdown()
    def test_machine_cycle_detection(self): tm.test_machine_cycle_detection()
    def test_k_bit_overflow(self): tm.test_k_bit_overflow()

class TestAnalyzer(unittest.TestCase):
    def test_static_while_true(self): ta.test_static_while_true()
    def test_static_ranking_countdown(self): ta.test_static_ranking_countdown()
    def test_static_recurrent_divergence(self): ta.test_static_recurrent_divergence()
    def test_static_step_divisibility(self): ta.test_static_step_divisibility()
    def test_gcd_zero_bug(self): ta.test_gcd_zero_bug()

class TestDiagonal(unittest.TestCase):
    def test_adversaries(self): td.test_all_diagonal_adversaries_cause_contradiction()

class TestTM(unittest.TestCase):
    def test_binary_inc(self): ttm.test_tm_binary_incrementer()
    def test_ping_pong(self): ttm.test_tm_ping_pong_cycle()
    def test_runaway(self): ttm.test_tm_runaway_unknown()

class TestSweep(unittest.TestCase):
    def test_soundness(self): tss.test_soundness_sweep_2500_programs()

suite.addTests(loader.loadTestsFromTestCase(TestMachine))
suite.addTests(loader.loadTestsFromTestCase(TestAnalyzer))
suite.addTests(loader.loadTestsFromTestCase(TestDiagonal))
suite.addTests(loader.loadTestsFromTestCase(TestTM))
suite.addTests(loader.loadTestsFromTestCase(TestSweep))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
sys.exit(0 if result.wasSuccessful() else 1)
