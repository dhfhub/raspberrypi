import PWDServo

#sudo python3 -B PWDServo_Test.py

servo1 = PWDServo.PWDServo(18)
servo1.goHome()

for deg in range(0, 90, 1):  # 0°から90°まで動かす
	servo1.moveTo(deg)
	servo1.waitMsec(100)
	
servo1.waitMsec(500)

for deg in range(90, -90, -1):  # 90°から-90°まで動かす
	servo1.moveTo(deg)
	servo1.waitMsec(100)

servo1.waitMsec(1000)
servo1.goHome()

