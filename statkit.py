import sys

OPERATIONS = ["mean", "median"]

def mean(values):
    return sum(values) / len(values)

def main():
    op = sys.argv[1]
    nums = [float(x) for x in sys.argv[2:]]
    if op == "mean":
        print(mean(nums))
    elif op == "median":
        print(median(nums))
    else:
        print(f"Unknown operation '{op}'. Available: {OPERATIONS}")

if __name__ == "__main__":
    main()

def median(values):
    s = sorted(values)
    n = len(s)
    mid = n // 2
    if n % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2
    return s[mid]