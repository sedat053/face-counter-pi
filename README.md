# face-counter-pi

# Raspberry Pi Yüz Sayacı ve RFID Erişim Sistemi

## 🔍 Genel Bakış

Bu proje, **RFID kart erişim sistemi** ile **gerçek zamanlı yüz sayımı** işlevlerini birleştiren bir **Raspberry Pi** uygulamasıdır.
Sistem, yalnızca yetkili RFID kart okutulduğunda kamerayı etkinleştirir ve OpenCV kullanarak görüntüdeki yüzleri algılar ve sayar. Üç LED, sistemin durumunu görsel olarak belirtir.

---

## ⚙️ Özellikler

* **RFID Doğrulama:** Sadece izinli kart okutulduğunda sistem devreye girer.
* **Yüz Algılama ve Sayma:** OpenCV’nin Haar Cascade algoritması ile gerçek zamanlı yüz tespiti.
* **LED Göstergeleri:**

  * **LED1 (GPIO 17):** Kamera aktif durumda.
  * **LED2 (GPIO 27):** Sistem bekleme modunda (kart bekliyor).
  * **LED3 (GPIO 22):** Görüntüde yüz algılandığında yanar.
* **Canlı Görüntü:** Kamera akışı üzerinde yüz sayısı ve tespit kutuları gösterilir.
* **Klavye Kontrolü:** `q` tuşuna basarak program sonlandırılır.

---

## 🧰 Donanım Gereksinimleri

* Raspberry Pi (örnek: Raspberry Pi 4)
* PiCamera (Picamera2 kütüphanesi ile uyumlu)
* MFRC522 RFID kart okuyucu
* 3 adet LED ve direnç
* Breadboard ve jumper kablolar

---

## 🧠 Yazılım Gereksinimleri

Raspberry Pi üzerinde aşağıdaki kütüphanelerin kurulu olması gerekir:

```bash
sudo apt update
sudo apt install python3-opencv python3-gpiozero python3-picamera2 python3-rpi.gpio
pip install mfrc522
```

---

## 📁 Proje Dosya Yapısı

```
face-counter-pi/
│
├── main.py               # Ana proje dosyası
├── README.md             # Açıklama dosyası
└── requirements.txt      # (isteğe bağlı) bağımlılıklar listesi
```

Örnek `requirements.txt`:

```text
opencv-python
gpiozero
mfrc522
picamera2
RPi.GPIO
```

---

## 🚀 Çalışma Mantığı

1. **Başlangıç:**

   * LED2 yanar → Sistem RFID kart bekleme modundadır.

2. **Kart Okutma:**

   * RFID okuyucu bir kart algıladığında, kartın ID’si `izinli_kart` listesi ile karşılaştırılır.

3. **Erişim Onayı:**

   * Kart ID’si izinli listede varsa:

     * LED2 söner.
     * LED1 yanar.
     * Kamera devreye girer.
     * Yüz algılama başlar.

4. **Yüz Algılama:**

   * OpenCV Haar Cascade modeli ile yüzler tespit edilir.
   * Her tespit edilen yüz yeşil dikdörtgenle işaretlenir.
   * En az bir yüz algılandığında LED3 yanar.
   * Yüz sayısı ekranda gösterilir.

5. **Programdan Çıkış:**

   * `q` tuşuna basıldığında kamera durur, pencereler kapanır ve GPIO pinleri sıfırlanır.

---

## 🧩 Kodun Açıklaması

* `izinli_kart = [151821882918]` : Erişime izin verilen RFID kart ID’lerinin listesi.
* `Picamera2()` : Raspberry Pi kamerasını başlatır.
* `CascadeClassifier` : OpenCV’nin yüz tespit algoritmasıdır.
* `led1`, `led2`, `led3` : Kamera, bekleme ve yüz algılama durumlarını göstermek için kullanılır.
* `cv2.putText()` : Görüntü üzerinde tespit edilen yüz sayısını gösterir.
* `GPIO.cleanup()` : Program bitiminde tüm pinleri güvenli şekilde sıfırlar.

---

## 💡 Örnek Kullanım

```
Cipi okutunuz
kilit acildi
kamera devreye giriyor
```

Kamera penceresi açıldığında, yüzler yeşil çerçeveyle gösterilir ve sol üstte tespit edilen yüz sayısı yazdırılır. `q` tuşuna basıldığında sistem kapanır.

---

## ⚠️ Notlar

* `izinli_kart` listesine yeni RFID kart ID’leri eklenerek yetkilendirme genişletilebilir.
* Kamera çözünürlüğü `picam2.preview_configuration.main.size = (1280,720)` satırında değiştirilebilir.
* `haarcascade_frontalface_default.xml` dosyası OpenCV’nin varsayılan yüz tespit modelidir.
* Yüz tespiti ışık koşullarına ve kamera açısına bağlı olarak değişiklik gösterebilir.

---




