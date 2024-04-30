import java.io.*;
import java.nio.file.*;

public class CaseConverter {
    public static void main(String[] args) {
        if (args.length != 2) {
            System.out.println("Usage: java CaseConverter <source file> <destination file>");
            System.exit(1);
        }

        Path sourcePath = Paths.get(args[0]);
        Path destinationPath = Paths.get(args[1]);

        try {
            String content = new String(Files.readAllBytes(sourcePath));
            String converted = convertCase(content);
            Files.write(destinationPath, converted.getBytes());
            System.out.println("File converted successfully.");
        } catch (IOException e) {
            System.out.println("An error occurred while converting the file.");
            e.printStackTrace();
        }
    }

    private static String convertCase(String str) {
        StringBuilder builder = new StringBuilder(str.length());
        for (char c : str.toCharArray()) {
            if (Character.isLowerCase(c)) {
                builder.append(Character.toUpperCase(c));
            } else if (Character.isUpperCase(c)) {
                builder.append(Character.toLowerCase(c));
            } else {
                builder.append(c);
            }
        }
        return builder.toString();
    }
}

// java CaseConverter input/test.txt output/java_test.txt