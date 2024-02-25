import numpy as np
import cv2

# 1. masukkan video yang akan proses
cap = cv2.VideoCapture('./video/video2.mp4')

width = int(cap.get(3))
height = int(cap.get(4))
frame_rate = 30.0

# 2. digunakan untuk menyimpan video yang telah diproses
out = cv2.VideoWriter('./video/hasil2.mp4', cv2.VideoWriter_fourcc(*'mp4v'), frame_rate, (width, height))

while True:
    ret, frame = cap.read()

    if not ret: break
    
    # 3. pertama-tama, video yang awalnya memiliki format warna BGR diubah menjadi HSV.
    # hal ini bertujuan untuk mempermudah proses deteksi warna karena hsv memisahkan warna, 
    # saturasi dan nilai yang mana lebih mudah daripada nilai red green blue
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)    

    # 4. menentukan batas bawah dan batas atas, warna apa yang akan diproses, pada kasus ini adalah warna lapangan (hijau)
    # angka tersebut bisa didapat dari color picker
    upperThres = np.array([60,255,255])
    lowerThres = np.array([0,95,0])

    # 5. membuat mask dimana hanya akan mengambil warna hijau pada video yang sudah di ubah menjadi hsv
    mask = cv2.inRange(hsv, lowerThres, upperThres)

    # 6. Memproses video dengan bitwise_and, dimana akan membandingkan antara video awal dengan mask yang sudah dibuat.
    # pada proses ini, output akhir akan dikeluarkan dimana video hanya mendeteksi warna hijau atau daerah di dalam lapangan
    result = cv2.bitwise_and(frame,frame, mask=mask)

    # 7. menyimpan hasil video
    out.write(result)

    # menampilkan hasil video
    cv2.imshow("frame", result)
    cv2.imshow("mask", mask)
    

    if cv2.waitKey(1) == ord('q'):
        break 

cap.release()
cv2.destroyAllWindows()