package example;

public class maind {
	
	public static void main(String[] args){
		int n = 10;
		for(int i = 0 ;i <= n;i++){
			for(int j = 0;j <= i;j++){
				System.out.print("*");
			}
			for(int j = i+1;j<=n;j++){
				System.out.print(" ");
			}
			for(int k = 0;k < n-i;k++){
				System.out.print(" ");
			}
			for(int k = 0;k<=i;k++){
				System.out.print("*");
			}
			System.out.println();
		}
		for(int i = 1;i<=n;i++){
			for(int j = n-i;j>=0;j--){
				System.out.print("*");
			}
			for(int j = n-i;j<n;j++){
				System.out.print(" ");
			}
			
			for(int k = 0;k<i;k++){
				System.out.print(" ");
			}
			for(int  k=0;k<=n-i;k++){
				System.out.print("*");
			}

			System.out.println();
		}

	}
}
