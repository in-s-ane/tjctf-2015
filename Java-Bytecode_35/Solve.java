import java.io.InputStream;
import java.io.PrintStream;
import java.util.Scanner;

// NOTE: Don't try to compile this; it won't work. Just read the annotated
// source.
public class Solve {
    public static void main(String[] args) {
        //Scanner a = new Scanner(System.in);
        //System.out.print("Enter passcode: ");
        //String b = a.nextLine();
        solve();
        //if (Solve.c(b)) {
        //    System.out.println("Success!");
        //} else {
        //    System.out.println("Failed");
        //}
    }

    public static void e(String b) {
        int i = 0;
        b = String.valueOf(b) + i;
    }

    public static boolean solve() {
        int i;
        int i2;
        // password must be numeric
        int d = 0;
        for (i = 0; i < b.length() - 1; i+=2) {
            d+=b.charAt(i) - 48;
        }
        for (i = 1; i < b.length() - 1; i+=2) {
            d+=(b.charAt(i) - 48) * 3;
        }
        int e = 10 - d % 10; // A value 1-10
        if (e != 9) { // e must be 9, and thus d % 10 must equal 1
            return false;
        }
        int f = 0;
        for (int i3 = 0; i3 < 5; ++i3) { // Digits 0-4
            f+=b.charAt(i3) - 48;
        }
        if (f != 21) {
            return false;
        }
        int g = 1;
        for (int i4 = 1; i4 < 5; ++i4) { // Digits 1-4
            g*=b.charAt(i4) - 48;
        }
        if (g != 480) {
            return false;
        }
        int h = b.charAt(1) - 48; // Digit 1
        int l = b.charAt(2) - 48; // Digit 2
        int m = b.charAt(3) - 48; // Digit 3
        int n = b.charAt(4) - 48; // Digit 4
        if (Math.abs(h + l - m) != 1 || Math.abs(h + l - n) != 1) {
            return false;
        }
        if (!b.substring(5, 11).equals("914323")) { // Digits 5-10 are 914323
            return false;
        }
        if (!b.contains((CharSequence)"0")) { // Contains a zero
            return false;
        }
        if (b.charAt(b.length() - 1) - 48 != e) { // Last digit equals e, which is 9
            return false;
        }
        return true;
    }
}

/*
Prime factors of 480:
2 2 2 2 2 3 5 => 3 4 5 8 or 2 6 5 8

025869143239 satisfies each condition except lines 29-35. We can append garbage
data that doesn't affect the results of any of the other checks directly before
the last digit to satisfy the check in lines 29-35. See solve.py.
*/

/* COMPUTING ORDER OF DIGITS 1-4
>>> a = [3,4,5,8]
>>> from itertools import permutations
>>> [x for x in permutations(a, r=4)]                                                           
[(3, 4, 5, 8), (3, 4, 8, 5), (3, 5, 4, 8), (3, 5, 8, 4), (3, 8, 4, 5), (3, 8, 5, 4), (4, 3, 5, 8), (4, 3, 8, 5), (4, 5, 3, 8), (4, 5, 8, 3), (4, 8, 3, 5), (4, 8, 5, 3), (5, 3, 4, 8), (5, 3, 8, 4), (5, 4, 3, 8), (5, 4, 8, 3), (5, 8, 3, 4), (5, 8, 4, 3), (8, 3, 4, 5), (8, 3, 5, 4), (8, 4, 3, 5), (8, 4, 5, 3), (8, 5, 3, 4), (8, 5, 4, 3)]
>>> def hasprop(x):
...    return abs(x[0] + x[1] - x[2]) == 1 and abs(x[0] + x[1] - x[3]) == 1
...
>>> filter(hasprop, permutations(a, r=4))
[]
>>> a = [2,8,6,5]
>>> filter(hasprop, permutations(a, r=4))
[(2, 5, 8, 6), (2, 5, 6, 8), (5, 2, 8, 6), (5, 2, 6, 8)]
*/

