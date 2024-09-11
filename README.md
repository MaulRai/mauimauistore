# 📋 **Pertanyaan Tugas 2** - Django PWS Application

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

---

Thanks for visiting **mauistore**! Happy shopping!

---