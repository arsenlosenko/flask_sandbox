#!/usr/bin/env python3

import psutil
import getpass


def main():
    to_bytes = 100000
    cpu_times = psutil.cpu_times()
    memory_stats = psutil.virtual_memory()
    swap_stats = psutil.swap_memory()
    print("Resource stats:")
    print("="*80)
    print("CPU Time used by {}'s process: {}".format(getpass.getuser(), cpu_times.user))
    print("Virtual memory stats:\n"
          "Total: {} MB | Available : {} MB | Active : {} MB | Buffers : {} MB"
          "".format(memory_stats.total/to_bytes,
                    memory_stats.available/to_bytes,
                    memory_stats.active/to_bytes,
                    memory_stats.buffers/to_bytes))
    

if __name__ == '__main__':
    main()