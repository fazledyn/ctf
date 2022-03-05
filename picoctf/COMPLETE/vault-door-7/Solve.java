import java.util.*;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.*;

class Solve {
	public static void main(String args[]) {
        	System.out.print("picoCTF{");
		getPassword();
		System.out.print("}");
	}

    // Each character can be represented as a byte value using its
    // ASCII encoding. Each byte contains 8 bits, and an int contains
    // 32 bits, so we can "pack" 4 bytes into a single int. Here's an
    // example: if the hex string is "01ab", then those can be
    // represented as the bytes {0x30, 0x31, 0x61, 0x62}. When those
    // bytes are represented as binary, they are:
    //
    // 0x30: 00110000
    // 0x31: 00110001
    // 0x61: 01100001
    // 0x62: 01100010
    //
    // If we put those 4 binary numbers end to end, we end up with 32
    // bits that can be interpreted as an int.
    //
    // 00110000001100010110000101100010 -> 808542562
    //
    // Since 4 chars can be represented as 1 int, the 32 character password can
    // be represented as an array of 8 ints.
    //
    // - Minion #7816
    public int[] passwordToIntArray(String hex) {
        int[] x = new int[8];
        byte[] hexBytes = hex.getBytes();
        for (int i=0; i<8; i++) {
            x[i] = hexBytes[i*4]   << 24
                 | hexBytes[i*4+1] << 16
                 | hexBytes[i*4+2] << 8
                 | hexBytes[i*4+3];
        }
        return x;
    }

    public static void getPassword() {
        int[] x = new int[8];
        x[0] = 1096770097;
        x[1] = 1952395366;
        x[2] = 1600270708;
        x[3] = 1601398833;
        x[4] = 1716808014;
        x[5] = 1734293296;
        x[6] = 842413104;
        x[7] = 1684157793;

	for (int i=0; i < 8; i++) {
		byte[] byteArr = new byte[4];
		byteArr[3] = (byte) x[i];
		byteArr[2] = (byte) (x[i] >> 8);
		byteArr[1] = (byte) (x[i] >> 16);
		byteArr[0] = (byte) (x[i] >> 24);
		System.out.print( new String(byteArr) );
	}
    }
}
