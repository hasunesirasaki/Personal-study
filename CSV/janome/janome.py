from janome.tokenizer import Tokenizer
t = Tokenizer()
data = "DJの練習を1ヶ月、まじめにやってみて思い出したのは「楽しい」は「頑張る」をしなければ始まらない"
tokens = t.tokenize(data)

for token in tokens:
    if token.part_of_speech.split(",")[0] =="名詞":
        if token.part_of_speech.split(",")[1] != "非自立" and\
        token.part_of_speech.split(",")[1] != "接尾":
            print(token)
