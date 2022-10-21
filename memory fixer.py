import subprocess
def cmd(command):
    return subprocess.check_output(command, shell=True).decode('utf-8')
ram=cmd('wmic ComputerSystem get TotalPhysicalMemory | findstr /V "TotalPhysicalMemory"')
ram=int(int(ram)/1024/1024)
if ram > 16341:
    ram = 16341
ram = int(ram)
subprocess.run('wmic pagefile list /format:list')
subprocess.run(r'wmic computersystem where name="%computername%" set AutomaticManagedPagefile=false')
subprocess.run(fr'wmic pagefileset where name="C:\pagefile.sys" set InitialSize={ram},MaximumSize={ram}')
