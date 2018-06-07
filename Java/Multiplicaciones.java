/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package multiplicaciones;

import java.util.Arrays;

/**
 *
 * @author steph
 */
public class Multiplicaciones {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
    int[][] a = { { 1, 2, 3 }, { 4, 5, 6 } };
    int[][] b = { { 7, 8 }, { 9, 10 }, { 11, 12 } };
    int[][] c = multiply(a, b);
    System.out.println(Arrays.deepToString(c));
        // TODO code application logic here
    }
    public static int[][] multiply(int[][] a, int[][] b) {
    int[][] c = new int[a.length][b[0].length];
    // se comprueba si las matrices se pueden multiplicar
    if (a[0].length == b.length) {
        for (int i = 0; i < a.length; i++) {
            for (int j = 0; j < b[0].length; j++) {
                for (int k = 0; k < a[0].length; k++) {
                    // aquí se multiplica la matriz
                    c[i][j] += a[i][k] * b[k][j];
                }
            }
        }
    }
    /**
     * si no se cumple la condición se retorna una matriz vacía
     */
    return c;
    
    }
}
