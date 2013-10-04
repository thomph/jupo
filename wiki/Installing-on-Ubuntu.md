Install `jupo` on server [Ubuntu 12.04](http://releases.ubuntu.com/)

### Preparations  
You will need to make sure that your username is on the sudo authorized list located at '/etc/sudoers'  
```
sudo apt-get update  
```

## Step 1  
**Install the required packages** 
``` 
sudo apt-get install unzip vim curl vim build-essential git libpcre3-dev libssl-dev python-dev libevent-dev python-setuptools libxslt-dev python-gevent python-virtualenv  
sudo apt-get build-dep python-imaging
```

## Step2  

### Dependencies  

**MongoDB**  

[http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/)  
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10  
echo "deb http://downloads-distro.mongodb.org/repo/ubuntu-upstart dist 10gen" | tee -a /etc/apt/sources.list.d/10gen.list  
sudo apt-get update  

sudo apt-get install mongodb-10gen  
```

Stop `mongodb`  
```
sudo /etc/init.d/mongodb stop  
```

This MongoDB instance will store its data files in the `/data/mongo` and its log files in `/var/log/mongo`  
```
mkdir /var/log/mongo  
mkdir -p /data/mongo  
chown mongodb:mongodb /data/mongo  
```

**Nginx** 

Get the sources (check [nginx page](http://nginx.org/en/download.html) before downloading, there might be a newer version available):
```
wget http://nginx.org/download/nginx-1.2.8.tar.gz  
tar xvzf nginx-1.2.8.tar.gz  
wget https://github.com/agentzh/headers-more-nginx-module/archive/v0.21.zip  
unzip v0.21  
cd nginx-1.2.8  
./configure --with-http_ssl_module --with-http_stub_status_module --add-module=../headers-more-nginx-module-0.21  
make && make install  
cp /usr/local/nginx/sbin/nginx /usr/sbin/  
```

Create folder log `/var/log/nginx/`  
```
mkdir /var/log/nginx/  
```
Create user `nginx`  
```
useradd nginx
```

**Memcached**

```
sudo apt-get install memcached 
```

Create user `memcached`
```
useradd memcached
```

Stop process  
```
sudo /etc/init.d/memcached stop
```

Disable auto start  
```
update-rc.d memcached disable
```

**Redis**

```
sudo apt-get install redis-server
```

Stop process  
```
sudo /etc/init.d/redis-server stop
```

Disable auto start  
```
update-rc.d redis-server disable
```

**ElasticSearch**

Install `java jdk`  
```
sudo apt-get install openjdk-7-jre
```

Install `elasticsearch`, check [elasticsearch page](http://www.elasticsearch.org/download/)  
```
wget https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-0.20.6.tar.gz  
tar -xzf elasticsearch-* && rm elasticsearch-*.tar.gz  
mv elasticsearch-* /usr/local/elasticsearch  
mkdir /data/elasticsearch  
```

Create `/etc/elasticsearch/elasticsearch.yml`  
> cluster:  
>        name:    jupo  
> network:  
>        bind_host:    127.0.0.1  

**Supervisor**
```
sudo curl https://raw.github.com/gist/176149/88d0d68c4af22a7474ad1d011659ea2d27e35b8d/supervisord.sh > /etc/init.d/supervisord  
file=/etc/init.d/supervisord  
mv ${file} ${file}.bak  
sed 's/^DAEMON_ARGS=""$/DAEMON_ARGS="-c\ \/home\/Workspace\/jupo\/conf\/supervisord.conf"/g' ${file}.bak > ${file}  
chmod +x ${file}  
```

## Step 3

### JUPO

Synchronize the system clock  
```
sudo apt-get install ntp ntpdate  
ntpdate 0.pool.ntp.org  
```

Create folder `jupo` log `/var/log/jupo/`  
```
mkdir /var/log/jupo  
```

**Install `virtualenv`**  
```
easy_install virtualenv pip  
```

**Clone project from `github`**  
```
mkdir -p /home/Workspace/  
cd /home/Workspace/  
git clone git://github.com/juposocial/jupo.git  
cd jupo  
git checkout develop  
```

**Install requirements**  
```
cd jupo  
virtualenv env  
source env/bin/activate  
pip install -r requirements.txt  
easy_install ordereddict  
```

Edit config file  
```
cp src/settings.example.py src/settings.py  
```
Change   

>`PRIMARY_DOMAIN`: Your domain  
>`EMAIL_REPLY_TO_DOMAIN`: Email domain  
>`SECRET_KEY`: Your secret key  
>`SMTP`: Fill infomation your `smtp` service, you can use [mandrillapp](http://mandrill.com/)  
>`AWS`: Use Amazon's AWS S3 file-storage service to store static and uploaded files  
>`GOOGLE`/`FACEBOOK`: [Login with Google/Facebook](https://github.com/juposocial/jupo/wiki/Create-App-Facebook-Google)  

Add line to file `/etc/hosts`  
Your_Ip    Your domain  

**Run process use `supervisord`**  
```
. env/bin/activate  
supervisord -c conf/supervisord.dev.conf  
```

Show status process  
```
supervisorctl -c conf/supervisord.dev.conf  
supervisor> status  
```