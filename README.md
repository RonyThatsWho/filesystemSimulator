# **Simulated Linux File System in Python**

In this project I attempt to emulate 4 core functions of linux file system browsing
> 	**ls**, **mkdir**, **cd** and **touch**


In this rendition all manipulations are done in memory with mock files/folders. 
Actual OS file system is not used for this task.



# **Additional Commmands**

```
clear - will clear all files and folder. Only singular "root" folder remains
```
```
quit - no longer taking input and terminates python aplication
```


# **Test Cases**

Attempt to create duplicate folders
```
mkdir test
mkdir test
```


Try to cd into file
```
touch file
cd file
```


navigate to root using singular "/"

```
mkdir test
cd test
mkdir test
cd test
mkdir test
cd test
cd /
```


Test cd and ".." functionality

```
mkdir test
cd test
mkdir test
cd test
cd ..
cd test
cd ../../test
```


verify ls folder and file differentiation and alphabatical order

```
touch zeta
mkdir alpha
touch beta
mkdir 300
touch 7
ls
```


# **To Do**
- [ ] import test case text files 
- [ ] make directory in specific file path

