
public class Main {

	public static void main(String[] args) {
		TriangoloRettangolo tr = new TriangoloRettangolo(1, 2);

		System.out.println(tr.Area());
		tr.setCat1(100);
		System.out.println(tr.Area());
		tr.setCat2(200);
		System.out.println(tr.Area());

		Persona pr = new Persona();
		pr.setNome("Ciccio");
		pr.setTemperaturaFarhenheit(37.5F);
		pr.setTemperaturaCelsuis(37.5F);
		System.out.println(pr.getNome());
		System.out.println(pr.getTemperaturaCelsuis());
		System.out.println(pr.getTemperaFarhenheit());
	}

}
