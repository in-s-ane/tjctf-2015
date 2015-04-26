import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

public class JavaBytecode {
    public static void main(String[] args) {
        Scanner a = new Scanner(System.in);
        System.out.print("Enter passcode: ");
        String b = a.nextLine();
        if (JavaBytecode.c(b)) {
            System.out.println("Success!");
        } else {
            System.out.println("Failed");
        }
    }

    private static void e(String b) {
        int i = 0;
        b = String.valueOf(b) + i;
    }

    private static boolean c(String b) {
        int i;
        int i2;
        for (i2 = 0; i2 < 10000000; ++i2) {
            JavaBytecode.e(b);
        }
        for (i2 = 0; i2 < b.length(); ++i2) {
            char c = b.charAt(i2);
            if (c >= '0' && c <= '9') continue;
            return false;
        }
        int d = 0;
        for (i = 0; i < b.length() - 1; i+=2) {
            d+=b.charAt(i) - 48;
        }
        for (i = 1; i < b.length() - 1; i+=2) {
            d+=(b.charAt(i) - 48) * 3;
        }
        int e = 10 - d % 10;
        int f = 0;
        for (int i3 = 0; i3 < 5; ++i3) {
            f+=b.charAt(i3) - 48;
        }
        int g = 1;
        for (int i4 = 1; i4 < 5; ++i4) {
            g*=b.charAt(i4) - 48;
        }
        int h = b.charAt(1) - 48;
        int l = b.charAt(2) - 48;
        int m = b.charAt(3) - 48;
        int n = b.charAt(4) - 48;
        if (!b.substring(5, 11).equals("914323")) {
            return false;
        }
        if (Math.abs(h + l - m) != 1 || Math.abs(h + l - n) != 1) {
            return false;
        }
        if (!b.contains((CharSequence)"0")) {
            return false;
        }
        if (b.charAt(b.length() - 1) - 48 != e) {
            return false;
        }
        if (f != 21) {
            return false;
        }
        if (g != 480) {
            return false;
        }
        if (e == 9) {
            return true;
        }
        return false;
    }
}

