import re

line = """"Ветаптека Липова Долина • Ветаптека У Липовій Долині • Ветаптеки Липова
        Долина • Ветаптеки У Липовій Долині • Ветеринарні Ліки • Вітаміни Для
        Тварин • Зоомедикація • Ветеринарні Препарати • Лікування Тварин •
        Допомога Ветеринара • Ветеринарні Консультації • Аптека Для Тварин •
        Профілактика Захворювань У Тварин • Ветеринарні Рекомендації • Ветаптека
        В Липовій Долині • Зоотовари Для Тварин • Товари Для Ветмедицини •
        Ветеринарна Аптека • Ветеринарні Клініки • Ветеринар • Ветеринарна
        Клініка • Ветеринарний Кабінет • Ветеринарні Кабінети • Ветеринарія •
        Ветеринарні Послуги • Все Для Тварин • Все Для Бджільництва •
        Акваріумістика • Ветпрепарати.
"""

line = re.sub(r' •', r',', line)

print(line)