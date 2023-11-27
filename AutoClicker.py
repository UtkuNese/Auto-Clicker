import pyautogui
import time

def mouse_clicker(num_clicks, interval):
    print(f"Mouse Clicker başlatıldı. {num_clicks} tıklama yapılacak, {interval} saniye aralıklarla.")

    for _ in range(num_clicks):
        pyautogui.click()
        time.sleep(interval)

if __name__ == "__main__":
    try:
        num_clicks = int(input("Kaç tıklama yapmak istiyorsunuz? "))
        interval = float(input("Tıklamalar arasında kaç saniye beklemek istiyorsunuz? "))

        mouse_clicker(num_clicks, interval)
    except ValueError:
        print("Geçersiz giriş. Lütfen sayısal bir değer girin.")
