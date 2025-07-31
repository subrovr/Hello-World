#!/usr/bin/env python3
"""
Prime Number Generator
Generates all prime numbers between 1 and 100 using the Sieve of Eratosthenes algorithm.
"""

def sieve_of_eratosthenes(limit):
    """
    Generate prime numbers up to the given limit using the Sieve of Eratosthenes algorithm.
    
    Args:
        limit (int): The upper bound for prime number generation
        
    Returns:
        list: A list of prime numbers up to the limit
    """
    if limit < 2:
        return []
    
    # Create a boolean array "prime[0..limit]" and initialize all entries as True
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False  # 0 and 1 are not prime numbers
    
    p = 2
    while p * p <= limit:
        # If prime[p] is not changed, then it is a prime
        if prime[p]:
            # Update all multiples of p
            for i in range(p * p, limit + 1, p):
                prime[i] = False
        p += 1
    
    # Collect all prime numbers
    primes = []
    for i in range(2, limit + 1):
        if prime[i]:
            primes.append(i)
    
    return primes

def is_prime(n):
    """
    Check if a number is prime using trial division.
    
    Args:
        n (int): The number to check
        
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """Main function to generate and display prime numbers between 1 and 100."""
    print("Prime Numbers Between 1 and 100")
    print("=" * 35)
    
    # Generate primes using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(100)
    
    print(f"Found {len(primes)} prime numbers:")
    print()
    
    # Display primes in a formatted way (10 per row)
    for i, prime in enumerate(primes):
        print(f"{prime:3d}", end=" ")
        if (i + 1) % 10 == 0:
            print()  # New line after every 10 numbers
    
    if len(primes) % 10 != 0:
        print()  # Add final newline if needed
    
    print()
    print(f"The largest prime number ≤ 100 is: {max(primes)}")
    print(f"The smallest prime number is: {min(primes)}")
    
    # Demonstrate the alternative is_prime function
    print("\nVerification using alternative method:")
    verification_primes = [n for n in range(1, 101) if is_prime(n)]
    print(f"Alternative method found {len(verification_primes)} primes")
    print(f"Both methods agree: {primes == verification_primes}")

if __name__ == "__main__":
    main()