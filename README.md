# Python example for OKCoin FIX api

This is a simple python example for OKCoin FIX API.

Since quickfix api for python does not support SSL as in java case, we should use manual tunneling using `stunnel`.

Because of that, the configuration file for quickfix api for using OKCoin should be slightly different from C# and Java case.  

**Note:** I'm using python 2.7

# Prerequisites
  1. `quickfix`
  2. ssh or ssl tunneling
    1. `openssh-server`
    2. `openssl` and `stunnel`
  
  **Note:** You can choose either ssh or ssl tunneling

# Install prerequisites
1. Install `quickfix` python api
  ```Shell
  pip install quickfix
  ```

2. Install ssh or ssl tunneling
  1. `openssh-server`
  ```Shell
  sudo apt-get install openssh-server
  ssh -L 9880:api.okcoin.cn:9880 username@<your ip address>
  ```
  2. Install `openssl` and `stunnel`
  
  See https://github.com/lim0606/python-okcoin-fix/tree/master/docs/stunnel


# Install this example
1. Download this repository
  ```Shell
  git clone https://github.com/lim0606/python-okcoin-fix.git
  ```

2. Set OKCoin API keys 
  1. Copy the example configuration file 
  ```Shell
  cp my_api.py.example my_api.py
  ```

  2. Change the below lines with your api keys
  ```
  api_key='your api key here'
  secret_key='your secret key here'
  ```

3. Set quickfix configuration file
  1. Copy the example configuration file
  ```Shell
  cp okcoin.cfg.example okcoin.cfg
  ```
  2. Open the configuration file
  ```Shell
  vim okcoin.cfg
  ```
  3. Change the line with the same used in tunneling (i.e. your ip address in this example)
  ```
  SocketConnectHost=Your ip address here
  ```
  
  **Note:** So this application communicates with OKCoin server via tunneling installed as prerequisites. That is why this setting is different from C# or Java example in OKCoin repo. 
  
  **Note:** We used `<your ip address>` in either `ssh`'s argument or `stunnel`'s configuration file 

  4. Change the line with user defined client name (e.g. generated using UUID)
  ```
  SenderCompID=SenderCompID user defined client name(e.g. generated using UUID)
  ```

4. Run  
  ```Shell
  python okcoin.py
  ```

**Note:** spec/FIX44.xml is copied from https://github.com/OKCoin/fix/blob/master/c%23/FixDemo/config/FIX44.xml

# References
1. https://github.com/tianyilai/QuickFix-python-client
2. https://futures.io/matlab-r-project-python/35213-python-quickfix.html
3. https://github.com/OKCoin/fix/blob/9e45e651cfada4a4c59cd51a40666cd33f22070b/java/src/com/okcoin/fix/OKClientApplication.java
4. https://github.com/OKCoin/fix/blob/85679c5f6793963c2bdaf03b72d6cb00d3b04cf7/c%23/FixDemo/bin/Debug/config/quickfix-client.cfg
