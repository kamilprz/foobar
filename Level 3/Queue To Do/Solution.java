
public class Solution{
    public static int solution(int start, int length){
        int checksum = 0, remaining = length;

        while(remaining > 0){
            for(int i = start; i < start + remaining; i++){
                checksum ^= i;
            }
            start += length;
            remaining--;
        }
        return checksum;
    }
}