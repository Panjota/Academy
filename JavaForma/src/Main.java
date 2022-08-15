import java.util.ArrayList;

public class Main {
    
    public static void main(String[] args) {
        
        ArrayList<Forma> formas = new ArrayList<>();

        Retangulo rA = new Retangulo(2, 4);
        Retangulo rB = new Retangulo(4, 3);

        Circulo cA = new Circulo(3);
        Circulo cB = new Circulo(10);

        Quadrado qA = new Quadrado(10, 10);

        formas.add(rA);
        formas.add(rB);
        formas.add(cA);
        formas.add(cB);
        formas.add(qA);

        for (int i = 0;i<formas.size();i++){
            System.out.println("Forma: "+formas.get(i) + " Área: "+formas.get(i).calcularArea() + " | " + " Perímetro: "+formas.get(i).calcularPerimetro());
        }

    }
}