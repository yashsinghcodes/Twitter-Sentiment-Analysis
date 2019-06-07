# Twitter-Sentiment-Analysis
Twitter Sentiment Analysis is a sime python module or file which help in analyse the public tweets on a paticular topic. 
To set up:

## Installation of Libraries
It's recommended that you use virtualenv so that existing packages aren't tempered with. You'll need Python 3 installed with pip.
Run:
`pip install tweepy`

`pip install textblob`

`pip install csv`

`pip install os`

## How to use
I made a file name main you can put it in your site packages or in the same folder. To locate your site-packages Run the following commands in your terminal:

`$ python`

Next, import the `sys` module:

`>>> import sys`

Then have Python print out the system path:

`>>> print(sys.path)`

Here, you’ll receive some output with at least one system path. If you’re in a programming environment, you may receive several. You’ll want to look for the one that is in the environment you’re currently using, but you may also want to add the module to your main system Python path. What you’re looking for will be similar to this:

`'/usr/sammy/my_env/lib/python3.5/site-packages'`

If you are putting it in the same folder then you can directly call it by:

`import main`

OR

`from main import TSA`

## Examples

```python
from main import TSA

twitter = TSA('Your API Key',' Your API secret key','Your Access token','Your Access Token Secret')
twitter.analysis('Apple')
```
