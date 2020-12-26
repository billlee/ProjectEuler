# find the value of n, 1 < n < 10^7 where 
# phi(n) is a permutation of n and the ratio 
# n/phi(n) produces a minimum
#
#
#
function isa_permutation(x::String, y::String)::Bool
    """
    Determines if two strings are permutations of each other
    """
    z = [false for i=1:length(y)]
    if length(x) != length(y)
        return false
    else 
        for j = 1:length(x)
            for k = 1:length(y) 
                if x[j] == y[k] && !z[k]
                    z[k] = true
                    break
                end 
            end 
        end 
    end 
    return all(z)
end 

function solve(max_number::Int32, primes::Array{Int64})::Int32
    """
    returns an array of the values of the totient 
    function to up the max number provided 
    """
    desired::Int32 = -1 # number which produces the max value
    mval::Float64 =  2147483647.0 # max value 
    totients = [0 for i = 1:max_number]

    # First store the primes and the prime powers
    for prime = primes
        totients[prime] = prime - 1
        k = 2; ppower = prime^k
        while ppower < max_number && ppower != 1
            totients[ppower] = ppower - (ppower/prime)
            k = k+1
            ppower = prime^k
        end 
    end 

    for t =  2:max_number
        totient = t 
        s = t
        p = 2
        if totients[t] != 0 
            continue
        end 

        while primes[p] <= s && p < length(primes)
            if s%primes[p] == 0  
                k = 1 
                while s%primes[p] == 0
                    s /= primes[p]
                    k = k+1
                end 
                ppower::Int32 = primes[p]^(k-1)
                quot::Int32 = s
                if gcd(quot, ppower) == 1  && quot != 1 
                    totients[t]  = totients[quot]*totients[ppower] 
                    break
                end 
                totient *= (1 - (1/primes[p]))
            end 
            p += 1
            totients[t] = round(totient)
        end 
        test::Int32 = round(totients[t])
        test = (test == t) ? test-1 : test

        if ((t/test) < mval ) && isa_permutation(string(test), string(t)) 
           desired = t
           mval = t/test
        end 
    end 
    return desired
end 

function sieve_of_erasthosenes(cap::Int32)::Array{Bool}
    """
    Returns a boolean of all the primes up to a certain 
    maximum number (cap)
    """
    A::Array{Bool} = [true for i = 1:cap]
    mx_check::Int32 = floor(sqrt(cap))
    for i = 2:mx_check
        if A[i] 
            k::Int32 = 0
            j::Int32 = i^2 + (k*i)
            while j <= cap 
                A[j] = false
                k = k+1
                j = (i^2) + (k*i)
            end 

        end 
    end 
    return A 
end 

function main()
    test_val = 10^7
    cap::Int32 = test_val
    primes = findall(x -> x == true, sieve_of_erasthosenes(cap))
    
    my_max::Int32 = test_val
    @time solve(my_max, primes)
end 

main()
