<h1>Traffic summator</h1>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KMHLMS36HC5MY&lc=RU&item_name=Traffic%20Summator%20Program&currency_code=RUB&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)
<br>

<p>
Программа 'Сумматор трафика' слушает заданный порт к которому клиенты, генерирующие трафик, подключаются по мере необходимости, далее весь полученный трафик программа  перенаправляет в один указанный адрес.
</p>

<p>
<b>
Для запуска использовать следущий синтаксис команды в терминале:
</b>
<br>
python3 ./summator.py -l PORT -a IPADDR -p PORT
</p>

<p>
Где:<br>
-I <b>PORT</b> - порт который слушает программа для подключения клиентов<br>
-a <b>IPADDR</b> - IP адрес куда перенаправляется трафик<br>
-p <b>PORT</b> - порт куда перенаправляется трафик
</p>

<p>
<b>Пример:</b><br>
python3 ./summator.py -l 9000 -a 192.168.100.50 -p 9001
</p>

<p>
<b>Тест</b><br>
Для теста можно притвориться клиентом, используя утилиту linux netcat.<br>
Пример: netcat 192.168.100.10 9000 (Притворимся клиентом)<br>
Пример: netcat -l 9001 (Притворимся сервером на который передаем весь трафик)<br>

Или можно использовать программу simulator-client.py из директории client-emulator для эмулирования клиентов с трафиком. (Для эмуляции нескольких клиентов необходимо запустить несколько копий simulator-client.py) <br>
Например: python3 ./simulator-client.py -c 1 -a localhost -p 9000 (Будет отсылать в порт 9000 название фигур из тектового списка раз в секунду)<br>
Например: python3 ./simulator-client.py -c 2 -a localhost -p 9000 (Будет отсылать в порт 9000 число из  тектового списка раз в секунду)<br>
Например: python3 ./simulator-client.py -c 3 -a localhost -p 9000 (Будет отсылать в порт 9000 цвет из тектового списка раз в секунду)
</p>

<p>
<b>Автозапуск</b>
Для автозапуска, вместе со стартом виртуального сервера, программу можно добавить в /etc/rc.local, записав полный путь до программы.
</p>

<p>
Для работы программы рекомендую использовать: <a href="https://www.ubuntu.com/server">ubuntu server</a><br>
 16.04(17.04) amd64
 </p>