def main():
    txt = input("Ingrese un emoji en txt:")
    print(convert(txt))

def convert(emojiTxt):
    r = emojiTxt.replace(":)", "🙂").replace(":(", "☹️").replace("._.", "😐")
    return r

main()