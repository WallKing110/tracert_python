# tracert_python
HomeWork for Internet Protocols curse.
Выполнил Саламахин Кирилл, студент КН-201.
Скрипт проводит трассировку tracert на Виндовс или traceroute на Linux.
Трассировка до переданного Ipv4-адреса или домена.
На пути вычисляет номер встреченной автономной системы и провайдера.
Скрипт запускается командой:
py main.py [(ipv4-adress) or (domain)]
Где ipv4-adress - адресс конечного сервера(74.110.80.112),
domain - домен, до которого нужно добраться(urfu.ru, vk.com).
Замечание: только один аргумент должен передаваться: либо ip, либо домен.
Если команда tracert/traceroute не смогла добраться до конечного пункта, то программа будет завершена и выведется соответствующее сообщение.
Пример работы скрипта:
1)Обычная работа: 
![alt text](D:\Files\2 grade\Internet\HW\tracert_python\for_readme\Right_work.jpg?raw=true)
2)Не добрался до хоста:
![alt text](https://github.com/Wallking110/tracert_python/blob/develop/didntreached.jpg?raw=true)
3)Неправильный инпут:
![alt text](https://github.com/Wallking110/tracert_python/blob/develop/badinput.jpg?raw=true)
