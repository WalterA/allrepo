
import java.lang.reflect.*;
import java.sql.Date;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Scanner;

public class salva  {
	
	static private Scanner scanner = new Scanner(System.in);
	
    public static Object Parse(String className) {
		try {
	        Class<?> clazz;
			clazz = Class.forName(className);
	        return Parse(clazz);
		} catch (ClassNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			return null;
		}
    }
	
    public static Object Parse(Class<?> clazz) { //String className) {

        try {
            //Class<?> clazz = Class.forName(className);

            Object instance = clazz.getDeclaredConstructor().newInstance();

            Field[] fields = clazz.getDeclaredFields();

            for (Field field : fields) {
                field.setAccessible(true);  // Make private fields accessible

                Class<?> fieldType = field.getType();
                String fieldName = field.getName();

                System.out.print("Inserire " + fieldName + " (" + fieldType.getSimpleName() + "): ");
                String input = scanner.nextLine();

                Object value = convertInput(fieldType, input);
                field.set(instance, value);
            }
            return instance;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        } finally {
        }
    }

    private static Object convertInput(Class<?> fieldType, String input) {
        if (fieldType == int.class||fieldType == Integer.class) {
            return Integer.parseInt(input);
        } else if (fieldType == double.class || fieldType == Double.class ) {
            return Double.parseDouble(input);
        } else if (fieldType == Date.class) {
        	java.sql.Date date=null;
			try {
	        	java.util.Date dDate;
//				dDate = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss z").parse(input);
				dDate = new SimpleDateFormat("dd/MM/yyyy").parse(input);
				date = new Date(dDate.getTime());
			} catch (ParseException e) {
				//e.printStackTrace();
			}
            return date;
        } else if (fieldType == boolean.class||fieldType == Boolean.class) {
            return Boolean.parseBoolean(input);
        } else if (fieldType == long.class||fieldType == Long.class) {
            return Long.parseLong(input);
        } else if (fieldType == float.class||fieldType == Float.class) {
            return Float.parseFloat(input);
        } else if (fieldType == char.class||fieldType == Character.class) {
            return input.charAt(0); 
        } else if (fieldType == String.class) {
            return input; 
        } else {
            return null;  // Tutto il resto è null!!
        }
    }
}
