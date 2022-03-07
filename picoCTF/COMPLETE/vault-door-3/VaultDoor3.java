import java.util.*;

class VaultDoor3 {
    public static void main(String args[]) {
        VaultDoor3 vaultDoor = new VaultDoor3();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
	String input = userInput.substring("picoCTF{".length(),userInput.length()-1);
	if (vaultDoor.checkPassword(input)) {
	    System.out.println("Access granted.");
	} else {
	    System.out.println("Access denied!");
        }
    }

    // Our security monitoring team has noticed some intrusions on some of the
    // less secure doors. Dr. Evil has asked me specifically to build a stronger
    // vault door to protect his Doomsday plans. I just *know* this door will
    // keep all of those nosy agents out of our business. Mwa ha!
    //
    // -Minion #2671
    public boolean checkPassword(String password) {
        if (password.length() != 32) {
            return false;
        }
        char[] buffer = new char[32];
        int i;
	System.out.println("First phase");
        for (i=0; i<8; i++) {
		System.out.println(i + "<--" + i);
            buffer[i] = password.charAt(i);
        }
	System.out.println("Second phase");
        for (; i<16; i++) {
		System.out.println(i + "<--" + (23-i));
            buffer[i] = password.charAt(23-i);
        }
	System.out.println("Phase 3");
        for (; i<32; i+=2) {
		System.out.println(i + "<--" + (46-i));
            buffer[i] = password.charAt(46-i);
        }
	System.out.println("Phase 4");
        for (i=31; i>=17; i-=2) {
		System.out.println(i + "<--" + i);
            buffer[i] = password.charAt(i);
        }
        String s = new String(buffer);
        return s.equals("jU5t_a_sna_3lpm12g94c_u_4_m7ra41");
    }
}
