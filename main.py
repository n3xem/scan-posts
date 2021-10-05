from analyse import *
from icecream import ic

parse_texts = parse("卒業研究を頑張ります")
ic(extract_noun(parse_texts))
