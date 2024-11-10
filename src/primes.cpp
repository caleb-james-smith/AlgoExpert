// primes.cpp

// input:  integer representing maximum value (max_val)
// output: list of all primes p such that p <= max_val 

// Method 1:
// Number of divisors
//
// Create an output array.
// For each n <= max_val, find the number of divisors.
// If n has two divisors, then it is prime;
// append it to the output array.
// Return the output array.

// Method 2:
// Sieve of Eratothenese
//
// Create an array of length max_val + 1
// with every entry set to True.
// The indices of the array represent numbers,
// and the contents of the array are booleans (True, False)
// representing if the number is prime.
//
// Iterate through the indices of the array.
// For each index p, if the array contents are True,
// iterate over 2 * p to max_val and set array[p] to False.
//
// Then, create a new output array to fill with prime numbers.
// Iterate over the array of booleans,
// and for each entry that contains True,
// append the index to the output array.
// Return the output array.
//

#include <iostream>

std::vector<int> get_divisors(int n)
{
    std::vector<int> divisors;
    for (int i = 1; i <= n; i++)
    {
        if (n % i == 0)
        {
            divisors.push_back(i);
        }
    }
    return divisors;
}

int get_num_divisors(int n)
{
    std::vector<int> divisors = get_divisors(n);
    int num_divisors = divisors.size();
    return num_divisors;
}

void test_num_divisors(int max_val)
{
    for (int n = 1; n <= max_val; n++)
    {
        int num_divisors = get_num_divisors(n);
        printf("n = %d, num_divisors = %d\n", n, num_divisors);
    }
}

std::vector<int> get_primes_v1(int max_val)
{
    std::vector<int> output;
    for (int n = 1; n <= max_val; n++)
    {
        int num_divisors = get_num_divisors(n);
        // if n has two divisors, it is prime
        if (num_divisors == 2)
        {
            output.push_back(n);
        }
    }
    return output;
}

void printVector(std::vector<int> my_vector)
{
    printf("[");
    for (int i = 0; i < my_vector.size(); i++)
    {
        if (i == 0)
        {
            printf("%d", my_vector[i]);
        }
        else
        {
            printf(", %d", my_vector[i]);
        }
    }
    printf("]\n");
}

int main()
{
    int max_val = 100;
    
    //test_num_divisors(max_val);
    
    std::vector<int> primes_v1 = get_primes_v1(max_val);
    int n_primes_v1 = primes_v1.size();
    
    printf("primes_v1: ");
    printVector(primes_v1);
    printf("n_primes_v1: %d\n", n_primes_v1);
    
    return 0;
}

