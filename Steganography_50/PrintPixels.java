import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.InputStream;
import java.io.PrintStream;
import java.io.PrintWriter;
import java.util.Scanner;
import javax.imageio.ImageIO;

public class PrintPixels {
    public static void main(String[] arrstring) throws Exception {
        String string = null;
        if (arrstring.length == 0) {
            System.out.print("Image: ");
            string = new Scanner(System.in).nextLine();
        } else {
            string = arrstring[0];
        }
        PrintWriter printWriter = new PrintWriter("out.txt");
        printWriter.println(PrintPixels.ppm(ImageIO.read(new File(string))));
        printWriter.close();
        System.out.println("Saved to out.txt");
    }

    public static String ppm(BufferedImage bufferedImage) {
        String string = "";
        for (int i = 0; i < bufferedImage.getHeight(); ++i) {
            for (int j = 0; j < bufferedImage.getWidth(); ++j) {
                Color color = new Color(bufferedImage.getRGB(i, j));
                string = string + "[" + i + ", " + j + "] :: (" + color.getRed() + " " + color.getGreen() + " " + color.getBlue() + ")\n";
            }
        }
        return string;
    }
}

