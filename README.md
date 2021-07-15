# ida-swift-demangle
A tool to demangle Swift function names in IDA.

You can use it in Mac's IDA Pro 7.0

## How to use
```bash
git clone https://github.com/paradiseduo/ida-swift-demangle.git
cd ida-swift-demangle
sudo mv swift.py /Applications/IDA\ Pro\ 7.0/ida.app/Contents/MacOS/plugins/
```
Open IDA Pro 7.0, Edit->Plugin->Swift Dump
![image](https://user-images.githubusercontent.com/14846965/125758923-f705d5c9-f319-40f9-8a38-15ac43626e7c.png)

### Before:

![image](https://user-images.githubusercontent.com/14846965/125759910-e1a52ab1-1739-4bdd-90e7-4458a18a9a17.png)

### After:

![image](https://user-images.githubusercontent.com/14846965/125760061-9d6a82e8-ca76-40f7-9638-2a762aa5696a.png)

### Original:

![image](https://user-images.githubusercontent.com/14846965/125760177-5a974913-3cff-4868-b1a8-22dc9af89027.png)
![image](https://user-images.githubusercontent.com/14846965/125760224-75cc08d8-991e-4bc8-a3e1-453168481132.png)


## Required
MacOS and install Xcode.app
