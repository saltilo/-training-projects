"""
вычисляет время выполнения перевода или редактуры
книги в зависимости от введенного количества
авторских листов 
"""
# who = 1 for editor, 2 for traslator


def magic_formula(book, who=1):
    """
    Функция подсчета времени работы людей, логика создана учеными
    """
    transPage = 1800
    authList = 40000
    normTrans = 6
    normEdit = 1.8
    if type(book) != int or book <= 0:
        raise ValueError(f"{book} - некорректное значени")
    if who == 1:
        return book / normEdit
    else:
        return ((book * authList) / transPage) / normTrans


def day_work():  # нужен ли в этой функции какой-то return?

    # блок сичитывания количества страниц от пользователя
    book = input(
        "Что ж, рассчитаем твой дедлайн. Сколько авторских листов в книге?")
    while (not book.isdigit()) or book[0] in ("0", "-"):
        book = input("Кажется, эта книга еще не написана. Давай еще раз.")
    book = int(book)

    # блок считывания профессии от пользователя
    a = input("Если ты переводчик, введи 2, а если редактор, то 1 \n")
    while not a.isdigit() and not a in ("1", "2"):
        a = input("Промазал мимо NumLock :) Попробуй еще раз!")
    a = int(a)

    # вызов подсчета формулы
    try:
        ans = magic_formula(book, a)
    except ValueError as e:
        print("Несмотря на мои защиты в формуле что-то пошло не так."
              " Администраторы разбираются, а вы пока отдохните "
              "и попробуйте через пару минут")
        EmergencyAdministaratorCall(e, +79111234567)

    ans = round(ans)

    if len(str(ans)) >= 2 and int(str(ans)[-2:]) in (11, 12, 13, 14):
        word_ending = "дней"
    elif int(str(ans)[-1]) == 1:
        word_ending = "день"
    elif int(str(ans)[-1]) in (2, 3, 4):
        word_ending = "дня"
    else:
        word_ending = "дней"

    # вывод ответа
    if a == 1:

        print(
            f"На перевод этой книги тебе понадобится {ans:.0f} {word_ending}")
    elif a == 2:
        print(
            f"На редактирование этой книги тебе понадобится {ans:.0f} {word_ending}")


day_work()
