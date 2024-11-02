import requests
import os
import xml.etree.ElementTree as ET
from cryptography import x509

# 获取吊销列表
crl = requests.get('https://android.googleapis.com/attestation/status', headers={'Cache-Control': 'max-age=0'}).json()

def parse_cert(cert):
    cert = "\n".join(line.strip() for line in cert.strip().split("\n"))
    parsed = x509.load_pem_x509_certificate(cert.encode())
    return f'{parsed.serial_number:x}'

def check_and_delete_if_revoked(xml_file):
    try:
        # 尝试解析XML文件
        certs = [elem.text for elem in ET.parse(xml_file).getroot().iter() if elem.tag == 'Certificate']

        # 解析证书序列号
        ec_cert_sn, rsa_cert_sn = parse_cert(certs[0]), parse_cert(certs[3])

        print(f'\nChecking {xml_file}...')
        print(f'EC Cert SN: {ec_cert_sn}\nRSA Cert SN: {rsa_cert_sn}')

        # 检查证书是否被吊销
        if any(sn in crl["entries"].keys() for sn in (ec_cert_sn, rsa_cert_sn)):
            print(f'Keybox in {xml_file} is revoked! Deleting the file...')
            os.remove(xml_file)
        else:
            print(f'Keybox in {xml_file} is still valid!')

    except ET.ParseError:
        print(f'Error: {xml_file} is not a well-formed XML file. Skipping...')

def main(directory):
    # 遍历目录下的所有XML文件
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xml'):
                xml_file = os.path.join(root, file)
                check_and_delete_if_revoked(xml_file)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python checkKB.py <directory>")
    else:
        main(sys.argv[1])
