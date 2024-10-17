
public class Persona {
	private String nome, cibo1, cibo2, cibo3;

	public String getNome() {
		return nome;
	}

	public String getCibo1() {
		return cibo1;
	}

	public void setCibo1(String cibo1) {
		this.cibo1 = cibo1;
	}

	public String getCibo2() {
		return cibo2;
	}

	public void setCibo2(String cibo2) {
		this.cibo2 = cibo2;
	}

	public String getCibo3() {
		return cibo3;
	}

	public void setCibo3(String cibo3) {
		this.cibo3 = cibo3;
	}

	public void setNome(String nome) {
		this.nome = nome;
	}

	public Persona(String nome) {
		super();
		this.nome = nome;
	}

	public Persona(String nome, String cibo1, String cibo2, String cibo3) {
		super();
		this.nome = nome;
		this.cibo1 = cibo1;
		this.cibo2 = cibo2;
		this.cibo3 = cibo3;
	}

	@Override
	public String toString() {
		return "Persona [nome=" + nome + ", cibo1=" + cibo1 + ", cibo2=" + cibo2 + ", cibo3=" + cibo3 + "]";
	}


}
