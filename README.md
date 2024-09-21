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


# 📋 **Pertanyaan Tugas 3**

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
Screenshot hasil akses di Postman: [Hasil akses Postman](https://drive.google.com/drive/folders/1msvpEBJlnvoDAKkk3di0BXPGNjNqlUZG?usp=sharing).

# 📋 **Pertanyaan Tugas 4**

## ↗ **Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`**
Ada perbedaan diantara keduanya. Pada `HttpResponseRedirect` arugument yang di-pass hanya bisa berupa url, sementara `redirect` bisa lebih dari itu, selain url fungsi ini bisa menerima model dan view ke argumentnya. Jadi lebih fleksibel daripada yang orang-orang ekspektasikan `redirect` bisa lakukan [^4].
`HttpResponseRedirect` merupakan kelas bawaan Django yang mengembalikan respons HTTP 302 (redirect) yang mengarahkan pengguna ke URL yang ditentukan. Fungsi ini digunakan ketika kita ingin lebih eksplisit dalam mengembalikan objek redirect, yaitu saat kita ingin menggunakan URL yang secara manual dihasilkan atau diubah. Sementara `redirect` adalah fungsi Django yang lebih mudah digunakan untuk mengarahkan pengguna karena lebih nyaman dan sering digunakan di kebanyakan situasi untuk mengurangi boilerplate code[^5].

## 💙👤 **Jelaskan cara kerja penghubungan model `MoodEntry` dengan `User`!**
Pada tutorial lalu, atribut `User` ditambah pada entity `MoodEntry` untuk mengidentifikasi kepunyaan dari setiap objek `MoodEntry`. Walaupun dengan atribut `id` sudah bisa teridentifikasi, namun belum jelas tentang pengaturan kemilikan objek tersebut. `User` pada field ini sendiri adalah objek `ForeignKey` yang parameter konstruktornya di pass `django.contrib.auth.models.User` agar dapat menghandle autentikasi. Dengan adanya atribut `User` ini, terdapat perubahan besar terhadap `MoodEntry`, yaitu:
- Pada `create_mood_entry`, instead save form nya saja, kita akan save user nya juga untuk melanjutkan dan redirect
- Pada  `show_main`, `MoodEntry` sekarang di filter agar objek yang keluar adalah punya si user spesifik ini. Dari filter ini request yang di pass akan bisa dipakai property nya lewat `request.user.<property>`. 
- Ketika pengguna login dan membuat mood entry, kita dapat menyimpan entri tersebut ke database dengan menghubungkannya ke pengguna yang login.


## 🔐 **Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.**
Perbedaan antara authentication dan authorization, singkatnya authentication untuk memverifikasi identitas dari suatu user atau service, sedangkan authorization menentukan hak aksesnya. Autentikasi biasa ditemukan dalam sistem untuk mengamankan akses untuk masuk ke aplikasi dan data. Contohnya jika kita butuh akses untuk ke situs, biasanya akan diminta usernama dan password. Behind the scene, sistem akan membandingkan username dan password yang kita masukkan dengan record pada database. Jika sama, sostem akan mengasumsikan kita adalah user yang valid dan akan diberikan akses. Sementara authorization adalah untuk memberikan user izin untuk mengakses data atau melakukan aksi tertentu. Contohnya jika ke toko kopi, ada A dan B yang berbeda role. A adalah barista, maka dia hanya bisa melihat dan melayani order. Di sisi lain B, sebagai manajer, selain 2 hal tadi juga punya akses untuk melihat penjualan hari ini. Karena A dan B punya role beda, sistem akan menggunakan identitas mereka untuk memberi izin (permission) masing-masing[^6].


Saat pengguna login, terjadi autentikasi. Seperti yang tadi dijelaskan, saat autentikasi berlangsung, behind the scene, sistem akan membandingkan username dan password yang kita masukkan dengan record pada database. Jika sama, sostem akan mengasumsikan kita adalah user yang valid dan akan diberikan akses. Dalam projek Django ini, proses autentikasi akan memverifikasi beberapa credential. proses ini membutuhkan keyword argument, username, dan password pada umumnya, menecek pada backend otentikasinya, kemudian return objek `User` jika credentialnya valid, else akan di-raise PermissionDenied dan return none.


Untuk implementasi authorization, Django memiliki sistem perizinan (permission) yang built-in. Sistem ini memungkinkan untuk mengatur izin ke user atau sekelompok user yang spesifik.Sistem ini digunakan oleh Django admin site, tetapi kita bisa menggunakannya juga untuk development. Beberapa permission yang digunakan Django admin diantaranya adalah akses untuk melihat dan mengubah permission dari suatu objek, melihat "add" form, dan melihat change list[^7].


## 🍪 **Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?**
Untuk mencapai koneksi persisten antara klien dan server, suatu software akan melakukan holding state, yaitu untuk mengingat siapa yang login saat berpindah-pindah halaman pada server kita. Django menyediakan session yang memungkinkan kita menyimpan dan megambil data per visit site. Django meng-handle proses pengiriman dan penerimaan cookies, dengan cara membuat session  ID cookie pada client side, dan menyimpan semua data yang berkaitan dengan server side. jadi datanya itself tidak tersimpan pada client side. Sistem otentikasi Django di-attach ke objek request lewat session dan middleware, yang akan memnyediakan atribut `request.user` untuk semua request dari representase user[^8].


Selain mempertahankan status 'login' pada situs dan menyimpan data pada server side, Cookies juga memiliki kegunaan lain, diantaranya yaitu:
- Menyimpan informasi pembayaran agar tetap aman
- Mempersonalisasi konten yang kita lihat
- Menyimpan settings dan tema yang kita prefer
- Melacak bagaiman user berinteraksi dengan web, sehingga dari sisi developer bisa meningkatkan layanan webnya
- Menampilkan iklan yang sudah dipersonalisasi dan relevan[^9].


Saat kita menyimpan informasi kita ke cookies, by default nilai dari cookie itu transparan, bisa diubah. Kita tidak ingin cookies kita disalahgunakan, contohnya jika cookies diakses dan dimodifikasi oleh pihak yang nakal atau dikirim ke domain yang tidak seharusnya dikirim ke situ. Potensi buruk bisa dimulai dari hanya annoying — web tidak bekerja atau behavior aneh pada web — hingga kekacauan. Kriminal siber bisa saja mencuri session ID dan menggunakannya untuk mengubah agar cookie itu sakan-akan login sebagai orang lain, dan bahkan mengambil data credential sensitif seperti bank atau e-commerce. Oleh karena itu, tidak semua cookies aman, namun bisa dicegah seperti mempertinggi aware kita dan mem-blok cookie yang mencurigakan atau filter izin mana saja untuk cookie yang ingin di accept[^10].

## 🛠 **Implementasi Checklist (Step-by-Step)**

1. **Melihat apa apa saja yang akan di implementasi dari Tutorial 3**:  
   Pertama, saya mencoba untuk memahami fungsi dan cara kerja dari method dan line yang ingin ditambahkan pada Tugas 3 ini. Saya melakukan GSGS (Google sana Google sini) tantang HTTP itself, karena pada tugas ini perlu pemahaman dasar tentang cara kerjanya, holding state, cookies, dan session.

2. **Membuat Fungsi dan Form Registrasi:**
   Untuk menginisiasi pembuatan User, diperlukan credential seperti username dan password, untuk itu kita memerlukan form registrasi dan logic function untuk menghandle proses login nya. Yang pertama akan diimplementasi adalah membuat method `register(request)` pada views.py, berisi form yang digunakan untuk membuat `UserCreationForm` baru dari yang sudah di-impor sebelumnya dengan memasukkan QueryDict berdasarkan input dari user pada request.POST dan memvalidasi dan save, kemudian akan redirect halaman main:login. Namun, jika kasusnya adalah bukan request.POST atau form tidak valid, maka form nya akan di pass ke template untuk di render kembali.

   Sedangkan untuk halaman register nya akan dibuat register.html pada direktori main/templates yang meng-extend base.html, berisi yang berisi table form dan message nya. Agar path ke html ini bisa terakses perlu ditambahkan `path('register/', register, name='register')` ke dalam list urlpattern dalam urls.py.

3. **Membuat Fungsi Login dan Logout:**
   Karena kita sudah mengimplementasikan register, kita perlu juga untuk mengimplementasi login dan logout, agar bagi yang sudah mempunyai akun, bisa dapat masuk ke server lagi lewat username dan password yang telah ia buat serta dapat keluar lagi. Logic login yang dibuat mirip dengan `register` tadi. Saya menambahkan function `login_user(request)`, bedanya pada method ini sumber form nya berasal dari `AuthenticationForm`, dicek validasinya, lalu di-retrieve user lewat `get_user` dan sudah ada built-in function dari Django bernama `login` untuk membuat session jika valid dan further handling nya. Diakhiri dengan redirect ke main:show_main. Kasus dimana request bukan POST akan di handle kurang lebih sama dengan `register`.

   Lalu, untuk halaman login nya akan dibuat login.html pada direktori main/templates yang meng-extend base.html, berisi yang berisi table form dan message nya. Agar path ke html ini bisa terakses perlu ditambahkan `path('login/', login_user, name='login')` ke dalam list urlpattern dalam urls.py.

   Untuk function `logout`, saya menambahkannua di views.py juga, berisi method built-in `logout(request)` yang digunakan untuk menghapus sesi pengguna yang saat ini masuk. Kemudian redirect ke main:login. Untuk implemntasinya pada html, saya tambahkan button dan anchor mengarah ke main:logout serta membuat path nya di urls.py.

4. **Akses dan Cookies:**
   Untuk meretriksi halaman main agar hanya dapat diakses oleh pengguna yang sudah login (terautentikasi), perlu ditambahkan modifier  `login_required` tepat diatas function show_main. Lalu, untuk menggunakan data dari cookies, pada validasi di function `login`, saya menambahkan `HttpResponseRedirect` dengan parameter `reverse("main:show_main")` yang kemudian akan di set cookienya. Untuk saat ini, kita memerlukan info last login, maka yang kita pas pada setter itu adalah `str(datetime.datetime.now())`. Lalu response ini akan di return.

   Untuk menampilkan `last_login` tadi, pada context di show_main, saya tambahkan informasi `last_login` lewat property COOKIES dari parameter request. Untuk memastikan cookie tidak tercampur saat pergantian user, perlu dihapus cookies nya di function `logout_user`. Lastly, karena informasi `last_login` telah di pass dari context, jadi kita bisa akses variabel nya dari html.

5. **Menghubungkan Model Product dengan User**
   Untuk menghubungkannya, pertama dengan membuat atribut `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada model Product, jadi Product pasti terasosiasikan dengan seorang user. Product akan disesuaikan agar product yang ditampilkan adalah kepunyaan user yang sedang login dengan penyesuaian di function `create_product. Lalu pada context di function show_main saya juga menambahkan name. Untuk menyimpan perubahan model, saya melakukan migrate. 

6. **Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal:**
   Model dan produk telah terimplementasi dan terhubung, maka step ini baru bisa kita lakukan. Saya membuat akun dengan username `meong` dan `hafizh` dengan masing masing ada 3 produk yang ditambahkan.

7. **Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi:**
   Context pada `show_main` sudah mengandung informasi `last_login` dan `name`. Informasi ini saya panggil ke html pada header di web saya untuk menyapa user dan menampilkan kapan terakhir user login

   `Mau belanja apa hari ini, {{ name }}?`
   `Sesi terakhir login: {{ last_login }}`

   Untuk cookies sudah saya terapkan pada step 4.

Thanks for visiting **mauistore**! Happy shopping!

---
[^1]: https://www.linkedin.com/pulse/importance-real-time-data-delivery-enterprises-challenges-ketan-raval-nvx0f/
[^2]: https://stackoverflow.com/questions/5615352/xml-and-json-advantages-and-disadvantages
[^3]: https://www.geeksforgeeks.org/csrf-token-in-django/
[^4]: https://stackoverflow.com/questions/13304149/what-the-difference-between-using-django-redirect-and-httpresponseredirect#:~:text=There%20is%20a%20difference%20between,it%20can%20"redirect"%20to.
[^5]: https://docs.djangoproject.com/en/stable/topics/http/shortcuts/#redirect
[^6]: https://www.onelogin.com/learn/authentication-vs-authorization#:~:text=Authentication%20and%20authorization%20are%20two,authorization%20determines%20their%20access%20rights.
[^7]: https://docs.djangoproject.com/en/4.2/topics/auth/default/
[^8]: https://www.dcs.gla.ac.uk/~leif/di/tutorial/cookie.html#:~:text=Django%20provides%20a%20session%20framework,is%20not%20stored%20client%20side.
[^9]: https://www.cookieyes.com/blog/internet-cookies/#:~:text=Cookies%20are%20set%20on%20the,ad%20targeting%2C%20and%20much%20more.
[^10]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies