package com.company;

//import android.util.Base64;
//import java.util.Base64;
import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

public class Crypto {
    //private static final String EGG = "V1cwd05XUXhjRkpRVkRBOQ==";

    /*
    private static byte[] encrypt(String pin, byte[] clear) throws Exception {
        byte[] salt = new byte[8];
        for (int i = 0; i < 8; i++) {
            salt[i] = (byte) i;
        }
        SecretKeySpec key = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(new PBEKeySpec(pin.toCharArray(), salt, 10000, 128)).getEncoded(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(1, key);
        return cipher.doFinal(clear);
    }

    public static byte[] decrypt(String pin, String enc64) throws Exception {
        byte[] salt = new byte[8];
        for (int i = 0; i < 8; i++) {
            salt[i] = (byte) i;
        }
        SecretKeySpec key = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(new PBEKeySpec(pin.toCharArray(), salt, 10000, 128)).getEncoded(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(2, key);
        return cipher.doFinal(Base64.getDecoder().decode(enc64));
    }
    */
    public static byte[] decrypt(String pin, byte[] raw) throws Exception {
        byte[] salt = new byte[8];
        for (int i = 0; i < 8; i++) {
            salt[i] = (byte) i;
        }
        SecretKeySpec key = new SecretKeySpec(SecretKeyFactory.getInstance("PBKDF2WithHmacSHA256").generateSecret(new PBEKeySpec(pin.toCharArray(), salt, 10000, 128)).getEncoded(), "AES");
        Cipher cipher = Cipher.getInstance("AES");
        cipher.init(2, key);
        return cipher.doFinal(raw);
    }
}