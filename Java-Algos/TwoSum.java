import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class TwoSum {

    public static int[] twoSum(int[] nums, int target) {
        Map dic = new HashMap();

        for (int i = 0; i < nums.length; i++) {
            int comp = target - nums[i];

            if (dic.containsKey(comp)) {
                return new int[]{(int)dic.get(comp), i};
            }
        dic.put(nums[i], i)
    }
    throw new IllegalArgumentException("No Solution!!!")

    public static void main(String[] args) {
        int[] res = twoSum(new int[]{2, 7, 11,15}, 26);
        System.out.println(Arrays.toString(res));
    }
}