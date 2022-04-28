### Connect to server and setup

```shell
ssh connection: ssh cloud_user@8482a3512d1c.mylabserver.com
commands:
yum groupinstall -y "development tools"
yum install -y lsof wget vim-enhanced words which
yum install -y \
libffi-devel zlib-devel bzip2-devel openssl-devel ncurses-devel \
sqlite-devel readline-devel tk-devel gdbm-devel db4-devel xzdevel \
libpcap-devel expat-devel
pip3.6 install --upgrade pip
```

### Set bashrc

```sh
curl -o ~/.bashrc https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/bashrc
curl -o ~/.vimrc https://raw.githubusercontent.com/linuxacademy/content-python3-sysadmin/master/helpers/vimrc
```

### Configure and create local git repo

```shell
git config --global user.name "Wilton Paulo"
git config --global user.email "wiltonpaulo@gmail.com"

mkdir sample
cd sample
touch file.txt
git init
git add --all .
git commit -m "Added new file"
```

### Install and remove pip packages

```sh
pip3 install packagename
pip3 list
pip3 freeze > requirements.txt
pip3 uninstall -y -r requirements.txt
pip3 install --user -r requirements.txt
```

# virtualenvs with python3

```sh
mkdir venvs
python3 -m venv venvs/experiment
source venvs/experiment/bin/activate
```

\*\* remember to add "venvs" dir to .gitignore

### Additional materials

https://github.com/linuxacademy/content-python3-sysadmin/tree/master/helpers

```

```
