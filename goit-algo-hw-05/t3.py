import timeit

# --- Алгоритмы пошуку підрядка ---

def knuth_morris_pratt(text, pattern):
    def build_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = build_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return -1


def boyer_moore(text, pattern):
    def bad_char_table(pattern):
        table = {}
        for i in range(len(pattern)):
            table[pattern[i]] = i
        return table

    m = len(pattern)
    n = len(text)
    table = bad_char_table(pattern)
    s = 0

    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            bad_char_shift = table.get(text[s + j], -1)
            s += max(1, j - bad_char_shift)
    return -1


def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    h = pow(d, m-1) % q
    p = 0
    t = 0

    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

    for s in range(n - m + 1):
        if p == t:
            if text[s:s+m] == pattern:
                return s
        if s < n - m:
            t = (d * (t - ord(text[s]) * h) + ord(text[s + m])) % q
            if t < 0:
                t += q
    return -1


# --- Автоопределение кодировки и чтение файлов ---

import chardet

def read_file_detect_encoding(path):
    with open(path, 'rb') as f:
        raw = f.read()
        result = chardet.detect(raw)
        encoding = result['encoding']
        print(f"Detected encoding for {path}: {encoding}")
        return raw.decode(encoding)

text1 = read_file_detect_encoding("homework/goit-algo-hw-05/text1.txt")
text2 = read_file_detect_encoding("homework/goit-algo-hw-05/text2.txt")

# --- Шаблоны для поиска ---

pattern_exist = "структура даних"
pattern_fake = "несуществующийпідрядок123"

# --- Вимірювання часу ---

def benchmark(func, text, pattern):
    return timeit.timeit(lambda: func(text, pattern), number=100) * 1000  # ms

# --- Порівняння ---

algorithms = [
    ("Knuth-Morris-Pratt", knuth_morris_pratt),
    ("Boyer-Moore", boyer_moore),
    ("Rabin-Karp", rabin_karp),
]

for name, algo in algorithms:
    print(f"\n--- {name} ---")
    print(f"text1 | EXISTING    : {benchmark(algo, text1, pattern_exist):.2f} ms")
    print(f"text1 | FAKE        : {benchmark(algo, text1, pattern_fake):.2f} ms")
    print(f"text2 | EXISTING    : {benchmark(algo, text2, pattern_exist):.2f} ms")
    print(f"text2 | FAKE        : {benchmark(algo, text2, pattern_fake):.2f} ms")
