import time
import subprocess 

def test_pin(pin):
  start_time = time.time()
  result= subprocess.run(["./pin_checker"], input=pin.encode(), capture_output=True)
  end_time   = time.time()
  return  end_time - start_time

pin = ""

for i in range(8):
  best=''
  max_time = 0 
  for d in '0123456789':
    attempt = pin + d + '0'*(7-i)
    time_taken = test_pin(attempt)
    if time_taken > max_time:
      max_time = time_taken
      best = d 

  pin += best 
  print(f"[+] Pin found so far: {pin}")
