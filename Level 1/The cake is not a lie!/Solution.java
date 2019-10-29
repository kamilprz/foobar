import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) throws IOException {
        String test = "false"; //8
        int i = solution(test);

        String test1 = ""; //6
        int i1 = solution(test1);

        String test2 = "abcabcabcabc"; //4
        int i2 = solution(test2);

        String test3 = "aaabaaaaabaaaaabaa"; //3
        int i3 = solution(test3);
    }

    public static int solution(String x){
        if(x.length()==0){
            return -1;
        }
        int length = x.length();
        String str1;
        String str2;
        for (int i=1; i < length; i++){
            str1 = x.substring(0,length-i);
            str2 = x.substring(i, length);
            if(str1.equals(str2)){
                return (length/i);
            }
        }
        return 1;
    }
}
