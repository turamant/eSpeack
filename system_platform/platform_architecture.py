import platform

print("Архитектура: ", platform.architecture())
print('Тип машины: ', platform.machine())
print('Cетевое имя компьютера: ', platform.node())
print('Идентификация платвормы: ', platform.platform())
print('Реальное имя процессора: ', platform.processor())
print('Номер и дата сорки пайтона: ', platform.python_build())
print('Компилятор который использовался для компиляции пайтона: ', platform.python_compiler())
print('Версия пайтона', platform.python_version())
print('Тип пайтона: ', platform.python_implementation())
print('Операционка: ', platform.system())

