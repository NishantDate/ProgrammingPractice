# You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

# Implement the BrowserHistory class:

#     BrowserHistory(string homepage) Initializes the object with the homepage of the browser.

#     void visit(string url) Visits url from the current page. It clears up all the forward history.

#     string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.

#     string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

# Examples:

class DoubleLL:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(DoubleLL):
    def __init__(self, homepage):
        self.history = DoubleLL(homepage)
    def visit(self,newpage):
        self.history.next = DoubleLL(newpage,prev = self.history)
        self.history = self.history.next
        return f"Currently at {self.history.prev.val}, going to {self.history.val}"
    def back(self, n = 1):
        print(f"going back {n}")
        for i in range(n):
            if self.history.prev:
                self.history = self.history.prev
            else:
                return f"History depth reached. Last website is {self.history.val}"
        return f"We're arrived at {self.history.val}"
    def forward(self, n = 1):
        print(f"going forward {n}")
        for i in range(n):
            if self.history.next:
                self.history = self.history.next
            else:
                return f"Forward depth reached. Last website is {self.history.val}"
        return f"We're arrived at {self.history.val}"
    def getCurrPage(self):
        return self.history.val
browserhistory = BrowserHistory("leetcode.com")
print(browserhistory.visit("google.com"))
print(browserhistory.visit("youtube.com"))
print(browserhistory.visit("facebook.com"))
print(browserhistory.back(3))
print(browserhistory.back())
print(browserhistory.getCurrPage())

