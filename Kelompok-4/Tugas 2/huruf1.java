/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package huruf;
import java.io.File;
import java.io.IOException;
import java.io.FileWriter;
import java.io.PrintWriter;

/**
 *
 * @author User
 */
public class huruf1 {
    public static void main(String Args[]){
        char i,j,k,l;
        try{
            File huruf = new File("huruf.txt");
            try (PrintWriter pr = new PrintWriter(new FileWriter(huruf))) {
                for(i=97; i<=122; i++){
                    for(j=97; j<=122; j++){
                        for(k=97; k<=122; k++){
                            for(l=97; l<=122; l++){
                                pr.print(" "+i+" "+j+" "+k+" "+l+"\n");
                            }
                        }
                    }
                }
                pr.close();
            }
            System.out.println("Data tersimpan");
        }
        catch(Exception e){
            System.out.print("Tidak dapat dicetak");
        }
    }
}
