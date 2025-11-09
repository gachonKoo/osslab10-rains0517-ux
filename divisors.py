# divisors.py
import sys

def get_divisors(n: int):
    out = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            out.append(i)
            if i != n // i:
                out.append(n // i)
        i += 1
    return sorted(out)

def main():
    if len(sys.argv) >= 2:
        n = int(sys.argv[1])           # 채점: python divisors.py 23
    else:
        n = int(sys.stdin.readline())  # (백업) 표준입력
    print(" ".join(map(str, get_divisors(n))))

if __name__ == "__main__":
    main()
