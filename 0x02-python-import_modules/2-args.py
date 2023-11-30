#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number_of_arguments = len(sys.argv) - 1
    print("Number of argument(s):" + (" argument" if number_of_arguments == 1 else " arguments") + ":", end="")

    for i in range(1, number_of_arguments + 1):
            print(f"{i}: {sys.argv[i]}\n")

            if number_of_arguments == 0:
                    print("")
