
public class Cibo {
	private String nome , tipologia;
	int calorie;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public int getCalorie() {
		return calorie;
	}

	public void setCalorie(int calorie) {
		this.calorie = calorie;
	}

	public String getTipologia() {
		return tipologia;
	}

	public void setTipologia(String tipologia) {
		this.tipologia = tipologia;
	}

	public Cibo(String nome, String colore, String tipologia) {
		super();
		this.nome = nome;
		this.calorie = calorie;
		this.tipologia = tipologia;
	}

	public Cibo() {
		super();
	}

	@Override
	public String toString() {
		return "Cibo [nome=" + nome + ", calorie=" + calorie + ", tipologia=" + tipologia + "]";
	}
}
