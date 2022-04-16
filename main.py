import os, winreg, random

def generate():
    chars = '1234567890abcdef'
    for i in range(1):
        device_id = ''
        for i in range(53):
            device_id += random.choice(chars)
    return device_id

def change(device_id):
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'SOFTWARE\miHoYoSDK', 0, winreg.KEY_WRITE)
    winreg.SetValueEx(key, 'MIHOYOSDK_DEVICE_ID', None, winreg.REG_SZ, device_id)
    winreg.CloseKey(key)
    print(f'MIHOYOSDK_DEVICE_ID Changed, new value: {device_id}\n')
    return

change(generate())
os.system('pause')
os._exit(0)
