import codecs


# HEX to 64BIT function
def hexTo64bit(string):
    b64 = codecs.encode(codecs.decode(string, 'hex'), 'base64').decode()
    print(b64)


def byte_xor(ba1, ba2):

    bin_value1 = bin(int(ba1, 16))[2:]
    bin_value2 = bin(int(ba2, 16))[2:]
    print(bin_value1)
    print(bin_value2)

    desired_length = len(bin_value1) if len(
        bin_value1) > len(bin_value2) else len(bin_value2)
    bin_value1 = bin_value1.zfill(desired_length)
    bin_value2 = bin_value2.zfill(desired_length)

    print(zip(bin_value1, bin_value2))
    result = [int(bit1) ^ int(bit2)
              for bit1, bit2 in zip(bin_value1, bin_value2)]
    string_result = "".join([str(bits) for bits in result])

    return hex(int(string_result, 2))[2:]


# hexTo64bit("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
# print(byte_xor("1c0111001f010100061a024b53535009181c",
#                b"686974207468652062756c6c277320657965"))
def toChar(bin1):
    return chr(bin1)


def decimalToBinary(n):
    return bin(n).replace("0b", "")


def XOR_Int(str1, int1):
    n = 2
    arr2 = [str1[i:i+n] for i in range(0, len(str1), n)]
    arr8bit = []
    for char in arr2:
        arr8bit.append(
            (bin(int(char[0], 16))[2:] + bin(int(char[1], 16))[2:]).zfill(8))
    result = [int(bit, 2) ^ int(decimalToBinary(int1).zfill(8), 2)
              for bit in arr8bit]
    finalArray = []
    for bin1 in result:
        finalArray.append(toChar(bin1))
    print("".join(finalArray))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'


def findCypher(str):
    for i in range(180):
        XOR_Int(str, i)


findCypher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# print(str(int(f'{0x2b:0>8b}', 2) ^ int(f'{0x1b:0>8b}', 2)))
# print(str(int(f'{0x2b:0>8b}', 2)))
# print(str(int(f'{0x1b:0>8b}', 2)))
# print(f'{0x48:0>8b}')
