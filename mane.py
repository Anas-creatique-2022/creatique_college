#print(len("j'aime le pain de la boulangerie".split()))

phrase = "jaime le pain de la boulangerie"


def count_words(sentence):
    nombre = len(sentence.split())
    return nombre


print(" PHRASE  : ", phrase,"###########")
print(" NOMBRE DE MOT dans la phrase JAIME LE PAIN DE LA BOULANGERIE : ", count_words(phrase),"###########")

