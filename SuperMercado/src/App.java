import java.util.ArrayList;

public class App{
    public static void main(String[] args) {
        
    Cliente alex = new Cliente("Alex", "1273");
    Cliente danilo = new Cliente("Danilo", "1253");
    Cliente leo = new Cliente("Leo", "1243");
    Cliente lucas = new Cliente("Lucas", "1233");
    Cliente kirk = new Cliente("Kirk", "1223");
        
    Produto arroz = new Produto("Arroz", 30f, 40);
    Produto feijao = new Produto("Feijão", 35f, 35);
    Produto macarrao = new Produto("Macarrão", 25f, 35);
    Produto carne = new Produto("Carne", 50f, 30);
    Produto frango = new Produto("Frango", 40f, 25);

    Item i1 = new Item(3, arroz);
    Item i2 = new Item(2, feijao);
    Item i3 = new Item(1, carne);
    Item i4 = new Item(3, frango);
    Item i5 = new Item(4, macarrao);

    ArrayList<Item> p1 = new ArrayList<Item>();
    ArrayList<Item> p2 = new ArrayList<Item>();
    ArrayList<Item> p3 = new ArrayList<Item>();

    p1.add(i1);
    p1.add(i2);
    p1.add(i3);
    p2.add(i3);
    p2.add(i2);
    p2.add(i5);
    p2.add(i4);
    p3.add(i1);
    p3.add(i4);
    p3.add(i3);
    

    Pedido pedido1 = new Pedido(alex,"Cartão", p1);
    Pedido pedido2 = new Pedido(leo,"Cartão", p2);
    Pedido pedido3 = new Pedido(kirk,"Cartão", p3);

    pedido1.mostrarPedido();
    pedido2.mostrarPedido();
    pedido3.mostrarPedido();

    }

}