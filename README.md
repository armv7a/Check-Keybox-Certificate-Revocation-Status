以下是适合您提供代码的 `README.md` 文件，其中包含中英双语说明：

---

# Check Keybox Certificate Revocation Status / 检查 Keybox 证书吊销状态

This script checks XML files in a specified directory to determine if any Keybox certificates have been revoked according to an online revocation list (CRL). If any certificate is found to be revoked, the corresponding XML file is deleted.

本脚本用于检查指定目录下的 XML 文件，以确定是否有 Keybox 证书已被吊销。检查基于一个在线吊销列表 (CRL)。如果发现任何证书被吊销，将会删除相应的 XML 文件。

## Requirements / 依赖

- `requests`: Used to retrieve the revocation list (CRL) from an online source.
- `cryptography`: Used to parse and analyze certificates within XML files.

请确保已安装以下依赖库：
- `requests`：用于从在线来源获取吊销列表 (CRL)。
- `cryptography`：用于解析和分析 XML 文件中的证书。

```bash
pip install requests cryptography
```

## Usage / 用法

```bash
python checkKB.py <directory>
```

- `<directory>`: The path to the directory containing the XML files to check.
- `<directory>`：包含要检查的 XML 文件的目录路径。

### Example / 示例

```bash
python checkKB.py /path/to/xml/files
```

## Code Explanation / 代码说明

### Functions / 函数

- **`parse_cert(cert)`**: Parses a PEM-formatted certificate and returns its serial number in hexadecimal format.
  
  解析 PEM 格式的证书并返回其序列号（十六进制格式）。

- **`check_and_delete_if_revoked(xml_file)`**: Parses an XML file, extracts Keybox certificates, and checks them against the CRL. If any certificate is revoked, deletes the XML file.
  
  解析 XML 文件，提取 Keybox 证书，并与吊销列表 (CRL) 进行比对。如果证书已被吊销，则删除 XML 文件。

- **`main(directory)`**: Iterates through all XML files in a specified directory and calls `check_and_delete_if_revoked` on each.
  
  遍历指定目录下的所有 XML 文件，并对每个文件调用 `check_and_delete_if_revoked` 函数。

### Notes / 注意事项

- Ensure that the directory specified contains XML files with `Certificate` tags for correct parsing.
- 请确保指定的目录包含带有 `Certificate` 标签的 XML 文件，以便正确解析。

---

