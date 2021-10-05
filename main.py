import MeCab
from icecream import ic


def parse(text):
    mecab = MeCab.Tagger("")
    node = mecab.parseToNode(text).next
    parse_texts = []

    while node.next:
        word = node.surface
        part_of_speech = node.feature.split(",")[0]
        parse_texts.append([word, part_of_speech])
        node = node.next

    return parse_texts


ic(parse("卒業研究を頑張ります"))
