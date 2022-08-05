
public class Item {
    public int totalItens;
    public Produto prodDesejado;

    public Item(int totalItens,Produto prodDesejado) {
        this.totalItens = totalItens;
        this.prodDesejado = prodDesejado;
    }

    public int getTotalItens() {
        return totalItens;
    }
    public void setTotalItens(int totalItens) {
        this.totalItens = totalItens;
    }

    public Produto getProdDesejado() {
        return prodDesejado;
    }

    public void setProdDesejado(Produto prodDesejado) {
        this.prodDesejado = prodDesejado;
    }

    
    
}
