# 📋 **Pertanyaan Tugas 2**

**URL Aplikasi:**
[My PWS Application](http://muhammad-raihan37-mauimauistore.pbp.cs.ui.ac.id/)

## 🛠 **Implementasi Checklist (Step-by-Step)**

1. **Membuat Proyek Django Baru**:  
   Pertama, saya membuat proyek Django baru dengan aplikasi bernama `main`. Langkah pertama yang saya lakukan adalah menginstall beberapa dependencies yang di list pada `requirements.txt`. Lalu mengatur allowed localhost dan menginisiasi git lalu push ke main. Setelah itu, saya push juga ke pws dan membuat projeknya disana.  Saya mengatur `urls.py` dan membuat model produk (`Product`) sesuai dengan kebutuhan e-commerce yang sedang saya kembangkan. Setelah itu saya berfokus untuk mulai membangun aplikasi `main` ini. Saya mendaftarkan aplikasi main ke dalam proyek, membuat templates berisi html.

2. **Menambahkan Product Model**:  
   Saya mengimplementasikan **model Product** yang menyimpan informasi terkait produk yang ditampilkan di toko online. Saya membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib yaitu String name, int price, dan String description. Saya juga menambahkan **derived property** `get_formatted_price` untuk memformat harga produk. Untuk tambahan informasi produk saya, saya juga menambahkan int rating dan int stocks.

3. **Membuat Views dan URL Routing**:  
   Selanjutnya, saya membuat `views.py` berisi fungsi `show_main` berisi context yang akan diakses pada html, dan `urls.py` di aplikasi main dan direktori projek utama yang berisis list dari url path yang diperlukan di projek saya agar tehubung dan berfungsi untuk menampilkan produk dan halaman lainnya.

4. **Mengimplementasikan HTML, CSS, dan JS**:  
   - **HTML**: Saya membuat struktur halaman yang berisi header, navigation bar, slider, dan kolom produk.
   - **CSS**: Untuk styling halaman, saya menambahkan style secara **inline** di HTML.
   - **JavaScript**: Saya mengimplementasikan **slider** untuk menampilkan produk dengan menambahkan script langsung di HTML.

5. **Menambahkan Gambar Produk**:  
   Gambar diimplementasikan menggunakan **link** agar langsung ter-render tanpa harus mengakses file lokal.

6. **Deployment ke PWS**:  
   Saya mengunggah proyek ke PWS dan mengalami beberapa masalah, namun berhasil menyelesaikannya setelah tiga kali percobaan.

7. **Menyusun README**:  
   Akhirnya, saya menulis README ini untuk menjelaskan proses implementasi secara menyeluruh.

---

## 🔄 **Bagan Request Client ke Web Aplikasi Django**

[Bagan Lucidchart](https://lucid.app/lucidchart/a4290da3-5787-4b64-b139-0a03e370075e/edit?viewport_loc=2598%2C997%2C1652%2C765%2C0_0&invitationId=inv_c628c477-0594-4954-af5b-b473867d4a54)

**Penjelasan Bagan:**
- **Models.py**: Mengatur struktur data yang akan disimpan di database.
- **Views.py**: Mengolah data dari model dan mengembalikan hasilnya ke template HTML.
- **urls.py**: Menyediakan rute untuk setiap view, menghubungkan URL dengan fungsi di views.
- **HTML**: Berfungsi sebagai template untuk menampilkan data yang dikirim dari views.

---

## 💻 **Fungsi Git dalam Pengembangan Perangkat Lunak**

Git digunakan untuk **versi kontrol**. Ini memungkinkan:
- Penyimpanan progres pengembangan ke cloud.
- Kolaborasi antar tim pengembang secara bersamaan.
- Pembuatan versi berbeda dari suatu proyek (seperti **save** dan **load**).

---

## 🚀 **Kenapa Django Dijadikan Framework Awal?**

Django dianggap sebagai framework yang:
- **Sederhana dan mudah dipelajari**: Django memberikan **struktur** yang jelas, membuatnya lebih mudah dipahami oleh pemula.
- **Straightforward**: Tanpa terlalu banyak konfigurasi rumit, memungkinkan fokus pada pemahaman **dasar-dasar pengembangan perangkat lunak**.

---

## 🧑‍💻 **Mengapa Model pada Django Disebut sebagai ORM?**

ORM (Object-Relational Mapping) adalah teknik untuk **mengkonversi data dari tabel database menjadi objek Python**. Di Django, **model** berperan sebagai ORM karena:
- **Model** memetakan data dari **database** menjadi objek Python, sehingga kita dapat berinteraksi dengan data menggunakan bahasa pemrograman, tanpa menulis SQL secara langsung.
- Django ORM menangani berbagai operasi basis data (CRUD) secara otomatis, mempermudah pengelolaan data.


## 📋 **Pertanyaan Tugas 3**

## 📦 **Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?**
Dalam mengembangkan suatu platform, ada kalanya kita perlu mengirimkan data dari satu stack ke stack lainnya. Data yang dikirimkan bisa bermacam-macam bentuknya. Data delivery memastikan data yang diperlukan tersedia secara real-time di berbagai bagian platform. Dengan ini, setiap pengguna atau sistem lain yang terhubung ke platform dapat mengakses data yang terbaru dan akurat.
Dalam platform yang besar, data biasanya tersebar di berbagai server atau lokasi. Data delivery yang efisien memastikan data dikirim dengan cara yang optimal, meminimalkan waktu trasfer data, dan mengurangi beban jaringan[^1].

## ❔**Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?**

Di banyak case, menurut saya JSON lebih baik daripada XML. JSON lebih compact dan lebih mudah untuk di load, khusunya di Javascipt. Di sisi lain XML lebih strict, namun dapat men-support schema dan namespace. Keunggulan lainnya, JSON lebih fleksibel dan lebih mudah digunakan.

JSON lebih populer dibandingkan XML karena, kembali ke alasan yang tadi, karena mudah digunakan dan lebih cepat untuk transfer data, sedangkan XML lebih kompleks[^2].


## ✅ **Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?**

Merujuk pada deskripsi dan cara kerjanya:

`Return True if the form has no errors, or False otherwise.`

Fungsi ini di integrasi pada saat kita ingin `POST` yang mana memerlukan ke-valid-an sebelum di kirim ke database untuk di proses. Hal ini untuk menghindari error saat membaca data ataupun saat mem-parse datanya. Jika data pada form sudah benar-benar valid, maka form baru di save dan dikirim.

## 🎫🛡 **Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?**

Merujuk pada tutorial 2 lalu, `csrf_token` adalah token yang berfungsi sebagai security. Token ini di-generate secara otomatis oleh Django untuk mencegah serangan berbahaya.
Token ini akan menghindari kita dari berbagai kemungkinan serangan. Saat user terautentikasi dan menjelajahi web, Django men-generate token ini yang sifatnya unik pada tiap sesi penjelajahan kita. Token ini akan dikirim pada form dan request dari user dan akan dicek pada server untuk memverifikasi request itu dari user yang terautentikasi atau dari sumber malicious. Disini, token CSRF melindungi dari serangan yang dapat mengubah data. Maka dari itu kita memerlukannya dalam membuat form pada Django.

Jika tidak ditambahkan maka berbagai serangan bisa muncul, seperti pengubahan data, penipuan, penggantian email, dan transfer of funds.

Penyerang ini dapat memanfaatkan data dari user untuk mengeksploitasinya seperti menyamar sebagai korban, mengubah data demi kepentingan penyerang, ataupun mengambil data akun di server lain lewat data credential user ini[^3].

## 🛠 **Implementasi Checklist (Step-by-Step)**

1. **Melihat apa apa saja yang akan di implementasi dari Tutorial 2**:  
   Pertama, saya mencoba untuk memahami fungsi dan cara kerja dari method dan line yang ingin ditambahkan pada Tugas 2 ini. Saya juga mencari tahu tentang Data Delivery ini. Karena checklist ini akan diimplementasikan langsung ke Tugas 1, jadi perlu ada beberapa penyesuaian yang saya rencanakan.

2. **Implementasi Skeleton sebagai Kerangka Views**:  
   Saya membuat base.html di root sebagai kerangka umum untuk halaman web lainnya di dalam projek. Lalu saya menambahkan konten 'templates' pada variabel `TEMPLATES` di settings.py. Selanjutnya me-wrap main.html yang lalu dengan block content.

3. **Mengubah Primary Key Dari Integer Menjadi UUID**:  
   Pada Data Delivery, diperlukan ID untuk mengidentidikasi objek yang disimpan pada database. Maka dari itu saya menambah property `id` yang bersifat unik pada model `Product` di models.py. Tidak lupa saya migrasikan model sebelum melihat hasilnya.

4. **Membuat Form Input Data dan Menampilkan Data**:  
   Saya akan membuat form pada HTML, namun sebelum mengimplementasikannya langsung ke html, saya perlu logic nya dulu dengan membuat form pada Django. Saya membuat forms.py yang berisi `ProductForm` yang meng-inherit ModelForm dan berisi subclass Meta. Lalu saya mengisi apa-apa saja yang saya perlukan untuk diisi user nantinya seperti "name", "price", "rating", "stock", "desc", dan "image". Setelah itu saya membuat function untuk POST data dari form dengan nama `create_product`. Fungsi ini divalidasi `form.is_valid()` yang sudah dijelaskan pada jawaban dari pertanyaan sebelumnya agar data dapat aman masuk ke database. Fungsi ini akan menghasilkan form yang dapat menambahkan data produk secara otomatis ketika data di-submit dari form. Kemudian, saya juga mengubah `show_main` dengan mem-pass product lewat context yang akan di render/kirim dan menambahkan path function create di urls.py.
   
   Untuk meng-implementasikannya secara front-end, saya membuat create_product.html dengan block content, block form, lengkap dengan csrf_token  demi keamanan, dan variabel post yang di pass Django tadi. Agar di render sebagai table, saya mengimplement nya sebagai `form.as_table`. Lalu untuk menampilkan pada main.html, saya menambahkan logic if-else, jika sudah ada product tampilkan product beserta atribut nya satu per satu dengan for-loop pada display yang saya sudah siapkan di html. Lalu saya cek hasilnya.

6. **Mengembalikan Data dalam Bentuk XML dan JSON**:  
   Untuk dapat digunakan dan diproses, data user akan diperoleh dalam bentu XML atau JSON. Maka dari itu, saya mebuat function `show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`. Fungsi-fungsi ini menerima parameter request dan jika dengan id akan meminta id juga, dan mengembalikan HttpResponse sesuai bentuk dan purpose masing-masing.

7. **Penggunaan Postman Sebagai Data Viewer**:  
   Terakhir saya mencoba untuk membuat request dengan method `GET` lewat Postman. Hasil akan di-attach pada akhir bagian Tugas 3 ini.

   ☘ **-- FITUR TAMBAHAN --**
8. **File picker untuk menambahkan gambar pada Produk**:  
   Pada model produk saya, terdapat properti `image` yang akan di isi oleh file gambar. Untuk mengimplementasinya, saya mengawali mengimport Pillow secara lokal dengan env:

   `pip install Pillow`
   
   properti `image` ini akan diisi dengan ImageField lalu pada ProductForm ditambahkan fieldnya pula.
   
   Karena request POST ini akan mem-pass file, maka pada parameter ProductForm akan ditambah request file, lalu masuk ke logic `form.is_valid()`. Kemudian untuk mengizinkan user mengunggah file-nya, pada create_product.html akan ditambahkan tag `enctype="multipart/form-data"` pada blok form. Untuk memastikan projek dapat handle file media, pada settings.py saya tambahkan line:

   `MEDIA_URL = '/media/'`
   
   `MEDIA_ROOT = os.path.join(BASE_DIR, 'media')`

   dan pada urls.py di proyek:

   `urlpatterns = [...] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)`

   Last, untuk display dari gambar yang telah diunduh, bisa di call lewat line:

   `<img src="{{ product.image.url }}" alt="{{ product.name }}" width="300">`

---

## 🖼 **Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.**
Screenshot hasil akses di Postman: https://drive.google.com/drive/u/0/folders/1msvpEBJlnvoDAKkk3di0BXPGNjNqlUZG

Thanks for visiting **mauistore**! Happy shopping!

---
[^1]: https://www.linkedin.com/pulse/importance-real-time-data-delivery-enterprises-challenges-ketan-raval-nvx0f/
[^2]: https://stackoverflow.com/questions/5615352/xml-and-json-advantages-and-disadvantages
[^3]: https://www.geeksforgeeks.org/csrf-token-in-django/
