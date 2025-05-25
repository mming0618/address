import hashlib
import base58

def hex_to_wif(hex_privkey, compressed=True):
    # 将十六进制字符串转为字节
    priv_key_bytes = bytes.fromhex(hex_privkey)
    
    # 添加版本字节（主网0x80）
    extended_key = b'\x80' + priv_key_bytes
    
    # 压缩格式添加后缀0x01
    if compressed:
        extended_key += b'\x01'
    
    # 计算两次SHA-256获取校验码
    first_sha256 = hashlib.sha256(extended_key).digest()
    second_sha256 = hashlib.sha256(first_sha256).digest()
    checksum = second_sha256[:4]
    
    # 拼接最终数据
    final_key = extended_key + checksum
    
    # Base58编码
    wif_key = base58.b58encode(final_key).decode('utf-8')
    return wif_key

# 示例使用
hex_private_key = "000000000000000000000000000000000000000000000000000002a221c58d8f"

# 生成未压缩WIF
uncompressed_wif = hex_to_wif(hex_private_key, compressed=False)
print("Uncompressed WIF:", uncompressed_wif)

# 生成压缩WIF
compressed_wif = hex_to_wif(hex_private_key, compressed=True)
print("Compressed WIF:", compressed_wif)
