import sys

def generate_dorks(domain):
    
    dork_templates = [
        "site:{domain} filetype:pdf",
        "site:{domain} filetype:xls OR filetype:xlsx",
        "site:{domain} filetype:doc OR filetype:docx",
        "site:{domain} inurl:login",
        "site:{domain} inurl:admin",
        "site:{domain} intitle:\"index of\"",
        "site:{domain} intext:password",
        "site:{domain} ext:sql OR ext:db OR ext:mdb",
        "site:{domain} inurl:wp-admin",
        "site:{domain} \"-www\"",
    ]

    dorks = [template.format(domain=domain) for template in dork_templates]
    return dorks

def save_to_file(dorks, domain):
    filename = f"dorks_{domain}.txt"
    

    try:
        with open(filename, 'w') as file:
            for dork in dorks:
                file.write(dork + "\n")
        print(f"Dorks disimpan di {filename}")
    except IOError as e:
        print(f"Gagal menyimpan file: {e}")
        sys.exit(1)

def display_dorks(dorks, domain):
    print(f"\n=== Google Dork Queries untuk domain: {domain} ===")
    print("=" * 50)
    for i, dork in enumerate(dorks, 1):
        print(f"{i:2d}. {dork}")
    print("=" * 50)

def main():    
    if len(sys.argv) != 2:
        print("Penggunaan: python dork_helper.py <nama_domain>")
        print("Contoh: python dork_helper.py example.com")
        sys.exit(1) 

    domain = sys.argv[1]
        
    dorks_list = generate_dorks(domain)
    display_dorks(dorks_list, domain)
        
    while True:
        save_choice = input("\nApakah Anda ingin menyimpan daftar ini ke file txt? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes', 'ya']:
            save_to_file(dorks_list, domain)
            break
        elif save_choice in ['n', 'no', 'tidak']:
            print("Daftar dork tidak disimpan ke file.")
            break
        else:
            print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")

if __name__ == "__main__":
    main()