def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(*args):  # аргументы прибывают отсюда
        print("Смотри, что я получил:", *args)
        function_to_decorate(*args)

    return a_wrapper_accepting_arguments


# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции

@a_decorator_passing_arguments
def print_full_name(*args):
    print ("Меня зовут", *args)


print_full_name("Питер", "Венкман")
# выведет:
# Смотри, что я получил: Питер Венкман
# Меня зовут Питер Венкман
# *