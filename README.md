# Simple Google Dork Helper

Sebuah skrip Python sederhana untuk menghasilkan daftar query Google Dork secara otomatis berdasarkan nama domain. Program ini dirancang untuk membantu dalam tahap awal pengumpulan informasi (reconnaissance) untuk tujuan keamanan siber atau SEO.

# Instalasi

```sh
# Clone repository ini
git clone https://github.com/bintang-prayoga/dork-helper
cd dork-helper

# Cek apakah python sudah terinstall
python --version
```

# Petunjuk Penggunaan

### 1. Buka terminal

### 2. Jalankan perintah berikut

```sh
python dork_generator.py <nama_domain>
```

### 3. Contoh perintah

```sh
python dork_generator.py www.example.com
```

# Output

Skrip akan menghasilkan sebuah file bernama dorks\_<nama_domain>.txt (misal: dorks_example.com.txt) yang berisi daftar dork.

![Contoh output program](/assets/contoh_output.png)
