import java.util.ArrayList;
import java.util.List;

public class greatestCandies{
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int t=candies.length;
        List<Boolean> result=new ArrayList<>();
        int max=0;
        for (int i=0;i<t;i++){
            if (candies[i]>max)max=candies[i];
        }
        for (int i=0;i<t;i++){
            if(candies[i]+extraCandies>=max)result.add(true);
            else result.add(false);
        }
        return (result);

        
    }
    public static void main (String[] args){
        
    }
}