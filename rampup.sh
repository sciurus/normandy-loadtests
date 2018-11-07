for i in `seq 1 2 13`; do
	echo $i
	uptime
	molotov -q -p 8 -w $i -d 300 api_tests.py
done

echo 15
uptime
molotov -p 8 -w 15 -d 900 api_tests.py

uptime
