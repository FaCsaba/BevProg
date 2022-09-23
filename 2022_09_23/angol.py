def main():
    c1 = """Totya is a hideous duck. His nose is enormous , his wings look terrible and he
            doesn't have any feather on his head. Even that Totya is always immaculate since
            he spends most of his time in water. It doesn't matter if his bath is freezing or
            boiling he takes a shower every day!"""

    li = list(c1.split())
    
    b1 = {
        "hideous": "very ugly",
        "enormous": "very big", 
        "terrible": "very bad", 
        "immaculate": "clean", 
        "freezing": "cold", 
        "boiling": "hot"
    }
    a = " ".join(map(lambda x: b1[x] if x in b1 else x, li))
    
    print(a)
    

if __name__ == "__main__":
    main()