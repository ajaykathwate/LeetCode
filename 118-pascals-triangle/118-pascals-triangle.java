class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        for(int i=1;i<=numRows;i++){
            
            List<Integer> current_list = new ArrayList<Integer>();
            for(int j=0;j<i;j++){
                if(j==0 || j==i-1){
                    current_list.add(1);
                    continue;
                }
                current_list.add(result.get(i-2).get(j-1) + result.get(i-2).get(j));     
            }
            
            result.add(current_list);
        }
        return result;  
    }
}