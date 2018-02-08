# Run this script using Monkeyrunner.

import commands
import time
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def click(device, x, y):
	device.touch(x, y, MonkeyDevice.DOWN_AND_UP)


def main():
	device = MonkeyRunner.waitForConnection()
	while True:
	 	click(device, 800, 1600)
		# click(device, 400, 1600)
		time.sleep(5)


if __name__ == '__main__':
	main()
