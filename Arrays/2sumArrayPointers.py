def twoSum(numbers: list[int], target: int) -> list[int]:
        
        right=len(numbers)-1
        left=0
        

        while right>left:
            a=numbers[left]
            b=numbers[right]
            if a+b==target:
                return [left,right]
            elif a+b>target:
                right-=1
            elif a+b<target:
                left+=1
        return []  
m1=[2,7,11,15]
print(twoSum(m1,9))