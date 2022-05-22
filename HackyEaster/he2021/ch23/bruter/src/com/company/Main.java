package com.company;

import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Base64;
import java.util.regex.Pattern;
import java.util.Base64;

public class Main {
    final static String alph = "abcdefghijklmnopqrstuvwxyz";
    final static String num  = "0123456789";
    public static void main(String[] args) throws IOException {
        final Pattern p = Pattern.compile("[a-z][0-9]{4}");
        final String filePath = "raw.txt";
        String r;
        r = new String(Files.readAllBytes( Paths.get(filePath) ));
        final byte[] raw = Base64.getDecoder().decode(r);
        FileWriter myWriter = new FileWriter("output.txt");
        //final byte[] egg2 = Base64.getDecoder().decode("V1cwd05XUXhjRkpRVkRBOQ==");
        //final byte[] egg1 = Base64.getDecoder().decode("NB2HI4DTHIXS653XO4XHS33VOR2WEZJOMNXW2L3XMF2GG2B7OY6XKYRYGJMGEMKDHBXXG===");


        for (int ia = 0 ; ia < 26 ; ia++ ) {
            for (int i1 = 0 ; i1 < 10 ; i1++ ) {
                String t1 = "" + alph.charAt(ia) + num.charAt(i1);
                for (int i2 = 0 ; i2 < 10 ; i2++ ) {
                    String t2 = t1 + num.charAt(i2);
                    System.out.println(t2);
                    for (int i3 = 0; i3 < 10; i3++) {
                        String t3 = t2 + num.charAt(i3);
                        for (int i4 = 0; i4 < 10; i4++) {
                            String pin = t3 + num.charAt(i4);
                            if (p.matcher(pin).matches()) {
                                //byte[] d = new byte[0];
                                try {
                                    byte[] d = Crypto.decrypt(pin, raw);
                                    myWriter.write(pin + ": ");
                                    myWriter.write(d[1]);
                                    myWriter.write(d[2]);
                                    myWriter.write(d[3]);
                                    myWriter.write("\n"); //, d[2], d[3]);
                                    if( d[1] == 'P' && d[2] == 'N' && d[3] == 'G') {
                                        System.out.println("Found solution for PIN " + pin);
                                        try (FileOutputStream stream = new FileOutputStream(pin + ".png")) {
                                            stream.write(d);
                                        }
//                                        byte[] e1 = Crypto.decrypt(pin, egg1);
//                                        try (FileOutputStream stream = new FileOutputStream("egg1.png")) {
//                                            stream.write(e1);
//                                        }
//                                        byte[] e2 = Crypto.decrypt(pin, egg2);
//                                        try (FileOutputStream stream = new FileOutputStream("egg2.png")) {
//                                            stream.write(e2);
//                                        }

                                    }
                                } catch (Exception e) {
                                    //pass; //e.printStackTrace();
                                }
                            } else {
                                System.out.println("String " + pin + " does not match pattern!");
                            }
                        }
                    }
                }
            }
        }
    }
}
