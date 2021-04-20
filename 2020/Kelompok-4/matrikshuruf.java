/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package huruf;
import java.util.Scanner;

/**
 *
 * @author User
 */
public class matrikshuruf {
    public static void main(String[] args){
        Scanner key=new Scanner(System.in);
        
        String kalimat;
        System.out.print("Masukkan Kalimat : ");
        kalimat=key.nextLine();
        
        char[] huruf = kalimat.toCharArray();//memasukkan kalimat kedalam array huruf
        int panjangKalimat = huruf.length;//menyimpan banyaknya huruf/space
        
        int i,j,k;
        //perulangan untuk membuat matriks hingga menjadi sederet kalimat awal
        for (i=2; i<=panjangKalimat; i++){ //i=2 agar bisa mulai dari 2 kolom 
            int a;//menyimpan batas untuk banyak baris yang diperlukan
            int b=0;
            int c=i;//menyimpan nilai i jika semua huruf sudah tertampung kedalam matriks
            //membuat batas untuk barisnya
            if (panjangKalimat%i==0){
                a=panjangKalimat/i;
            }
            else{
                a=panjangKalimat/i+1;
            }
            //
            for (j=0; j<a; j++) { //perulangan membuat baris
                b=b;//nilai b diupdate ulang setelah keluar dari kolom
                for (k=0; k<i; k++) { //perulangan membuat kolom
                   while(b<panjangKalimat && b<=k){//perulangan huruf
                       System.out.print(huruf[b]);//cetak huruf ke-b
                       b++;
                   }
                }
                System.out.print("\n");
                i=i+c;
            }
            i=c;
            System.out.print("\n");
        }
    }
}