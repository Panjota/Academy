import java.util.ArrayList;

public class Pedido {
    private Cliente nome;
    private String tipoPagamento;
    private ArrayList<Item> itens;
    private double valorTotal;
    
    public Pedido(Cliente nome, String tipoPagamento, ArrayList<Item> itens) {
        this.nome = nome;
        this.tipoPagamento = tipoPagamento;
        this.itens = itens;
        this.valorTotal = 0.0f;

        for (Item item: this.itens) {
            this.valorTotal+=item.getTotalItens()*item.getProdDesejado().getPreco();
        }
    }

    public String getTipoPagamento() {
        return tipoPagamento;
    }
    public void setTipoPagamento(String tipoPagamento) {
        this.tipoPagamento = tipoPagamento;
    }
    public ArrayList<Item> getItens() {
        return itens;
    }
    public void setItens(ArrayList<Item> itens) {
        this.itens = itens;
    }
    public Cliente getNome() {
        return nome;
    }
    public void setNome(Cliente nome) {
        this.nome = nome;
    }
    public double valorTotal(double preco,int totalItens){
        valorTotal = valorTotal + (preco * totalItens);
        return valorTotal;
    }

    public void mostrarPedido () {
        int soma = 0;
        for(Item item: itens){
            soma += item.getTotalItens();
        }
        System.out.println("\n-------------NOTA----------------");
        System.out.println("Cliente: "+ nome);
        System.out.println("Total Itens: "+ soma);
        System.out.println("Tipo de Pagamento: "+ tipoPagamento);
        System.out.println("-------------ITENS-----------------");
        for (int i=0;i<itens.size();i++){
            System.out.print("\nProduto: "+itens.get(i).getProdDesejado().getNome()+" ___ Quantidade: "+itens.get(i).totalItens);
        }
        System.out.print("\nValor Total: R$"+ valorTotal);

    }

}
