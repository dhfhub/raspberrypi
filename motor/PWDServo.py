import wiringpi
#servo は VS-S092J
#1.wiringpi2のインストール
#$ sudo apt-get update
#$ sudo apt-get install python3-dev python3-pip
#$ sudo pip3 install wiringpi2
#2.wiringPi2-Pythonのインストール
#$ git clone https://github.com/Gadgetoid/WiringPi2-Python.git
#cd WiringPi2-Python
#$ sudo python3 setup.py install

class PWDServo:
	PWM_PIN = 18   # GPIOの18番ピン
	DEG_MAX = 90 # Max 90°
	DEG_MIN = -90 # Min 90°
	DEG_HOME = 0 # Home 0°
	DUTY_MAX = 115 # 90°の時
	DUTY_MIN = 38  # -90°の時
	DUTY_HOME= 77  # 0°の時
	deg = 0
	duty = 0       # Duty比の値(0から1024)
	
	def __init__(self, pin):
		self.PWM_PIN = pin
		wiringpi.wiringPiSetupGpio()   #winringPiの初期設定
		wiringpi.pinMode(self.PWM_PIN, wiringpi.GPIO.PWM_OUTPUT)
		#「Balanced」→「mark:space」Modeに変更
		wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
		# 周波数を50Hzにすると、18750/周波数=375
		wiringpi.pwmSetClock(375)
	
	def setParams(self, DEG_MAX, DEG_MIN, DEG_HOME, DUTY_MAX, DUTY_MIN, DUTY_HOME):
		self.DEG_MAX = DEG_MAX
		self.DEG_MIN = DEG_MIN
		self.DEG_HOME = DEG_HOME
		self.DUTY_MAX = DUTY_MAX
		self.DUTY_MIN = DUTY_MIN
		self.DUTY_HOME = DUTY_HOME
	
	def goHome(self):
		wiringpi.pwmWrite(self.PWM_PIN, self.DUTY_HOME)        # 0°の位置に移動
	
	def waitMsec(self, msec):
		wiringpi.delay(msec)
	
	def moveTo(self, deg):
		if deg < self.DEG_MIN :
			self.deg = self.DEG_MIN
		elif deg > self.DEG_MAX :
			self.deg = self.DEG_MAX
		else :
			self.deg = deg
		
		self.duty = int((self.DUTY_MAX - self.DUTY_MIN)*(self.deg - self.DEG_MIN)/(self.DEG_MAX - self.DEG_MIN) + self.DUTY_MIN)
		wiringpi.pwmWrite(self.PWM_PIN, self.duty)
	
