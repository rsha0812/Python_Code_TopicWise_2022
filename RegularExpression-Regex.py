### Regex: --- Udemy 
## Qn : To match the word "Bitcoin" at the beginning of string.
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.match("Bitcoin",s)
print(result.group())

## Qn: To match the word "Bitcoin" at the beginning of string by ignoring the case (Upper/Lower).
## Soln: 
#re.I is a flag that ignores the case of the matched characters
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.match("bitcoin",s,re.I)
print(result.group())

## Qn: To match the word "Bitcoin" at the beginning of string by using (.) belonging to regex syntax: 
### Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.match(r"B.{6} .{3}", s)
print

## Qn: Write the code to match 2009 in the string 
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"(\d{4})\s", s)
print(result.group(1))
 '''
 Analysis: 
\d : Returns a match where the string contains digits (numbers from 0-9)
{} : Exactly the specified number of occurrences ({4} in this eg.)
\s : Returns a match where the string contains a white space character
'''
## Qn : To match Jan 3rd 2009 in the string using search()
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"(.{3}\s\d\w\w\s\d{4})\s", s)
print(result.group(1))

## Qn : To match BTC in the string using search()
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"([A-Z]{3})", s)
print(result.group(1))

## Qn: To match 1BTC in the string. 
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"([0-9]\s[A-Z]{3})", s)
print(result.group(1))

## Qn: To Match in the string. 
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B."
result = re.search(r"(\$\d{5}),", s) ## for searching $20000
result = re.search(r"(\$\d{3}[A-Z])\.", s) ### For searching $300B 
result = re.search(r"\s(.{6} .{3} .{2})\s", s) ### To match market cap of 
### Analysis: {6} - market; {3} - cap; {2} - of 
print(result.group(1))

## Qn : To match 184,073,529,068 in string.
## Soln: 
import re

s = "Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
result = re.search(r"\$(\d{3},[0-9]{3},\d{3},[0-9]{3}),", s)
result = re.search(r"\$(\d{1,3},\d{1,3}\.\d{1,3}),", s) ## 10,259.02
result = re.search(r"\s(.{4}\s\d\.\d\d%)", s) ## 24h: 0.10%
print(result.group(1))

## Qn: To relace all years with XXXX in the string. 
### Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
result = re.sub(r"\s\d{4}", " XXXX", s)
print(result)

## Qn: To replace floating Point number with dot(.). 
## Soln:
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
result = re.sub(r"\d{1,},*\d*\.\d{1,}", ".", s)
print(result)

## Qn: To replace all occurence of BTC in string with Bitcoin using sub().
## Soln:
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
result = re.sub(r"[A-Z]{3}", "Bitcoin", s)

## Qn: Relace all words starting with Upper Case letter or digits greater than or equal to 6 in the string with W. 
## Soln: 
import re
s = "Bitcoin was born on Jan 3rd 2009 as an alternative to the failure of the current financial system. In 2017, the price of 1 BTC reached $20000, with a market cap of over $300B. Bitcoin, Market Cap: $184,073,529,068, Price: $10,259.02, Volume 24h: $15,670,986,269, Circulating Supply: 17,942,600 BTC, Change 24h: 0.10%"
result = re.sub(r"[A-Z]\w{1,}|[6-9]", "W", s)
print(result)