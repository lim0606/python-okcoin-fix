# Introduction
Since quickfix api for python does not support SSL as in java case, we should use manual tunneling using `stunnel`. 

This is how I configured. 

# Setting stunnel
1. Install `openssl`
  ```Shell
  sudo apt-get install openssl
  ```

2. Generate SSL certificate, which will be used by `stunnel`
  ```Shell
  openssl genrsa -out key.pem 2048
  openssl req -new -x509 -key key.pem -out cert.pem -days 1095
  cat key.pem cert.pem >> stunnel.pem
  ```
  **Note:** This generated `.pem` file will be moved to `/etc/stunnel/`

3. Install `stunnel`
  ```Shell
  sudo apt-get update
  sudo apt-get install stunnel4
  ```

4. Enabling `stunnel`
  1. Open `stunnel`'s setting file
   ```Shell
   sudo vim /etc/default/stunnel4
   ```
  2. Change the line,
   ```
   ENABLED=0
   ```
   to 
   ```
   ENABLED=1
   ```

5. Move the above `.pem` file to `/etc/stunnel/`
  ```Shell
  sudo mv stunnel.pem /etc/stunnel/.
  ```
  
6. Make a configuration file of `stunnel`
  1. Stunnel configures itself using a file named "stunnel.conf" which by default is located in "/etc/stunnel".
     Create a "stunnel.conf" file in the "/etc/stunnel" directory:

     ```Shell
     sudo vim /etc/stunnel/stunnel.conf
     ```
  2. Add the below lines in the created file 
     ```
     client = yes
     cert = /etc/stunnel/stunnel.pem

     [OKSERVER]
     accept = <your id address>:9880
     connect = api.okcoin.cn:9880
     ```

    **Note:** `<your id address>` can be found via `ifconfig

  **Note:** The resulting configuration file may look like https://github.com/lim0606/python-okcoin-fix/blob/master/stunnel.conf.example

7. Run `stunnel`
  ```Shell
  sudo stunnel4
  ```

# References
1. http://www.cnblogs.com/li-dp/p/4720764.html
2. https://waiseekweng.wordpress.com/2014/09/08/configure-for-fixn/
3. https://www.digitalocean.com/community/tutorials/how-to-set-up-an-ssl-tunnel-using-stunnel-on-ubuntu
4. http://www.ubuntugeek.com/stunnel-universal-ssl-tunnel-for-network-daemons.html
