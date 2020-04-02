my_f = open("numbers.txt", encoding="utf-8")
content = my_f.readlines()
my_f.close()
print(content)


def changes_name(content, name_oridgin, name_cheng):
    for i in range(len(content)):
        if content[i].startswith(name_oridgin) is True:
            a = content[i].replace(name_oridgin, name_cheng)
            content.insert(i, a)
            content.pop(i + 1)


changes_name(content, name_oridgin='One', name_cheng='Один')

changes_name(content, name_oridgin='Two', name_cheng='Два')

changes_name(content, name_oridgin='Three', name_cheng='Три')

changes_name(content, name_oridgin='Four', name_cheng='Четыри')

print(content)

my_f = open("new.txt", "w", encoding="utf-8")
my_f.writelines(content)
my_f.close()