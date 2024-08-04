import base64
default_key=7

def bitwise_xor(data, key=default_key):
    """Bitwise XOR each byte in the data with the key."""
    return bytes([b ^ key for b in data])

def encode_string(input_str, key=default_key):
    """Encode a string using base64 and bitwise XOR."""
    # Replace parts of the URL with shorter symbols
    input_str = input_str.replace("https://", "~")
    input_str = input_str.replace("terabox", "!")
    input_str = input_str.replace(".com/", "@")
    input_str = input_str.replace(".fun/", "#")


    # Convert the input string to bytes
    data = input_str.encode('utf-8')
    # Apply bitwise XOR with the key
    xor_data = bitwise_xor(data, key)
    # Encode the result using base64
    encoded_str = base64.urlsafe_b64encode(xor_data).decode('utf-8').rstrip('=')
    return encoded_str

def decode_string(encoded_str, key=default_key):
    """Decode an encoded string using base64 and bitwise XOR."""
    # Decode the base64 string
    padded_encoded_str = encoded_str + '=' * (-len(encoded_str) % 4)
    data = base64.urlsafe_b64decode(padded_encoded_str)
    # Reverse the bitwise XOR with the key
    xor_data = bitwise_xor(data, key)
    # Convert the bytes back to a string
    decoded_str = xor_data.decode('utf-8')

    # Reverse the replacements
    decoded_str = decoded_str.replace("~", "https://")
    decoded_str = decoded_str.replace("!", "terabox")
    decoded_str = decoded_str.replace("@", ".com/")
    decoded_str = decoded_str.replace("#", ".fun/")

    return decoded_str

# # Example usage
# original_string = "https://freeterabox.com/s/1xyhM8MmXjyaA06qBd4WWWg"
# key = 7  # Example key for encoding

# encoded_string = encode_string(original_string, key)
# decoded_string = decode_string(encoded_string, key)

# print(f'Original string: {original_string}')
# print(f'Encoded string: {encoded_string}')
# print(f'Decoded string: {decoded_string}')
# print(f"Encoded string length: {len(encoded_string)}")
# print(f"Original string length: {len(original_string)}")


x = "eXBwcCk2NzUzc2J1ZkdwZncodG9mdWIoYW5rYmtudHM4dHJ1azowY2R2dm9NaG80TEI0QTc1MEtsaWNW"
print(decode_string(x))