def fibonnacci(n):
    """returns the nth fibonnacci number"""
    
    if n <= 1:
        return n
    else:
        return(fibonnacci(n-2) + fibonnacci(n-1))

if __name__ == '__main__':
    print(fibonnacci(6))