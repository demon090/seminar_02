# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input('введите первое число от 1 до 1000: '))
y = int(input('введите второе число от 1 до 1000: '))
s = x + y
p = x * y
first = (s-int((s**2-4*p)**0.5))//2
second = (s+int((s**2-4*p)**0.5))//2

print(first, second)
