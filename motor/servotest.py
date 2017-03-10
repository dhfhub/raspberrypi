import wiringpi

#servo は VS-S092J
#sudo python3 servotest.py
#1.wiringpi2のインストール
#$ sudo apt-get update
#$ sudo apt-get install python3-dev python3-pip
#$ sudo pip3 install wiringpi2
#2.wiringPi2-Pythonのインストール
#$ git clone https://github.com/Gadgetoid/WiringPi2-Python.git
#cd WiringPi2-Python
#$ sudo python3 setup.py install


PWM_PIN = 18   # GPIOの18番ピン
DUTY_MAX = 115 # 90°の時
DUTY_MIN = 38  # -90°の時
DUTY_HOME= 77  # 0°の時
duty = 0       # Duty比の値(0から1024)

wiringpi.wiringPiSetupGpio()   #winringPiの初期設定
wiringpi.pinMode(PWM_PIN, wiringpi.GPIO.PWM_OUTPUT)
#「Balanced」→「mark:space」Modeに変更
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
# 周波数を50Hzにすると、18750/周波数=375
wiringpi.pwmSetClock(375)

wiringpi.pwmWrite(PWM_PIN, DUTY_HOME)        # 0°の位置に移動
wiringpi.delay(100) #0.1sec

for duty in range(DUTY_HOME, DUTY_MAX+1, 1):  # 0°から90°まで動かす
	wiringpi.pwmWrite(PWM_PIN, duty)
	wiringpi.delay(100) #0.1sec
wiringpi.delay(500)    #0.5sec
for duty in range(DUTY_MAX, DUTY_MIN-1, -1):  # 90°から-90°まで動かす
	wiringpi.pwmWrite(PWM_PIN, duty)
	wiringpi.delay(100)
wiringpi.delay(500)

wiringpi.pwmWrite(PWM_PIN, DUTY_HOME)        # 0°の位置に移動

