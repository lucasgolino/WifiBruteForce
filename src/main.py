import subprocess, string, itertools, time, thread, hashlib, sys

class cmd():
	def RunShell(self, cmd):
		return subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True).stdout.read()

class bruteForce():
	def __init__(self, mHash):
		self.hash 	= mHash
		self.thread = multithread() 

	def printPass(self, passwd):
		if passwd == self.hash:
			print "> Match Password: %s" % passwd
			time.sleep(3)
		else:
			print "> Password: %s" % passwd

	def force(self, minl, maxl):
		chars = string.letters + string.digits
		for i in xrange(minl, maxl):
			generated = ("".join(item) for item in itertools.product(*[chars], repeat=i))
			for passwd in generated:
				self.printPass(passwd)
				thread.start_new_thread(self.thread.md5Thread, (passwd, ))

class multithread():
	def __init__(self):
		self.activeThreads 	= 0
		self.lib 			= hashlib.md5()
		self.wifi 			= wifi()

	def md5Thread(self, passwd):
		self.lib.update(passwd)
		#thread.start_new_thread(self.wifi.connect, (passwd, self.lib.hexdigest(), ))

class wifi():
	def __init__(self):
		self.ssid 	= ''
		self.port 	= 'wlan0'
		self.cmd	= cmd()

		self.getInfo()
		self.configWlan()

	def getInfo(self):
		self.ssid = raw_input("> SSID: ")

	def configWlan(self):
		self.cmd.RunShell("iwconfig %s essid %s" % (self.port, self.ssid))
		self.cmd.RunShell("iwconfig %s mode managed" % self.port)
		self.cmd.RunShell("iwconfig %s channel 11" % self.port)

	def connect(self, passwd, digest):
		try:
			self.cmd.RunShell("iwconfig %s key %s" % (self.port, digest))
			try:
				self.cmd.RunShell('dhclient %s', self.port)
				self.matchPass(self, passwd, digest)
			except Exception, e:
				return "-> Error (%s)" % e

		except:
			return None


	def matchPass(self, passwd, digest):
		return sys.exit("> PASSWD - %s - (HASH: %s)" % (passwd, digest))

class main():
	def __init__(self):
		self.lenght = {'min':0, 'max':0}
		self.hash 	= ""

		self.getInfo()

		init_bf = bruteForce(self.hash)
		init_bf.force(self.lenght['min'], self.lenght['max'])

	def getInfo(self):
		self.lenght['min'] = int(raw_input("> min size: "))
		self.lenght['max'] = int(raw_input("> max size: "))
		self.hash = raw_input("> search hash: ")

main()

while 1:
	pass

