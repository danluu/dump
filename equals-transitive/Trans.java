class Trans {
    public static void main(String args[]) {
	long   x = 9007199254740992L;    // 2^53
	double y = 9007199254740992.0;  // 2.0^53
	long   z = 9007199254740993L;    // 2^53+1
	System.out.println(x == y);
	System.out.println(y == z);
	System.out.println(x == z);
    }
}

