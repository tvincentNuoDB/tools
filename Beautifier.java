import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;

public class Beautifier {
	
	public static void main(String[] args){
		if(args.length < 2) {
			System.out.println("Usage:\n java Beautifier [COLOR=NEW_COLOR][FILENAME]");
			System.exit(1); 
		}

		String filename = args[args.length - 1];
		ArrayList<Pair> pairs = new ArrayList<>();

		for(int i = 0; i < args.length - 1; i++)
			pairs.add(new Pair(args[i].split("=")[0], args[i].split("=")[1]));
		

		StringBuilder sb = new StringBuilder();

		try {
			BufferedReader br = new BufferedReader(new FileReader(filename));
			String line = br.readLine();

			while (line != null) {
            	sb.append(line);
            	sb.append(System.lineSeparator());
            	line = br.readLine();
        	}
        	String file = sb.toString();
        	br.close();

        	for(int i = 0; i < pairs.size(); i++)
        		file = file.replace(pairs.get(i).getKey(), pairs.get(i).getValue());

			FileWriter fstream = new FileWriter(filename);        
			BufferedWriter out = new BufferedWriter(fstream);
			out.write(file);
			out.close();

		}
		catch (Exception e){
			System.out.println("An error has occured: " + e.getMessage());
		}
	}
}

class Pair {
	String key;
	String value;
	public Pair(String key, String value){
		this.key = key;
		this.value = value;
	}

	public String getKey(){
		return key;
	}
	public String getValue(){
		return value;
	}

}