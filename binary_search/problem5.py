# You are given an array arr of length N, representing money with N customers. The i-th customer has arri rupees. There is another array cost of length M, representing the cost of M items in a store. The j-th item costs costj rupees. The store offers some discount money d which any customer can use to buy an item. Each customer can buy only one item and cannot use his money to buy an item for any other customer.

# Task

# Determine the maximum number of customers who can buy an item and the minimum total sum of customers’ money spent to achieve maximum customers with an item.

# Notes

# Assume 1-Based Indexing.
# The discount money d is common for all the customers, i.e., if one customer spends r rupees from d, then the discount money is reduced to (d-r) for all the customers.
# Multiple customers can spend money from the discount.


#ans
from sqlalchemy import false, true


def check(k,arr,cost,d):
    N=len(arr)
    for i in range(0,k):
        d= d-max(0,cost[i]-arr[N-k+i])
        if d<0:
            return false
    return true

def maxCustomers(N, M, d, arr, cost):
    
    #sort the arrays
    arr.sort()
    cost.sort()

    l=0
    r=min(N,M)
    maxItem=0
    while(l<=r):
        mid=(l+r)//2
        
        if check(mid,arr, cost, d) :
            maxItem=mid
            l=mid+1
        else:
            r=mid-1
    #total money spent and maxItem baught
    sum=0
    for j in range(0,maxItem):
        sum = sum +cost[j]
    
    minMoney= max(0,sum-d)
    ans=[maxItem,minMoney]
    return ans

N, M, d = map(int ,input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))

out_=maxCustomers(N,M,d,arr,cost)
print(' '.join(map(str,out_)))


# #include<bits/stdc++.h>
# using namespace std;

# bool check(int k, vector<int> &arr, vector<int> &cost, int d) {
#     int N = arr.size();
#     for (int i = 0; i < k; ++i) {
#         d -= max(0, cost[i] - arr[N - k + i]);
#         if (d < 0)
#             return false;
#     }
#     return true;
# }

# vector<int> maxCustomers (int N, int M, int d, vector<int> arr, vector<int> cost) {
#     // Write your code here
#     sort(arr.begin(), arr.end());
#     sort(cost.begin(), cost.end());
#     int l = 0, r = min(N, M), maxItems = 0;
#     while (l <= r) {
#         int mid = (l + r) / 2;
#         if (check(mid, arr, cost, d)) {
#             maxItems = mid;
#             l = mid + 1;
#         } else {
#             r = mid - 1;
#         }
#     }

#     long long sum = 0;
#     for (int i = 0; i < maxItems; ++i) {
#         sum += cost[i];
#     }

#     int minMoney = max(0, sum - d);
#     vector<int> vec{maxItems, minMoney};
#     return vec;
# }

# int main() {

#     ios::sync_with_stdio(0);
#     cin.tie(0);
#     int N, M, d;
#     cin >> N >> M >> d;
#     assert(1 <= N && N <= 100000);
#     assert(1 <= M && M <= 100000);
#     assert(0 <= d && d <= 1000000000);
#     vector<int> arr(N);
#     for (int i_arr = 0; i_arr < N; i_arr++)
#     {
#         cin >> arr[i_arr];
#         assert(arr[i_arr] >= 1 && arr[i_arr] <= 10000);
#     }
#     vector<int> cost(M);
#     for (int i_cost = 0; i_cost < M; i_cost++)
#     {
#         cin >> cost[i_cost];
#         assert(cost[i_cost] >= 1 && cost[i_cost] <= 1000000000);
#     }
#     vector<int> out_;
#     out_ = maxCustomers(N, M, d, arr, cost);
#     cout << out_[0];
#     for (int i_out_ = 1; i_out_ < out_.size(); i_out_++)
#     {
#         cout << " " << out_[i_out_];
#     }
# }