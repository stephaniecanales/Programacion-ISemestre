package prueba;

import java.util.Scanner;

public class principal {
    public static void main (String[]args){
        Operaciones oper = new Operaciones();
        System.out.println("Menu");
        System.out.println("1) Suma");
        System.out.println("2) Resta");
        System.out.println("3) Multiplicar");
        System.out.println("4) Dividir");
        System.out.println ("ingrese la opcion que desea ejecutar");
        Scanner entrada = new Scanner(System.in);
        int opcion = entrada.nextInt();
        System.out.println("Ingrese el valor 1: ");
        int valor1 = entrada.nextInt();
        System.out.println("Ingrese el valor 2: ");
        int valor2 = entrada.nextInt();
        double resultado = 0;        
        switch (opcion){
            case 1:
                resultado = oper.suma(valor1, valor2);
                break;
            case 2:
                resultado = oper.resta (valor1, valor2);
                break;
            case 3:
                resultado = oper.multiplicacion(valor1, valor2);
                break;
            case 4:
                resultado = oper.division(valor1, valor2);
                break;
            case 5:
                System.exit(0);
            default:
                System.out.println("No se realizo ninguna operacion");
        }
        System.out.println("El rsultado es:" + resultado);
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
}
