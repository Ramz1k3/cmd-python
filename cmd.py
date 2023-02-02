# cmd-python
import os
import random
import pyfiglet

result = pyfiglet.figlet_format("shirt", font = "digital" )
print(result)

a = input(f"введите язык ru или lang>")
if a == 'ru' or 'RU':
    b = "привет я ширт"
    v = "введите значение>>"
    y = "введите имя папки или файла: "
    j = "ошибка"
    m = "идентификатор пользователя текущего процесса:"
    bm = dir(os)
elif a == 'lang' or 'LANG':
    b = "Hello i shart"
    v = "enter a value>>"
    y = "enter the name of the folder or file:"
    j = "Error"
    m = "user ID of the current process:"
    bm = dir(os)



print(b)
print("введите help чтобы ознакомиться с инструкцией")
while True:
    a = input(v)
    if a == 'dir':
        dir = input(y)
        os.mkdir(dir)
    elif a == 'cd':
        sd = input(y)
        os.chdir(sd)
        print(os.getcwd)
        while True:
            a = input(f"{os.getcwd()}>>>")
            if a == 'dir':
                dir = input(y)
                os.mkdir(dir)
            elif a == 'cd':
                sd = input(y)
                os.chdir(sd)
                print(os.getcwd)
                print(os.getcwd())
            elif a == 'exit':
                os.chdir('..')
                print(os.getcwd())
            elif a == 'echo':
                bar = input("")
                print(bar)
            elif a == 'terminal name':
                print(os.getlogin())
            elif a == 'kotal':
                print(os.listdir())
            elif a == 'random':
                a = int(input("от"))
                b = int(input("до"))
                random_number = random.randint(a, b)
                print(random_number)
            elif a == 'dir/s':
                # !/usr/bin/env python
                from stat import S_ISREG, ST_CTIME, ST_MODE
                import os, sys, time

                # path to the directory (relative or absolute)
                dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

                # get all entries in the directory w/ stats
                entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
                entries = ((os.stat(path), path) for path in entries)

                # leave only regular files, insert creation date
                entries = ((stat[ST_CTIME], path)
                           for stat, path in entries if S_ISREG(stat[ST_MODE]))
                # NOTE: on Windows `ST_CTIME` is a creation date
                #  but on Unix it could be something else
                # NOTE: use `ST_MTIME` to sort by a modification date

                for cdate, path in sorted(entries):
                    print(time.ctime(cdate), os.path.basename(path))
            elif a == 'help':
                print("dir-создать папку\n"
                      "cd-перейти в деректорию или файл\n"
                      "proc-идентификатор пользователя текущего процесса\n"
                      "echo-выводит что вы напишите\n"
                      "terminal name-имя терменала\n"
                      "kotal-показывает котолог текущей дериктории\n"
                      "dir/s-показывает все файлы созданные когда либо в текущей деректории\n"
                      "dir /i-показвает опсалютно все файлы")


            else:
                print(j)


    elif a == 'proc':
        print(m,(os.getpid()))

    elif a == 'random':
        a = int(input("от: "))
        b = int(input("до: "))
        random_number = random.randint(a, b)
        print(random_number)
    elif a == 'echo':
        bar = input("")
        print(bar)
    elif a == 'terminal name':
        print(os.getlogin())
    elif a == 'kotal':
        print(os.listdir())
    elif a == 'dir/s':
        # !/usr/bin/env python
        from stat import S_ISREG, ST_CTIME, ST_MODE
        import os, sys, time

        # path to the directory (relative or absolute)
        dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

        # get all entries in the directory w/ stats
        entries = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
        entries = ((os.stat(path), path) for path in entries)

        # leave only regular files, insert creation date
        entries = ((stat[ST_CTIME], path)
                   for stat, path in entries if S_ISREG(stat[ST_MODE]))
        # NOTE: on Windows `ST_CTIME` is a creation date
        #  but on Unix it could be something else
        # NOTE: use `ST_MTIME` to sort by a modification date

        for cdate, path in sorted(entries):
            print(time.ctime(cdate), os.path.basename(path))
    elif a == 'dir /i':
        print(bm)
    elif a == 'help':
        print("<dir>-создать папку\n"
              "<cd>-перейти в деректорию или файл\n"
              "<proc>-идентификатор пользователя текущего процесса\n"
              "<echo>-выводит что вы напишите\n"
              "<terminal name>-имя терменала\n"
              "<kotal>-показывает котолог текущей дериктории\n"
              "<dir/s>-показывает все файлы созданные когда либо в текущей деректории\n"
              "<dir /i>-показвает опсалютно все файлы\n"
              "и команду нужно писать без <>"
              "этот проект я знаю говнкод ,но я пока учюсь и добавить сюда еще функций и приложений")

    else:
        print(j)

