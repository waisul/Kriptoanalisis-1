/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package replace_text;
import java.util.Scanner;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

/**
 *
 * @author Ericco
 */
public class Replace_text {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         Scanner key=new Scanner(System.in);
        
        String cipher;
        System.out.print("Masukkan Ciphertext : ");
        cipher=key.nextLine();
        
        char[] huruf = cipher.toCharArray();
        int panjang = huruf.length;
        String huruf1, huruf2;
        
        System.out.print("Huruf yang diganti : ");
        huruf1=key.next();
        System.out.print("Huruf pengganti : ");
        huruf2=key.next();

        try{
            File hasil = new File("hasil.txt"); 
            try (PrintWriter pr = new PrintWriter(new FileWriter(hasil))) {
                pr.print("Hasil find dan replace : " +cipher.replace(huruf1, huruf2));
                pr.close();
            }
            System.out.println("Berhasil");
        }catch(IOException e){
            System.out.print("Gagal");
        }
    }
}

