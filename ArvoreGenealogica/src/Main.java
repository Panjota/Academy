public class Main {
    public static void main(String[] args){
        Pessoa alex = new Pessoa("Alex");
        Pessoa julie = new Pessoa("Julie");
        Pessoa juliezinha = new Pessoa("Juliezinha", "Alex", "Julie");
        Pessoa andre = new Pessoa("André", "Alex", "Julie");
        Pessoa beniciu = new Pessoa("Beniciu", "Bruno", "Iara");
        Pessoa analu = new Pessoa("Analu", "Hiago", "Auxiliadora");
        Pessoa juliezinha1 = new Pessoa("Juliezinha", "Alex", "Julie");

        juliezinha.verificarIrmandade(andre);
        beniciu.verificarIrmandade(juliezinha);

        juliezinha.verificarIgualade(juliezinha1);
        analu.verificarIgualade(juliezinha);

    }
}
