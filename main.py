import MeCab
from icecream import ic


def parse(text):
    mecab = MeCab.Tagger()
    parseds = [[parsed.split("\t")[0], parsed.split("\t")[1].split(",")[0]]
               for parsed in mecab.parse(text).split("\n")[:-2]]
    return parseds


ic(parse("卒業研究を頑張ります"))
