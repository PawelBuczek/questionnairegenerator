from datetime import datetime
import calendar


def generate_questionnaire(date_iso_format: str):
    date = datetime.fromisoformat(date_iso_format)
    months_pol = {1: "styczeń", 2: "luty", 3: "marzec", 4: "kwiecień", 5: "maj", 6: "czerwiec",
                  7: "lipiec", 8: "sierpień", 9: "wrzesień", 10: "październik", 11: "listopad", 12: "grudzień"}
    months_pol_gen = {1: "stycznia", 2: "lutego", 3: "marca", 4: "kwietnia", 5: "maja", 6: "czerwca",
                      7: "lipca", 8: "sierpnia", 9: "września", 10: "października", 11: "listopada", 12: "grudnia"}

    numeral_pol = {1: "szy", 2: "gi", 3: "ci", 4: "ty", 5: "ty", 6: "ty", 7: "my", 8: "my", 9: "ty", 10: "ty", 11: "ty",
                   12: "ty", 13: "ty", 14: "ty", 15: "ty", 16: "ty", 17: "ty", 18: "ty", 19: "ty", 20: "ty", 21: "szy",
                   22: "gi", 23: "ci", 24: "ty", 25: "ty", 26: "ty", 27: "my", 28: "my", 29: "ty", 30: "ty", 31: "szy"}

    weekdays_pol = {0: "poniedziałek", 1: "wtorek", 2: "środa",
                    3: "czwartek", 4: "piątek", 5: "sobota", 6: "niedziela"}

    s = f"Potencjalne terminy sesji na {months_pol.get(date.month)}:\n"

    num_days = calendar.monthrange(date.year, date.month)[1]
    for i in range(num_days):
        s += "X   "  # this will be replaced by correct indicator after running b_add_indicators
        s += f"{i+1}-{numeral_pol.get(i+1)} "
        s += f"{months_pol_gen.get(date.month)} "
        s += f"({weekdays_pol.get(calendar.weekday(date.year, date.month, i+1))})\n"

    with open("questionnaire.txt", "w", encoding="utf-8") as f:
        f.write(s[:-1])

if __name__ == '__main__':
    generate_questionnaire("2023-10-01")