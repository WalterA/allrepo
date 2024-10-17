
public class Cibo {
	private String nome , tipologia;
	double calorie;
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public String getTipologia() {
		return tipologia;
	}
	public void setTipologia(String tipologia) {
		this.tipologia = tipologia;
	}
	public double getCalorie() {
		return calorie;
	}
	public void setCalorie(double calorie) {
		this.calorie = calorie;
	}
	public Cibo(String nome, String tipologia, double calorie) {
		super();
		this.nome = nome;
		this.tipologia = tipologia;
		this.calorie = calorie;
	}
	public Cibo() {
		super();
	}
	@Override
	public String toString() {
		return "Cibo [nome=" + nome + ", tipologia=" + tipologia + ", calorie=" + calorie + "]";
	}
	

}
