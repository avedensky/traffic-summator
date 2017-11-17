<h1>Traffic summator</h1>

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=KMHLMS36HC5MY&lc=RU&item_name=Traffic%20Summator%20Program&currency_code=RUB&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted)
<br>

<p>
The 'Traffic summator' program listens to the specified ip port and wait clients. After connection all traffic redirect to the specified host (ip and port are specified).
</p>

![Main Window](https://github.com/avedensky/traffic-summator/raw/master/img/scr-1.jpg)

<p>
<b>
Command syntax for start:
</b>
<br>
python3 ./summator.py -l PORT -a IPADDR -p PORT
</p>

<p>
Где:<br>
-I <b>PORT</b> - listen port<br>
-a <b>IPADDR</b> - redirect ip<br>
-p <b>PORT</b> - redirect port
-v - verbose mode
</p>

<p>
<b>For example:</b><br>
python3 ./summator.py -l 9000 -a 192.168.100.50 -p 9001
</p>

<p>
<b>For test</b><br>
You can use linux netcat utility<br>
For example: netcat 192.168.100.10 9000 (as client)<br>
For example: netcat -l 9001 (as host)<br>

Or<br> 

You can use client emulator program 'simulator-client.py' from directory
'client-emulator'. (You can starting several copy of 'simulator-client.py' for emulate several clients)<br>

For example:: python3 ./simulator-client.py -c 1 -a localhost -p 9000 (Will send to port 9000 name of the figures once a second)<br>

For example:: python3 ./simulator-client.py -c 2 -a localhost -p 9000 (Will send to port 9000 the name of the number once a second)<br>

For example:: python3 ./simulator-client.py -c 3 -a localhost -p 9000 (Will send to port 9000 colors name once a second)
</p>

<p>
<b>Autostart</b>
<br>
For autostarting you can add program to /etc/rc.local file
</p>
