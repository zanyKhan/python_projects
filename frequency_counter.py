#------------------------Frequency counter using dictionary------------------------------

frequency = {}
def frequency_counter(container):
    unique = set(container)
    for item in unique:
        count = container.count(item)
        frequency.update({item: count})
    print(frequency)

str = "Hello"
frequency_counter(str)

lst = [1, 7,9, 7,6, 5,1,7]
frequency_counter(lst)

tpl = ( 100,0, 100 , 10, 10)
frequency_counter(tpl)

sentence = " Hello from i am from i".split()
frequency_counter(sentence)
