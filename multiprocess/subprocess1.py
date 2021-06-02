'''
lscpu  - комманда выдачи информации по CPU
'''

import subprocess

def ping(address):
    reply = subprocess.run(['ping', '-c', '3', '-n', address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return reply.stdout
    else:
        return reply.stderr


if __name__=='__main__':
    '''
    result = subprocess.run(['ls', '-ls'])
    print(result)

    ret = subprocess.run(['ping', '-c', '3', '-n', '8.8.8.8'],
                         stderr=subprocess.PIPE, encoding='utf-8')
    print("Ошибка: ", ret.stderr)
    print(ping('yandex.ru'))
    print(ping('lenta.ru'))'''
    res_CPU = subprocess.run(['lscpu'])
    print("Ошибки: ", res_CPU.stderr)
