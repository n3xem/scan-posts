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


def is_noun(parse_text):
    return parse_text[1] == '名詞'


def extract_noun(parse_texts):
    return list(filter(is_noun, parse_texts))


parse_texts = parse("卒業研究を頑張ります")
ic(extract_noun(parse_texts))
