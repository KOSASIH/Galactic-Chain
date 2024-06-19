#include <openssl/aes.h>
#include <openssl/pem.h>

typedef struct {
    AES_KEY enc_key;
    AES_KEY dec_key;
} HEKey;

HEKey* he_generate_key() {
    HEKey* key = malloc(sizeof(HEKey));
    AES_KEY enc_key;
    AES_KEY dec_key;
    RAND_bytes(key->enc_key, sizeof(AES_KEY));
    RAND_bytes(key->dec_key, sizeof(AES_KEY));
    return key;
}

void he_encrypt(HEKey* key, unsigned char* plaintext, unsigned char* ciphertext) {
    AES_encrypt(plaintext, ciphertext, &key->enc_key);
}

void he_decrypt(HEKey* key, unsigned char* ciphertext, unsigned char* plaintext) {
    AES_decrypt(ciphertext, plaintext, &key->dec_key);
}
