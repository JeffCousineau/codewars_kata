#include <vector>

int sum(std::vector<int> nums) {
  int total = 0;
  for(int i =0; i < nums.size(); i++)
  {
    total += nums[i];
  }
}
