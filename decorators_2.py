def getTalk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.capitalize() + "!"

    def whisper(word="да"):
        return word.lower() + "..."

    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper


talk = getTalk('whisper')
talk2 = getTalk('shout')

print(talk())
print(talk2())


