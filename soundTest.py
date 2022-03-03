from datetime import datetime
import warnings
import subprocess

warnings.filterwarnings('ignore')
folder = '/Users/ishandhanani/Desktop/rp_experiments/audio.mp3'

while True:
    print('Set the time of your alarm in XXXX format')
    inputted = input()
    if len(inputted) != 4:
        print('try again')
        continue
    else:
        break
hr = inputted[:2]
min = inputted[2:]
print(hr,min)
ct = datetime.now()
print(ct.hour, '\n', ct.minute)

if int(hr) == ct.hour and int(min) == ct.minute:
    subprocess.run(['open', folder], check=True)
    for i in range(10):
        print('A L A R M')

