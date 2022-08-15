public class Circulo extends Forma {
    private float raio;

    public Circulo(float raio) {
        this.raio = raio;
    }

    public float getRaio() {
        return raio;
    }
    public void setRaio(float raio) {
        this.raio = raio;
    }

    @Override
    public float calcularArea(){
        float area = 0;
        area = (float) (Math.PI*Math.pow(raio, 2));
        return area;
    }

    @Override
    public float calcularPerimetro() {
        float perimetro = 0;
        perimetro = (float) (2 * Math.PI * raio);
        return perimetro;
    }

    @Override
    public String toString() {
        
        return "Circulo";
    }
}
