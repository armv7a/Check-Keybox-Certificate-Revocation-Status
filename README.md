# Keybox 检查与删除脚本 | Keybox Check and Delete Script

此脚本用于检查指定目录中的 `keybox.xml` 文件是否已被吊销，并自动删除解析失败或证书不完整的文件。  
This script checks `keybox.xml` files in a specified directory to see if they have been revoked, and automatically deletes files that fail to parse or contain incomplete certificates.

## 功能描述 | Features

- **吊销检查**：通过从 `https://android.googleapis.com/attestation/status` 获取的吊销列表，检查每个文件的证书序列号是否在吊销列表中。
- **证书解析**：支持提取并检查文件中的 `Certificate` 标签，解析 EC 和 RSA 证书的序列号。
- **文件删除**：
  - 如果 XML 文件解析失败，自动删除该文件。
  - 如果文件证书不完整（缺少至少 4 个 `Certificate` 标签），自动删除该文件。
  - 若证书已被吊销，也会删除该文件。
  
- **Revocation Check**: Uses the revocation list from `https://android.googleapis.com/attestation/status` to check if each file's certificate serial numbers are revoked.
- **Certificate Parsing**: Extracts and checks the serial numbers of EC and RSA certificates from `Certificate` tags in each file.
- **File Deletion**:
  - Automatically deletes files that fail XML parsing.
  - Deletes files missing a minimum of 4 `Certificate` tags.
  - Deletes files with certificates that have been revoked.

## 使用说明 | Usage

1. 克隆或下载此项目。
2. 确保已安装必要的依赖库：
   ```bash
   pip install requests cryptography
   ```
3. 在终端或命令行中运行脚本，指定要检查的目录：

   ```bash
   python checkKB.py <directory>
   ```
   - `<directory>`：包含待检查 XML 文件的文件夹路径。

1. Clone or download this project.
2. Make sure required libraries are installed:
   ```bash
   pip install requests cryptography
   ```
3. Run the script from the terminal or command prompt, specifying the directory to check:

   ```bash
   python checkKB.py <directory>
   ```
   - `<directory>`: Path to the folder containing XML files to check.

## 脚本逻辑 | Script Logic

1. **文件解析**：对于每个 XML 文件，提取所有 `Certificate` 标签的内容。
2. **证书序列号检查**：解析 `Certificate` 标签中的证书，获取 EC 和 RSA 证书的序列号。
3. **吊销状态验证**：将证书序列号与吊销列表进行比对，确认证书是否被吊销。
4. **文件删除**：
   - 若文件缺少足够的 `Certificate` 标签，自动删除文件。
   - 若文件无法解析，自动删除文件。
   - 若证书在吊销列表中，删除该文件。

1. **File Parsing**: For each XML file, extracts content from all `Certificate` tags.
2. **Certificate Serial Number Check**: Parses certificates from `Certificate` tags, retrieving the serial numbers of EC and RSA certificates.
3. **Revocation Status Validation**: Cross-checks certificate serial numbers with the revocation list.
4. **File Deletion**:
   - Files with insufficient `Certificate` tags are automatically deleted.
   - Files that fail parsing are automatically deleted.
   - Files with certificates in the revocation list are deleted.

## 示例输出 | Sample Output

```
Checking C:\Users\Administrator\keybox_files\keybox_1.xml...
EC Cert SN: a1b2c3d4e5f67890
RSA Cert SN: 12345abcde67890f

Keybox in C:\Users\Administrator\keybox_files\keybox_1.xml is still valid!

Warning: C:\Users\Administrator\keybox_files\keybox_2.xml does not contain enough certificates. Deleting file...
Error: C:\Users\Administrator\keybox_files\keybox_3.xml is not a well-formed XML file. Deleting file...
Keybox in C:\Users\Administrator\keybox_files\keybox_4.xml is revoked! Deleting the file...
```

## 注意事项 | Notes

- 确保目录路径中只有 `.xml` 格式的文件，以避免不必要的错误。
- 请根据需要修改吊销列表 URL。

- Ensure that the directory path contains only `.xml` files to avoid unnecessary errors.
- Modify the revocation list URL as needed.

## 依赖库 | Dependencies

- `requests`：用于从互联网下载吊销列表。
- `cryptography`：用于解析证书序列号。
- `xml.etree.ElementTree`：用于解析 XML 文件内容。

- `requests`: Downloads the revocation list from the internet.
- `cryptography`: Parses certificate serial numbers.
- `xml.etree.ElementTree`: Parses XML file contents.

## License

MIT License
