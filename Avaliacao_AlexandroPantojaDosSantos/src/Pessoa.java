

public class Pessoa{
    public String nome;
    public String pai;
    public String mae;

    //a) Construtores Sobrecarregados
    public Pessoa(String nome, String pai, String mae) {
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
    public String getPai() {
        return pai;
    }
    public void setPai(String pai) {
        this.pai = pai;
    }
    public String getMae() {
        return mae;
    }
    public void setMae(String mae) {
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
    
}
