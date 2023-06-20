class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author == self]
    
    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        return contract
    
    def total_royalties(self):
        return sum([contract.royalties for contract in Contract.all if contract.author == self])



class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]



class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        if isinstance(author, Author):
            self.author = author
        else:
            raise Exception("Invalid author")
        if isinstance(book, Book):
            self.book = book
        else:
            raise Exception("Invalid book")
        if isinstance(date, str):
            self.date = date    
        else: raise Exception("Invalid date")
        if isinstance(royalties, int):
            self.royalties = royalties
        else: raise Exception("Invalid royalties")
        self.all.append(self)
        
    @classmethod
    def contracts_by_date(cls):
        return sorted(cls.all, key=lambda contract: contract.date)

