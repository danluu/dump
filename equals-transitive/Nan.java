class Nan {
    public static void main (String args[]) {
	double n = 0.0 / 0.0;
	System.out.println(java.lang.Math.min(n, 1.0));
	System.out.println(java.lang.Math.min(1.0, n));
    }
}

