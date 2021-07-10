#加載官方ovrelay
from pynq.overlays.base import BaseOverlay
from pynq.lib import MicroblazeLibrary
base = BaseOverlay('base.bit')
print('finish')

#打開串口(感測器1)
lib = MicroblazeLibrary(base.RPI, ['spi'])
spi1 = lib.spi_open(11, 9, -1, 8)
#device = lib.uart_open(14,15)
a = spi.read(spi1)
print(a,'psi')

#打開串口(感測器2)
lib = MicroblazeLibrary(base.RPI, ['spi'])
spi2 = lib.spi_open(11, 9, -1, 7)
#device = lib.uart_open(14,15)
b = spi.read(spi2)
print(b,'psi')

#打開串口(感測器3)
lib = MicroblazeLibrary(base.RPI, ['spi'])
spi3 = lib.spi_open(11, 9, -1, 6)
#device = lib.uart_open(14,15)
c = spi.read(spi3)
print(c,'psi')

#打開串口(感測器4)
lib = MicroblazeLibrary(base.RPI, ['spi'])
spi4 = lib.spi_open(11, 9, -1, 5)
#device = lib.uart_open(14,15)
d = spi.read(spi4)
print(d,'psi')
