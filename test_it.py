from ukro_g2p.predict import G2P

g2p = G2P('ukro-base-uncased', cpu=True)

sentences = [
    'я хочу спитати',
    'Звича́йно на то́му яко́го подаро́вано',
]

for s in sentences:
    print(s)

    words = s.lower().split(' ')

    words_phonemes = []
    for word in words:
        word_no_accent = [it for it in word if it != '́']
        phonemes = g2p(word_no_accent)

        words_phonemes.append(''.join(phonemes))
    
    print(' '.join(words_phonemes))
