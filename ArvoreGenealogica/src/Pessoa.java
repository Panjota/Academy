

public class Pessoa{
    public String nome;
    public Pessoa pai;
    public Pessoa mae;

    //a) Construtores Sobrecarregados
    public Pessoa(String nome, Pessoa pai, Pessoa mae) {
        this.nome = nome;
        this.pai = pai;
        this.mae = mae;
        
    }
    public Pessoa(String nome) {
        this.nome = nome;
        pai = null;
        mae = null;
    }

    //get and set
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public Pessoa getPai() {
        return pai;
    }
    public void setPai(Pessoa pai) {
        this.pai = pai;
    }
    public Pessoa getMae() {
        return mae;
    }
    public void setMae(Pessoa mae) {
        this.mae = mae;
    }

    //c) verificando a irmandade
    public void verificarIrmandade(Pessoa pessoa){
        if(nome != pessoa.getNome() && mae == pessoa.getMae() || pai == pessoa.getPai()){
            System.out.println(nome+ " e "+ pessoa.getNome()+ " são irmãos");
        }else{
            System.out.println(nome+ " e "+ pessoa.getNome()+ " não são irmãos");
        }
    }
    //b) verificando igualdade semântica
    public void verificarIgualade(Pessoa pessoa) {
        if (nome == pessoa.getNome() && mae == pessoa.getMae()){
            System.out.println(nome+ " e "+ pessoa.getNome()+ " são iguais");
        }else{
            System.out.println(nome+ " e "+ pessoa.getNome()+ " são diferentes");

        }
    }
    
    //d)Verificando se uma pessoa do parametro é antecessora de outra
    public void verificarAntecessor(Pessoa pessoa){
        if (pai == pessoa || mae == pessoa){
            System.out.println(pessoa.getNome() + " é antecessor(a) de " + nome);
        }else{
            System.out.println(pessoa.getNome() + " não é antecessor de " + nome);
        }
    }

    // segundo metodo opcional, ele verificar se a pessoa tem antecessores
    // se ele tiver ele mostra quem são, se não, ele mostra que não tem.
    public void verificandoAntecessores(){
        if (pai == null && mae == null){
            System.out.println(nome + " não tem antecessores!!");
        }else{
            System.out.println("Os antecessores de " + nome + " são: " + getPai() + " e " + getMae());
        }
    
    }
    @Override
    public String toString() {
        return  nome;
    }
    
    
}
