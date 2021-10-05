import MeCab
mecab = MeCab.Tagger("-Ochasen")
print(mecab.parse("卒業研究を頑張ります"))
