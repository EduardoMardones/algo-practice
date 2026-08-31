# Longest Common Prefix
# Encuentra el prefijo común más largo entre un arreglo de strings.
#
# Fecha: 2026-08-31

def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ''
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ''
    return prefix


if __name__ == '__main__':
    print(longest_common_prefix(['flower', 'flow', 'flight']))  # 'fl'
    print(longest_common_prefix(['dog', 'racecar', 'car']))     # ''
