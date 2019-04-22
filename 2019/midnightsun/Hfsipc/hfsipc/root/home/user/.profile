export HOME=/home/user
export USER=user
export PATH=/bin:/usr/bin

COLOR="34"
cd /home/user
export PS1="\e[01;${COLOR}m$(whoami)@hfs\[\033[00m\]:\[\033[36m\]\w\[\033[00m\]\$ "
