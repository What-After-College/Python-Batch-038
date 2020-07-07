#include<bits/stdc++.h>
using namespace std;

int main()
{
    // int a[5] = {10,15,20,25,30};
    // int n = (1<<5);
    // int flag = 0;
    // for(int i=1; i<n; i++)
    // {
    //     int count = 0;
    //     int k = 0;
    //     int j = i;
    //     while(j)
    //     {
    //         if(j&1) count+=a[k];
    //         k++;
    //         j = j>>1;
    //     }

    //     if(count==68) 
    //     {
    //         flag = 1;
    //         break;
    //     }
    // }

    // if(flag) cout<<"YES"<<endl;
    // else cout<<"NO"<<endl;

    int a[10] = {1,2,3,4,5,7,4,3,2,1};

    int k = 0;

    for(int i=0; i<10; i++)
    {
        k^=a[i];
    }
    
    int j = 0;
    int temp = k;

    while (temp)
    {
        if(temp&1) break;
        j++;
        temp = temp>>1;
    }

    int un1=0;
    for(int i=0; i<10; i++)
    {
        if(a[i]&(1<<j)) un1^=a[i];
    }


    cout<<un1<<" "<<(k^un1)<<endl;
    return 0;
}