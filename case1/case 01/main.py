from datetime import date
import calendar

DIGITS = {
    "0": [
        " *** ",
        "*   *",
        "*   *",
        "*   *",
        " *** ",
    ],
    "1": [
        "  *  ",
        " **  ",
        "  *  ",
        "  *  ",
        " *** ",
    ],
    "2": [
        " *** ",
        "    *",
        " *** ",
        "*    ",
        "*****",
    ],
    "3": [
        "**** ",
        "    *",
        " *** ",
        "    *",
        "**** ",
    ],
    "4": [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *",
    ],
    "5": [
        "*****",
        "*    ",
        "**** ",
        "    *",
        "**** ",
    ],
    "6": [
        " *** ",
        "*    ",
        "**** ",
        "*   *",
        " *** ",
    ],
    "7": [
        "*****",
        "    *",
        "   * ",
        "  *  ",
        " *   ",
    ],
    "8": [
        " *** ",
        "*   *",
        " *** ",
        "*   *",
        " *** ",
    ],
    "9": [
        " *** ",
        "*   *",
        " ****",
        "    *",
        " *** ",
    ],
}

WEEKDAYS = {
    0: "понедельник",
    1: "вторник",
    2: "среда",
    3: "четверг",
    4: "пятница",
    5: "суббота",
    6: "воскресенье",
}


def get_birth_date() -> date:
    """Запрашивает дату рождения и проверяет корректность введённых данных."""
    while True:
        try:
            day = int(input("Введите день рождения: "))
            month = int(input("Введите месяц рождения: "))
            year = int(input("Введите год рождения: "))
            return date(year, month, day)
        except ValueError:
            print("Дата введена неверно. Попробуйте ещё раз.\n")



def get_weekday_name(birth_date: date) -> str:
    return WEEKDAYS[birth_date.weekday()]



def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)



def get_age(birth_date: date) -> int:
    today = date.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age



def print_stylized_date(birth_date: date) -> None:
    """Выводит дату в формате дд мм гггг, где цифры нарисованы звёздочками."""
    formatted = birth_date.strftime("%d%m%Y")
    groups = [formatted[:2], formatted[2:4], formatted[4:]]

    print("\nДата рождения в стилизованном виде:\n")
    for row in range(5):
        parts = []
        for group in groups:
            parts.append(" ".join(DIGITS[d][row] for d in group))
        print("   ".join(parts))



def main() -> None:
    birth_date = get_birth_date()

    print(f"\nВы родились в {get_weekday_name(birth_date)}.")
    print("Год был високосным." if is_leap_year(birth_date.year) else "Год не был високосным.")
    print(f"Сейчас вам {get_age(birth_date)} полных лет.")

    print_stylized_date(birth_date)


if __name__ == "__main__":
    main()
