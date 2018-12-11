import src.encryptor as encryptor

# English letters frequency
frequencies = {
    "a": 0.0817,
    "b": 0.0149,
    "c": 0.0278,
    "d": 0.0425,
    "e": 0.127,
    "f": 0.0229,
    "g": 0.0202,
    "h": 0.0609,
    "i": 0.0697,
    "j": 0.0015,
    "k": 0.0077,
    "l": 0.0403,
    "m": 0.0241,
    "n": 0.0675,
    "o": 0.0751,
    "p": 0.0193,
    "q": 0.001,
    "r": 0.0599,
    "s": 0.0633,
    "t": 0.0906,
    "u": 0.0276,
    "v": 0.0098,
    "w": 0.0236,
    "x": 0.0015,
    "y": 0.0197,
    "z": 0.0007
}


def frequency_analysis(text, key):
    test_frequency = {}
    text = encryptor.crypt(text, key)
    for letter in text:
        letter = letter.lower()
        if letter in frequencies and letter not in test_frequency:
            test_frequency[letter] = text.count(letter)/len(text)
    delta = 0
    for key, value in test_frequency.items():
        delta += abs(frequencies[key] - value)
    return delta


def analysis(text):
    keys = {}
    for i in range(1, len(encryptor.alphabet)):
        keys[i] = frequency_analysis(text, -i)
    sorted_keys = sorted(keys.items(), key=lambda kv: kv[1])
    return sorted_keys[0][0]


def decrypt():
    text = encryptor.read_file(encryptor.cipher_url)
    key = analysis(text)
    open_text = encryptor.crypt(text, -key)
    encryptor.write_file(encryptor.open_text_url, open_text)
    print("Decrypted with key", key)


if __name__ == '__main__':
    decrypt()


