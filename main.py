import turing_machine

size = 50
tape_len = 30

machine1 = turing_machine.create_random_machine(size)
#tape, num, state = turing_machine.create_random_start(tape_len, size)
tape, num, state = turing_machine.create_zero_start(tape_len)

machine1.calc(tape, num, state, 100, True)

