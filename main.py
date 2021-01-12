"""
Enigma Remake version.
@Author Xiaofeng Zhao
"""
import sys
from Alphabet import Alphabet
from Machine import Machine
from Utils import *
from Permutation import Permutation
from FixedRotor import FixedRotor
from Rotor import Rotor
from Reflector import Reflector
from MovingRotor import MovingRotor
from _io import TextIOWrapper


def read_config(config_file: TextIOWrapper):
    """
    :param config: read the configuration file.
    :return: Alphabet/num_rotors/num_pawls/all_Rotors
    """
    all_rotors = []

    alphabet_string = config_file.readline().rstrip()
    alphabet = Alphabet(alphabet_string)

    num_setting = config_file.readline().split()
    num_rotors = num_setting[0]
    num_pawls = num_setting[1]
    while True:
        line = config_file.readline()
        if line == "":
            break
        else:
            rotor = read_rotor(line, alphabet)
            all_rotors.append(rotor)
    return alphabet, num_rotors, num_pawls, all_rotors


def read_rotor(rotor_str: str, alphabet: Alphabet):
    list_str = rotor_str.split()
    name = list_str[0]
    type = list_str[1]
    cycles = ""
    for i in range(2, len(list_str)):
        cycles += list_str[i]
    perm = Permutation(cycles, alphabet)

    if type[0] == 'N':
        rotor = FixedRotor(name, perm)
    elif type[0] == 'M':
        notches = ""
        for i in range(1, len(type)):
            if type[i] in alphabet.alphabetString:
                notches += type[i]
            else:
                raise Exception("The notch is not in the alphabet string!")
        rotor = MovingRotor(name, perm, notches)
    elif type[0] == 'R':
        rotor = Reflector(name, perm)
    else:
        raise Exception("Unknown type of rotor.")

    return rotor


def process(machine: Machine, input_file: TextIOWrapper):
    coded_message = ""
    num_rotor = machine.num_rotors()
    config_flag = False
    while True:
        line = input_file.readline()
        line_list = line.split()
        if not line:
            return coded_message
        elif line == '\n':
            coded_message += '\n'
        elif line_list[0] == '*':
            machine.reset_rotors()
            machine.reset_plugboard()
            rotor_name_list = line_list[1: num_rotor + 1]
            machine.insert_all_rotors(rotor_name_list)
            machine.set_rotors(line_list[num_rotor + 1])

            machine.set_plugboard(list2str(line_list[num_rotor + 2: len(line_list)]))
            config_flag = True
        else:
            if config_flag is False:
                raise Exception("The machine is not configured!")
            else:
                coded_message += machine.convert_str(line)
                coded_message += '\n'


if __name__ == '__main__':
    """
    argv[1] is the path of configure file
    argv[2] is the the path of the input file
    argv[3] is optional; when present, it is the path of an output file.
    Otherwise, output goes to 'test/output/output.txt'
    """
    if len(sys.argv) == 3:
        config_file = open(sys.argv[1], 'r')
        input_file = open(sys.argv[2], 'r')
    elif len(sys.argv) == 4:
        config_file = open(sys.argv[1], 'r')
        input_file = open(sys.argv[2], 'r')
        output_file = sys.argv[3]
        sys.stdout = open("test/output/output.txt", 'w')
    else:
        raise Exception("The input argument must be 2 or 3!")

    alphabet, num_rotors, num_pawls, all_rotors = read_config(config_file)
    machine = Machine(alphabet, int(num_rotors), int(num_pawls), all_rotors)
    coded_message = process(machine, input_file)

    count = 1
    for i in range(len(coded_message)):
        ch = coded_message[i]
        if ch == '':
            break
        elif ch == '\n':
            print('\n', end='')
            count = 1
        elif count % 5 != 0 or (count % 5 == 0 and coded_message[i + 1] == '\n'):
            print(ch, end='')
            count += 1
        else:
            print(ch + ' ', end='')
            count = 1

    config_file.close()
    input_file.close()
    sys.stdout.close()



