
from simulator import Simulator


def main():
    s = Simulator(strategy='first_fit')

    s.build_blocks()
    s.build_processes()

    blocks = s.get_blocks()
    procs = s.get_processes()

    allocation_result = []
    true_allocations = 0

    for p in procs:
        ret = s.allocate(p)
        allocation_result.append((p, ret))
        if ret: 
            true_allocations += 1


    frags_info = s.generate_fragments_info()
    print('SUMMARY')
    print('{} blocks\n{} processes'.format(len(blocks), len(procs)))
    print('{} processes alocated'.format(true_allocations))
    print('{} free fragments\n{} lowest\n{} highest\n{:.2f} mean size'.
            format(frags_info[0],
                   frags_info[1],
                   frags_info[2],
                   frags_info[3]))


main()
