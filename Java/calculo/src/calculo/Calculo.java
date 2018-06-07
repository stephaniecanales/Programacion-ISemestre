/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculo;

import java.util.Scanner;

/**
 *
 * @author steph
 */
public class Calculo {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Figura figi = new Figura ();
        System.out.println("Menu");
        System.out.println("1) valor radio");
        System.out.println("2) area radio");
        System.out.println("3) valor alto");
        System.out.println("4) ing alto");
        System.out.println("5) valor ancho");
        System.out.println("6) ing ancho ");
        System.out.println("7) area");
        System.out.println("8) salir");
        System.out.println ("ingrese la opcion que desea ejecutar");
        Scanner entrada = new Scanner(System.in);
        int opcion = entrada.nextInt();
        System.out.println("Ingrese el valor: ");
        int valor = entrada.nextInt();
        System.out.println("Ingrese el valor 1: ");
        int valor1 = entrada.nextInt();
        System.out.println("Ingrese el valor 2: ");
        int valor2 = entrada.nextInt();
        System.out.println("Ingrese el alto: ");
        int alto = entrada.nextInt();
        System.out.println("Ingrese el ancho: ");
        int ancho = entrada.nextInt();
        double resultado = 0;        
        switch (opcion){
            case 1:
                resultado = figi.circulo(valor);
                break;
            case 2:
                resultado = figi.circulo2 (valor);
                break;
            case 3:
                resultado = figi.alto(valor1);
                break;
            case 4:
                resultado = figi.alto2(valor1);
                break;
            case 5:
                resultado = figi.ancho(valor2);
                break;
            case 6:
                resultado = figi.ancho2(valor2);
                break;
            case 7:
                resultado = figi.area(alto,ancho);
                break;
            case 8:
                System.exit(0);
            default:
                System.out.println("No se realizo ninguna operacion");
        }
        System.out.println("El resultado es:" + resultado);
        /* if (opcion == 1){ Forma de hacerlo con if
            oper.suma(20,25);
        }
        else if (opcion == 2){
            oper.resta(20,25);
        }
        else if (opcion == 3){
            oper.multiplicacion(20,25);
        }
        else if (opcion == 4){
            oper.division(20, 25);
        }*/  
    }
        // TODO code application logic here
    }
    
