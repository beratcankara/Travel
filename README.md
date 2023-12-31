# Django Seyahat Uygulaması

Bu, Django ile geliştirilmiş bir seyahat uygulamasıdır. Uygulama, kullanıcıların seyahat rezervasyonları yapabilmesine ve sürücü olarak kayıt olabilmesine olanak tanır.

## Özellikler

- Kullanıcılar, seyahat rezervasyonları yapabilirler.
- Kullanıcılar, seyahat rezervasyonlarını görüntüleyebilir, düzenleyebilir ve iptal edebilirler.
- Kullanıcılar, seyahat rezervasyonlarına sürücü seçebilirler.
- Sürücüler, kayıt olarak seyahat rezervasyonlarını kabul edebilirler.
- Sürücüler, çalışma saatlerini belirleyebilirler ve müsaitlik durumlarını güncelleyebilirler.

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın:

```
git clone https://github.com/kullaniciadi/seyahat-uygulamasi.git
```

2. Proje dizinine gidin:

```
cd seyahat-uygulamasi
```

3. Sanal bir ortam oluşturun ve etkinleştirin:

```
python -m venv myenv
source myenv/bin/activate  # Linux/Mac
myenv\Scripts\activate  # Windows
```

4. Gerekli bağımlılıkları yükleyin:

```
pip install -r requirements.txt
```

5. Veritabanını oluşturun ve migrate işlemini yapın:

```
python manage.py migrate
```

6. Uygulamayı çalıştırın:

```
python manage.py runserver
```

7. Tarayıcınızda aşağıdaki URL'yi açın:

```
http://localhost:8000
```

## Kullanım

- Uygulama başlatıldığında, kullanıcılar ana sayfada seyahat rezervasyonlarına göz atabilirler.
- Kullanıcılar, rezervasyon yapmak için kayıt olmalıdır.
- Kayıtlı kullanıcılar, giriş yapabilir ve seyahat rezervasyonları yapabilirler.
- Kullanıcılar, rezervasyonlarını görüntüleyebilir, düzenleyebilir ve iptal edebilirler.
- Kullanıcılar, seyahat rezervasyonları için uygun sürücüleri seçebilirler.
- Sürücüler, kayıt olarak seyahat rezervasyonlarını kabul edebilirler.
- Sürücüler, çalışma saatlerini ve müsaitlik durumunu güncelleyebilirler.

## Katkıda Bulunma

Katkıda bulunmak için, lütfen GitHub deposunu fork edin ve yerel bir klon oluşturun. Yaptığınız değişikliklerle birlikte yeni bir dal oluşturun ve ardından değişikliklerinizi bir

 pull talebi olarak gönderin.

## Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakın.

---

## Geliştirici

- Ad: beratcankara
- E-posta: berat-can-kara@hotmail.com

---

Bu README dosyası, seyahat uygulaması için temel bir kullanım kılavuzu ve kurulum talimatlarını içermektedir. Daha fazla ayrıntı için lütfen projenin belgelerine ve kaynak koduna başvurun.
