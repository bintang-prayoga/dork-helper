import sys
import datetime
import argparse
import json

def generate_dorks(domain, categories):
    """Generate Google dorks based on domain and selected categories"""

    dork_templates = {
    "login": [
        f"site:{domain} inurl:login",
        f"site:{domain} inurl:admin",
        f"site:{domain} inurl:wp-admin",
        f"site:{domain} inurl:administrator",
        f"site:{domain} inurl:auth",
        f"site:{domain} inurl:signin",
        f"site:{domain} intext:\"login\" OR intext:\"log in\"",
        f"site:{domain} intitle:\"Admin Login\"",
        f"site:{domain} inurl:cp OR inurl:controlpanel",
        f"site:{domain} inurl:dashboard",
        f"site:{domain} intitle:\"Login\" | intitle:\"Sign In\"",
        f"site:{domain} inurl:/portal/",
        f"site:{domain} inurl:/account/",
        f"site:{domain} intext:\"Forgot Password\"",
        f"site:{domain} \"Enter your username and password\"",
        f"site:{domain} inurl:userlogin",
        f"site:{domain} inurl:memberlogin",
        f"site:{domain} inurl:remote",
        f"site:{domain} inurl:cas",
        f"site:{domain} inurl:/owa/"
    ],
    "file": [
        f"site:{domain} filetype:pdf",
        f"site:{domain} filetype:xls OR filetype:xlsx",
        f"site:{domain} filetype:doc OR filetype:docx",
        f"site:{domain} filetype:ppt OR filetype:pptx",
        f"site:{domain} filetype:txt",
        f"site:{domain} filetype:csv",
        f"site:{domain} filetype:zip OR filetype:rar",
        f"site:{domain} filetype:xml",
        f"site:{domain} filetype:log",
        f"site:{domain} filetype:cfg OR filetype:conf",
        f"site:{domain} filetype:ini",
        f"site:{domain} filetype:pem OR filetype:key",
        f"site:{domain} filetype:json",
        f"site:{domain} filetype:yml OR filetype:yaml",
        f"site:{domain} filetype:sh",
        f"site:{domain} filetype:ps1",
        f"site:{domain} filetype:mdb",
        f"site:{domain} filetype:kdbx",
        f"site:{domain} filetype:rdp",
        f"site:{domain} filetype:csv intext:password"
    ],
    "backup": [
        f"site:{domain} ext:sql OR ext:db OR ext:mdb",
        f"site:{domain} ext:bak OR ext:backup",
        f"site:{domain} ext:old OR ext:orig",
        f"site:{domain} inurl:backup",
        f"site:{domain} intext:\"sql dump\"",
        f"site:{domain} filetype:sql",
        f"site:{domain} intext:\"database backup\"",
        f"site:{domain} ext:tar OR ext:gz",
        f"site:{domain} inurl:mysqldump",
        f"site:{domain} intext:\"backup\" filetype:zip",
        f"site:{domain} intext:\"Index of\" \"database.sql\"",
        f"site:{domain} inurl:dump OR inurl:dumps",
        f"site:{domain} filetype:7z \"backup\"",
        f"site:{domain} intext:\"db_backup\" OR intext:\"database_backup\"",
        f"site:{domain} \"backup of {domain}\"",
        f"site:{domain} ext:dump",
        f"site:{domain} inurl:*.sql.gz",
        f"site:{domain} intext:\"backup\" filetype:tgz",
        f"site:{domain} filetype:bzip2 OR filetype:bz2",
        f"site:{domain} \"cpanel_backup\""
    ],
    "email": [
        f"site:{domain} \"@{domain}\"",
        f"site:{domain} intext:\"email\" OR intext:\"e-mail\"",
        f"site:{domain} intext:\"contact\" \"@{domain}\"",
        f"site:{domain} intext:\"mailto:\"",
        f"site:{domain} filetype:txt intext:\"@{domain}\"",
        f"site:{domain} intext:\"support@{domain}\"",
        f"site:{domain} intext:\"admin@{domain}\"",
        f"site:{domain} intext:\"info@{domain}\"",
        f"site:{domain} inurl:contact intext:\"@\"",
        f"site:{domain} \"email list\" OR \"mailing list\"",
        f"site:{domain} filetype:pdf intext:\"@{domain}\"",
        f"site:{domain} filetype:xls intext:\"@{domain}\"",
        f"site:{domain} intext:\"*@{domain}\"",
        f"site:{domain} inurl:staff OR inurl:employees intext:\"@\"",
        f"site:{domain} \"team\" intext:\"@{domain}\"",
        f"site:{domain} filetype:doc intext:\"@{domain}\"",
        f"site:{domain} inurl:author intext:\"@{domain}\"",
        f"site:{domain} \"PGP public key\" intext:\"@{domain}\"",
        f"site:{domain} intext:\"contact us\" \"@{domain}\"",
        f"site:{domain} inurl:people intext:\"@{domain}\""
    ],
    "sensitive": [
        f"site:{domain} intext:\"password\"",
        f"site:{domain} intext:\"username\" OR intext:\"user name\"",
        f"site:{domain} intext:\"confidential\"",
        f"site:{domain} intext:\"secret\"",
        f"site:{domain} intext:\"private\"",
        f"site:{domain} intext:\"internal\"",
        f"site:{domain} ext:env",
        f"site:{domain} inurl:config",
        f"site:{domain} intext:\"api key\" OR intext:\"api_key\"",
        f"site:{domain} intext:\"access token\" OR intext:\"access_token\"",
        f"site:{domain} intext:\"aws_access_key_id\"",
        f"site:{domain} intext:\"aws_secret_access_key\"",
        f"site:{domain} intext:\"BEGIN RSA PRIVATE KEY\"",
        f"site:{domain} filetype:yml \"password:\"",
        f"site:{domain} filetype:json \"Authorization: Bearer\"",
        f"site:{domain} inurl:id_rsa OR inurl:id_dsa",
        f"site:{domain} filetype:pem intext:\"private key\"",
        f"site:{domain} intext:\"DB_PASSWORD\" ext:env",
        f"site:{domain} intext:\"client_secret\"",
        f"site:{domain} filetype:log intext:\"password\""
    ],
    "directories": [
        f"site:{domain} intitle:\"Index of\"",
        f"site:{domain} intitle:\"Directory listing\"",
        f"site:{domain} inurl:\"/.git\"",
        f"site:{domain} inurl:\"/admin/\"",
        f"site:{domain} inurl:\"/backup/\"",
        f"site:{domain} inurl:\"/uploads/\"",
        f"site:{domain} inurl:\"/files/\"",
        f"site:{domain} inurl:\"/temp/\"",
        f"site:{domain} inurl:\"/logs/\"",
        f"site:{domain} inurl:\"/test/\"",
        f"site:{domain} intitle:\"Index of /private\"",
        f"site:{domain} intitle:\"Index of /config\"",
        f"site:{domain} inurl:/wp-content/uploads/",
        f"site:{domain} intitle:\"Index of /backups\"",
        f"site:{domain} intitle:\"Index of /db\"",
        f"site:{domain} intitle:\"Index of\" \"Parent Directory\"",
        f"site:{domain} inurl:/data/",
        f"site:{domain} inurl:/assets/",
        f"site:{domain} intitle:\"Index of /secret\"",
        f"site:{domain} inurl:/inc/ OR inurl:/includes/"
    ]
}
    
    if not categories:
        categories = list(dork_templates.keys())
    
    result = {"domain": domain, "categories": {}}
    all_dorks = []
    
    for category in categories:
        if category in dork_templates:
            result["categories"][category] = dork_templates[category]
            all_dorks.extend(dork_templates[category])
    
    return result, all_dorks

def display_dorks(dorks_data, all_dorks):
    """Display dorks in console with nice formatting"""
    print(f"\n{'='*60}")
    print(f"GOOGLE DORK GENERATOR - {dorks_data['domain'].upper()}")
    print(f"{'='*60}")
    print(f"Total dorks generated: {len(all_dorks)}")
    print(f"Categories: {', '.join(dorks_data['categories'].keys())}")
    print(f"{'='*60}")
    
    counter = 1
    for category, dorks in dorks_data["categories"].items():
        print(f"\n {category.upper()} ({len(dorks)} dorks):")
        print("-" * 40)
        for dork in dorks:
            print(f"{counter:2d}. {dork}")
            counter += 1
    
    print(f"\n{'='*60}")

def save_to_file(dorks_data, all_dorks, domain, args):
    """Save dorks to file in text or JSON format"""
    timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    
    if args.output:
        base_filename = args.output.replace('.txt', '').replace('.json', '')
    else:
        base_filename = f"dork_list_{domain}_{timestamp}"
    
    try:
        if args.json:
            json_filename = f"{base_filename}.json"
            with open(json_filename, 'w', encoding='utf-8') as json_file:
                json.dump(dorks_data, json_file, indent=4, ensure_ascii=False)
            print(f" Dorks berhasil disimpan dalam format JSON: {json_filename}")
        else:
            txt_filename = f"{base_filename}.txt"
            with open(txt_filename, 'w', encoding='utf-8') as file:
                file.write(f"Google Dorks untuk domain: {domain}\n")
                file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                file.write(f"Total dorks: {len(all_dorks)}\n")
                file.write("="*60 + "\n\n")
                
                counter = 1
                for category, dorks in dorks_data["categories"].items():
                    file.write(f"[{category.upper()}] - {len(dorks)} dorks\n")
                    file.write("-" * 40 + "\n")
                    for dork in dorks:
                        file.write(f"{counter:2d}. {dork}\n")
                        counter += 1
                    file.write("\n")
            
            print(f" Dorks berhasil disimpan dalam format TXT: {txt_filename}")
            
    except IOError as e:
        print(f" Gagal menyimpan file: {e}")
        sys.exit(1)

def main():    
    parser = argparse.ArgumentParser(
        description="Google Dork Generator untuk domain tertentu.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Contoh penggunaan:
  python dork_helper.py example.com
  python dork_helper.py example.com --categories login file
  python dork_helper.py example.com --categories backup email --json
  python dork_helper.py example.com --output my_dorks --json
        """
    )
    
    parser.add_argument("domain", help="Nama domain target (misal: example.com)")
    parser.add_argument(
        "--categories", 
        nargs="+", 
        choices=["login", "file", "backup", "email", "sensitive", "directories"],
        help="Kategori dork yang diinginkan (default: semua kategori)"
    )
    parser.add_argument("--json", action="store_true", help="Output dalam format JSON")
    parser.add_argument("--output", help="Nama file output (tanpa ekstensi)")
    
    args = parser.parse_args()

    if not args.domain:
        print("Error: Domain diperlukan!")
        print("Penggunaan: python dork_helper.py <nama_domain>")
        print("Contoh: python dork_helper.py example.com")
        sys.exit(1)
    
    
    domain = args.domain.replace("http://", "").replace("https://", "").replace("www.", "")
    
    print("Generating Google dorks...")
    dorks_data, all_dorks = generate_dorks(domain, args.categories)
    
    display_dorks(dorks_data, all_dorks)
    
    while True:
        save_choice = input("\nApakah Anda ingin menyimpan daftar ini ke file? (y/n): ").lower().strip()
        if save_choice in ['y', 'yes', 'ya']:
            save_to_file(dorks_data, all_dorks, domain, args)
            break
        elif save_choice in ['n', 'no', 'tidak']:
            print("Dorks tidak disimpan ke file.")
            break
        else:
            print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

if __name__ == "__main__":
    main()