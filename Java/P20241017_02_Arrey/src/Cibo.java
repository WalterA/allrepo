
public class Cibo {
	private String nome , colore , tipologia;

	public String getNome() {
		return nome;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public String getColore() {
		return colore;
	}

	public void setColore(String colore) {
		this.colore = colore;
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
		this.colore = colore;
		this.tipologia = tipologia;
	}

	public Cibo() {
		super();
	}

	@Override
	public String toString() {
		return "Cibo [nome=" + nome + ", colore=" + colore + ", tipologia=" + tipologia + "]";
	}
}
