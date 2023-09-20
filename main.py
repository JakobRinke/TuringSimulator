import turing_machine

size = 2
tape_len = 5

machine1 = turing_machine.create_random_machine(size)
tape, num, state = turing_machine.create_random_start(tape_len, size)
#tape, num, state = turing_machine.create_zero_start(10)

machine1.calc(tape, num, state, 40, True)

