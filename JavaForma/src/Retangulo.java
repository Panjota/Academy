public class Retangulo extends Forma{
    private float lado;
    private float altura;

    public Retangulo(float lado, float altura){
        this.lado = lado;
        this.altura = altura;
    }

    public float getLado() {
        return lado;
    }
    public void setLado(float lado) {
        this.lado = lado;
    }

    public float getAltura() {
        return altura;
    }
    public void setAltura(float altura) {
        this.altura = altura;
    }

    @Override
    public float calcularArea(){
        float area = 0;
        area = lado * altura;
        return area;
    }

    @Override
    public float calcularPerimetro() {
        float perimetro = 0;
        perimetro = 2 * (lado + altura);
        return perimetro;
    }

    @Override
    public String toString() {
        return "Retangulo";
    }

    
}
