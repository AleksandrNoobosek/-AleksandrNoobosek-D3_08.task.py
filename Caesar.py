def encrypt_caesar(msg, shift=4):
    s_sym1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    b_sym1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(s_sym1)
    s_sym2 = s_sym1[shift:] + s_sym1[:shift]
    b_sym2 = b_sym1[shift:] + b_sym1[:shift]
    translation = msg.maketrans(s_sym1 + b_sym1, s_sym2 + b_sym2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift=3):
    return encrypt_caesar(msg, -1 * shift)


msg = 'Москва Слезам не верит'
str = encrypt_caesar('Москва Слезам не верит')
print(str)
print(decrypt_caesar(str))