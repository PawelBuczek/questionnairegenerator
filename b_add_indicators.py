def add_indicators(s: str) -> str:  # rework it to modify the txt file
    ind = ":regional_indicator_"
    indicator_letter_dict = {1: f"{ind}a:", 2: f"{ind}b:", 3: f"{ind}c:", 4: f"{ind}d:", 5: f"{ind}e:",
                             6: f"{ind}f:", 7: f"{ind}g:", 8: f"{ind}h:", 9: f"{ind}i:", 10: f"{ind}j:",
                             11: f"{ind}k:", 12: f"{ind}l:", 13: f"{ind}m:", 14: f"{ind}n:", 15: f"{ind}o:",
                             16: f"{ind}p:", 17: f"{ind}q:", 18: f"{ind}r:", 19: f"{ind}s:", 20: f"{ind}t:",
                             21: f"{ind}u:", 22: f"{ind}v:", 23: f"{ind}w:", 24: f"{ind}x:", 25: f"{ind}y:",
                             26: f"{ind}z:"}
    for i in range(26):
        s = s.replace("\nX", f"\n{indicator_letter_dict.get(i+1)} ", 1)

    return s

def add_indicators_to_file():
    with open("questionnaire.txt", "r", encoding="utf-8") as f:
        file_content = f.read()
    with open("questionnaire.txt", "w", encoding="utf-8") as f:
        f.write(add_indicators(file_content))

if __name__ == '__main__':
    add_indicators_to_file()