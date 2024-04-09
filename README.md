# tracert_python
HomeWork for Internet Protocols curse.
Выполнил Саламахин Кирилл, студент КН-201.
Скрипт проводит трассировку tracert на Виндовс или traceroute на Linux.
Трассировка до переданного Ipv4-адреса или домена.
На пути вычисляет номер встреченной автономной системы и провайдера.
Скрипт запускается из папки source/module командой:
py main.py [(ipv4-adress) or (domain)]
Где ipv4-adress - адресс конечного сервера(74.110.80.112),
domain - домен, до которого нужно добраться(urfu.ru, vk.com).
Замечание: только один аргумент должен передаваться: либо ip, либо домен.
Если команда tracert/traceroute не смогла добраться до конечного пункта, то программа будет завершена и выведется соответствующее сообщение.

Пример работы скрипта:

1)Обычная работа:

![Right_work](https://github.com/WallKing110/tracert_python/assets/57759414/d28b3070-7b66-49a1-b4ca-a2073fab484e)

2)Не добрался до хоста:

![didntreached](https://github.com/WallKing110/tracert_python/assets/57759414/5249451f-18b4-4590-bd1c-dcca0d9f72c5)

3)Неправильный инпут:

![badinput](https://github.com/WallKing110/tracert_python/assets/57759414/9db35eae-755d-4120-bb05-7712e7361a3a)
