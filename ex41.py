import random
from urllib.request import urlopen
import sys

#WORD_URL = "http://learncodethe hardway.org/words.txt"
WORD_URL = "https://learncodethehardway.org/words.txt"

WORDS = []

PHRASES = {
    "class %%%(%%%):":
     "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
     "class %%% has-a function *** that takes self and @@@ params.",
    "*** = %%%()":
     "Set *** to an instance of class %%%.",
    "***.***(@@@)":
     "From *** get the *** function, call it with the params self, @@@.",
    "***.*** = '***'":
     "From *** get the *** attribute and set it to '***'."
}

if len(sys.argv) == 2 and sys.argv[1] == 'english':
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding = "utf-8"))


def convert(snippet, phrase):
    class_names = [w.capitalize() for w in
                  random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
        random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        for word in class_names:
            result = result.replace("%%%", word, 1)

        for word in other_names:
            result = result.replace("***", word, 1)

        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)

            input(">")
            print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")

# 这是一段Python代码，它包括了一个小游戏。游戏中会输出一些Python语法的代码片段和对应的描述，玩家需要根据描述填写出正确的代码。
# 代码片段中会有一些占位符，如 "%%%"，"***"，"@@@" 等，代表需要填写的类名、函数名、参数名等等。
# 程序会随机选择一些单词来作为占位符的值，玩家需要根据这些值填写出正确的代码。
# 如果在运行游戏时在命令行参数中传入 "english" 参数，那么程序会先输出描述，然后等待用户输入代码；
# 否则程序会先输出代码片段，然后等待用户输入描述。用户可以通过 Ctrl-D 来退出游戏。
