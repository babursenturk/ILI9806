#TCON Write
import RPi.GPIO as GPIO
import time

#define macros
global BB_CS
BB_CS  = 1
global BB_SCL
BB_SCL  = 2
global BB_SDA
BB_SDA = 4
global BB_DC
BB_DC = 8

SPI_CLK 	= 15  # 15
SPI_DATA 	= 13  # 13
SPI_RESET	= 22  # 22
SPI_CS		= 37  # 37

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SPI_DATA, GPIO.OUT)
GPIO.setup(SPI_CLK, GPIO.OUT)
GPIO.setup(SPI_RESET, GPIO.OUT)
GPIO.setup(SPI_CS, GPIO.OUT)

def TCON_CLKHigh():
	GPIO.output(SPI_CLK, True)

def TCON_CLKLow():
	GPIO.output(SPI_CLK, False)

def TCON_DataLow():
	GPIO.output(SPI_DATA, False)

def TCON_DataHigh():
	GPIO.output(SPI_DATA, True)

def TCON_ResetHigh():
	GPIO.output(SPI_RESET, True)

def TCON_ResetLow():
	GPIO.output(SPI_RESET, False)

def TCON_CSHigh():
	GPIO.output(SPI_CS, True)

def TCON_CSLow():
	GPIO.output(SPI_CS, False)

def Clock_Change():
	TCON_CLKLow()
	time.sleep(1/1000000)
	TCON_CLKHigh()
	time.sleep(1/1000000)

def GfxTconSetIO(mask, level):
	if  (mask == BB_SCL):
		if (level == 1):
			TCON_CLKHigh()
		else:
			TCON_CLKLow()
	elif (mask == BB_SDA):
		if (level == 1):
			TCON_DataHigh()
		else:
			TCON_DataLow()
	elif (mask == BB_DC):
		if (level == 1):
			TCON_SetData()
		else:
			TCON_SetCommand()

def Write_Byte(value):
	mask = 128

	while mask:	#1000 0000
		if (mask & value):
			GfxTconSetIO(BB_SDA, True)
		else:
			GfxTconSetIO(BB_SDA, False)

		Clock_Change()
		mask >>= 1

def SetCommand(value):
	TCON_CSLow()
	#0
	TCON_DataLow()
	Clock_Change()
	#0
	TCON_DataLow()
	Clock_Change()
	#1
	TCON_DataHigh()
	Clock_Change()

	for i in range(5):
		TCON_DataLow() #0
		Clock_Change()

	Write_Byte(value >> 8)

	for i in range(8):
		TCON_DataLow() #0
		Clock_Change()


	Write_Byte(value & 0xFF)
	TCON_CSHigh()

def SetData(value):
	TCON_CSLow()
	#0
	TCON_DataLow()
	Clock_Change()
	#1
	TCON_DataHigh()
	Clock_Change()

	for i in range(6):
		TCON_DataLow() #0
		Clock_Change()

	Write_Byte(value)

	TCON_CSHigh()

def GfxTconInit():
	TCON_CLKHigh()
	TCON_DataHigh()
	TCON_CSHigh()

	TCON_ResetHigh()
	time.sleep(0.001)
	TCON_ResetLow()
	time.sleep(0.01)
	TCON_ResetHigh()

	time.sleep(0.12)
	SetCommand(0x1100)

	SetData(0x00)
	time.sleep(0.12)

    #//////////////////Initial CODE///////////////////////	
	SetCommand(0xFF00)
	SetData(0x77)
	SetCommand(0xFF01)
	SetData(0x01)
	SetCommand(0xFF02)
	SetData(0x00)
	SetCommand(0xFF03)
	SetData(0x00)
	SetCommand(0xFF04)
	SetData(0x10)

	SetCommand(0xC000)
	SetData(0xE9)
	SetCommand(0xC001)
	SetData(0x03)

	SetCommand(0xC100)
	SetData(0x08)
	SetCommand(0xC101)
	SetData(0x02)
	SetCommand(0xC200)
	SetData(0x31)
	SetCommand(0xC201)
	SetData(0x08)
	
	#SetCommand(0xC300)
	#SetData(0x8F)   # EP dene (8F) bir de DE dene
	
	SetCommand(0xCC00)
	SetData(0x10)


	SetCommand(0xB000)
	SetData(0X00)

	SetCommand(0xB001)
	SetData(0x0B)

	SetCommand(0xB002)
	SetData(0x10)

	SetCommand(0xB003)
	SetData(0x0D)

	SetCommand(0xB004)
	SetData(0x11)

	SetCommand(0xB005)
	SetData(0x06)

	SetCommand(0xB006)
	SetData(0x01)

	SetCommand(0xB007)
	SetData(0x08)

	SetCommand(0xB008)
	SetData(0x08)

	SetCommand(0xB009)
	SetData(0x1D)

	SetCommand(0xB00A)
	SetData(0x04)

	SetCommand(0xB00B)
	SetData(0x10)

	SetCommand(0xB00C)
	SetData(0x10)

	SetCommand(0xB00D)
	SetData(0x27)

	SetCommand(0xB00E)
	SetData(0x30)

	SetCommand(0xB00F)
	SetData(0x19)

	SetCommand(0xB100)
	SetData(0x00)

	SetCommand(0xB101)
	SetData(0x0B)

	SetCommand(0xB102)
	SetData(0x14)

	SetCommand(0xB103)
	SetData(0x0C)

	SetCommand(0xB104)
	SetData(0x11)

	SetCommand(0xB105)
	SetData(0x05)

	SetCommand(0xB106)
	SetData(0x03)

	SetCommand(0xB107)
	SetData(0x08)

	SetCommand(0xB108)
	SetData(0x08)

	SetCommand(0xB109)
	SetData(0x20)

	SetCommand(0xB10A)
	SetData(0x04)

	SetCommand(0xB10B)
	SetData(0x13)

	SetCommand(0xB10C)
	SetData(0x10)

	SetCommand(0xB10D)
	SetData(0x28)

	SetCommand(0xB10E)
	SetData(0x30)

	SetCommand(0xB10F)
	SetData(0x19)


	SetCommand(0xFF00)
	SetData(0x77)

	SetCommand(0xFF01)
	SetData(0x01)

	SetCommand(0xFF02)
	SetData(0X00)

	SetCommand(0xFF03)
	SetData(0X00)

	SetCommand(0xFF04)
	SetData(0x11)


	SetCommand(0xB000)
	SetData(0x35)
# vcom
	SetCommand(0xB100)
	SetData(0x38)
# end vcom
	SetCommand(0xB200)
	SetData(0x02)

	SetCommand(0xB300)
	SetData(0x80)

	SetCommand(0xB500)
	SetData(0x4E)

	SetCommand(0xB700)
	SetData(0x85)

	SetCommand(0xB800)
	SetData(0x20)

	SetCommand(0xB900)
	SetData(0x10)

	SetCommand(0xC100)
	SetData(0x78)

	SetCommand(0xC200)
	SetData(0x78)

	SetCommand(0xD000)
	SetData(0x88)

	time.sleep(0.1)
	
	# GIP 
	SetCommand(0xE000)
	SetData(0X00)

	SetCommand(0xE001)
	SetData(0X00)

	SetCommand(0xE002)
	SetData(0x02)


	SetCommand(0xE100)
	SetData(0x05)

	SetCommand(0xE101)
	SetData(0X00)

	SetCommand(0xE102)
	SetData(0X00)

	SetCommand(0xE103)
	SetData(0X00)

	SetCommand(0xE104)
	SetData(0x04)

	SetCommand(0xE105)
	SetData(0x00)

	SetCommand(0xE106)
	SetData(0x00)

	SetCommand(0xE107)
	SetData(0x00)

	SetCommand(0xE108)
	SetData(0x00)

	SetCommand(0xE109)
	SetData(0x20)

	SetCommand(0xE10A)
	SetData(0x20)


	SetCommand(0xE200)
	SetData(0x00)

	SetCommand(0xE201)
	SetData(0x00)

	SetCommand(0xE202)
	SetData(0x00)

	SetCommand(0xE203)
	SetData(0x00)

	SetCommand(0xE204)
	SetData(0x00)

	SetCommand(0xE205)
	SetData(0x00)

	SetCommand(0xE206)
	SetData(0x00)

	SetCommand(0xE207)
	SetData(0x00)

	SetCommand(0xE208)
	SetData(0x00)

	SetCommand(0xE209)
	SetData(0x00)

	SetCommand(0xE20A)
	SetData(0x00)

	SetCommand(0xE20B)
	SetData(0x00)

	SetCommand(0xE20C)
	SetData(0x00)


	SetCommand(0xE300)
	SetData(0x00)

	SetCommand(0xE301)
	SetData(0x00)

	SetCommand(0xE302)
	SetData(0x33)

	SetCommand(0xE303)
	SetData(0x00)


	SetCommand(0xE400)
	SetData(0x22)

	SetCommand(0xE401)
	SetData(0x00)


	SetCommand(0xE500)
	SetData(0x07)

	SetCommand(0xE501)
	SetData(0x34)

	SetCommand(0xE502)
	SetData(0xA0)

	SetCommand(0xE503)
	SetData(0xA0)

	SetCommand(0xE504)
	SetData(0x05)

	SetCommand(0xE505)
	SetData(0x34)

	SetCommand(0xE506)
	SetData(0xA0)

	SetCommand(0xE507)
	SetData(0xA0)

	SetCommand(0xE508)
	SetData(0x00)

	SetCommand(0xE509)
	SetData(0x00)

	SetCommand(0xE50A)
	SetData(0x00)

	SetCommand(0xE50B)
	SetData(0x00)

	SetCommand(0xE50C)
	SetData(0x00)

	SetCommand(0xE50D)
	SetData(0x00)

	SetCommand(0xE50E)
	SetData(0x00)

	SetCommand(0xE50F)
	SetData(0x00)


	SetCommand(0xE600)
	SetData(0x00)

	SetCommand(0xE601)
	SetData(0x00)

	SetCommand(0xE602)
	SetData(0x33)

	SetCommand(0xE603)
	SetData(0x00)


	SetCommand(0xE700)
	SetData(0x22)

	SetCommand(0xE701)
	SetData(0x00)


	SetCommand(0xE800)
	SetData(0x06)

	SetCommand(0xE801)
	SetData(0x34)

	SetCommand(0xE802)
	SetData(0xA0)

	SetCommand(0xE803)
	SetData(0xA0)

	SetCommand(0xE804)
	SetData(0x04)

	SetCommand(0xE805)
	SetData(0x34)

	SetCommand(0xE806)
	SetData(0xA0)

	SetCommand(0xE807)
	SetData(0xA0)

	SetCommand(0xE808)
	SetData(0x00)

	SetCommand(0xE809)
	SetData(0x00)

	SetCommand(0xE80A)
	SetData(0x00)

	SetCommand(0xE80B)
	SetData(0x00)

	SetCommand(0xE80C)
	SetData(0x00)

	SetCommand(0xE80D)
	SetData(0x00)

	SetCommand(0xE80E)
	SetData(0x00)

	SetCommand(0xE80F)
	SetData(0x00)


	SetCommand(0xEB00)
	SetData(0x02)

	SetCommand(0xEB01)
	SetData(0X00)

	SetCommand(0xEB02)
	SetData(0x10)

	SetCommand(0xEB03)
	SetData(0x10)

	SetCommand(0xEB04)
	SetData(0x00)

	SetCommand(0xEB05)
	SetData(0x00)

	SetCommand(0xEB06)
	SetData(0x00)


	SetCommand(0xEC00)
	SetData(0x02)

	SetCommand(0xEC01)
	SetData(0X00)


	SetCommand(0xED00)
	SetData(0xAA)

	SetCommand(0xED01)
	SetData(0x54)

	SetCommand(0xED02)
	SetData(0x0B)

	SetCommand(0xED03)
	SetData(0xBF)

	SetCommand(0xED04)
	SetData(0xFF)

	SetCommand(0xED05)
	SetData(0xFF)

	SetCommand(0xED06)
	SetData(0xFF)

	SetCommand(0xED07)
	SetData(0xFF)

	SetCommand(0xED08)
	SetData(0xFF)

	SetCommand(0xED09)
	SetData(0xFF)

	SetCommand(0xED0A)
	SetData(0xFF)

	SetCommand(0xED0B)
	SetData(0xFF)

	SetCommand(0xED0C)
	SetData(0xFB)

	SetCommand(0xED0D)
	SetData(0xB0)

	SetCommand(0xED0E)
	SetData(0x45)

	SetCommand(0xED0F)
	SetData(0xAA)

# END GIP

	SetCommand(0xFF00)
	SetData(0x77)

	SetCommand(0xFF01)
	SetData(0x01)

	SetCommand(0xFF02)
	SetData(0X00)

	SetCommand(0xFF03)
	SetData(0X00)

	SetCommand(0xFF04)
	SetData(0X00)

	SetCommand(0x2900)
	SetData(0x00)
	
	time.sleep(0.10)

	TCON_CSHigh()
	time.sleep(0.02)

	TCON_CLKLow()


GfxTconInit()
print("Init bitti RESET high")
# while True:
TCON_ResetHigh()

#for i in range	50)

#	GPIO.output(13,True)
#	time.sleep(1)
#	GPIO.output(13,False)
#	time.sleep(1)
#GPIO.cleanup()
