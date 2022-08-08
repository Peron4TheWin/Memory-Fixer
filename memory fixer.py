import psutil
import os

memoria = psutil.virtual_memory()
total = memoria.total
RAM = int(total / 1024 / 1024)
os.system('bcdedit/set nx Optin')

if RAM > 16341:
    RAM = 16341

RAM = int(RAM)
os.system('wmic pagefile list /format:list')
os.system('wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false')
pre = r'C:\\pagefile.sys'
comando = f'wmic pagefileset where name="{pre}" set InitialSize={RAM},MaximumSize={RAM}'
os.system(comando)
