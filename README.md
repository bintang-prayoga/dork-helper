# Simple Google Dork Helper

Sebuah skrip Python sederhana untuk menghasilkan daftar query Google Dork secara otomatis berdasarkan nama domain. Program ini dirancang untuk membantu dalam tahap awal pengumpulan informasi (reconnaissance) untuk tujuan keamanan siber atau SEO.

# Instalasi

```sh
# Clone repository ini
$ git clone https://github.com/bintang-prayoga/dork-helper
$ cd dork-helper

# Cek apakah python sudah terinstall
$ python --version
```

# Petunjuk Penggunaan

### 1. Buka terminal

### 2. Jalankan perintah berikut

```sh
$ python dork_helper.py <nama_domain> [-h] [--categories {login,file,backup,email,sensitive,directories}
[{login,file,backup,email,sensitive,directories} ...]] [--json] [--output OUTPUT] domain
```

### 3. Contoh perintah

```sh
$ python dork_helper.py www.example.com

OR

$ python dork_helper.py example.com --categories login file

OR

$ python dork_helper.py example.com --categories backup email --json

OR

$ python dork_helper.py example.com --output my_dorks --json
```

# Output

Skrip akan menghasilkan sebuah file bernama dorks\_<nama*domain>\_date_time.txt (misal: \_dork_list_example.com_25092025_122420.txt*) yang berisi daftar dork.

Contoh hasil bisa dilihat di file _result_example.json_ dan _result_example.txt_

# License

Distributed under the MIT License. See `LICENSE` for more information.
