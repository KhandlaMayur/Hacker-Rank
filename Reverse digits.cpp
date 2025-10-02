class Solution {
  public:
    int reverseDigits(int n) {
        // Code here
        int i=0,rev=0;
        while(n%10==0 && n!=0){
            n=n/10;
        }
        while(n>0){
            i=n%10;
            rev=rev*10+i;
            n=n/10;
        }
        return rev;
    }
};
