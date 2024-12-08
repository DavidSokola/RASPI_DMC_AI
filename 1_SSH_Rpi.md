## 1.Prepare Your Raspberry Pi

Enable SSH:
Open a terminal on the Raspberry Pi.
Run the command:

```console
sudo systemctl enable ssh
sudo systemctl start ssh
```

Find the IP address of the Raspberry Pi:

        
```console
hostname -I
```

Find raspberry IP adress

```console
ifconfig
```

*Install Development Tools (if required):
Update the system and install necessary tools like Python, Node.js, or any other environment your project needs.*

## 2.Install Visual Studio Code

Download and install Visual Studio Code on your local machine.

## 3.Install the Remote-SSH Extension in VS Code

Open VS Code.
Go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side or pressing *Ctrl+Shift+X*
Search for Remote - SSH and install it.

## 4.Set Up an SSH Configuration

In VS Code, press Ctrl+Shift+P (or Cmd+Shift+P on Mac) to open the Command Palette.
Type Remote-SSH: Add New SSH Host and press Enter.
Enter your Raspberry Pi's SSH connection string in the format:

```console
pi@<Raspberry_Pi_IP>
```

Replace <Raspberry_Pi_IP> with the IP address of your Raspberry Pi.
Choose the SSH configuration file where you want to save this connection (usually ~/.ssh/config).
If prompted, enter the Raspberry Pi password.

## 5.Connect to the Raspberry Pi

Press Ctrl+Shift+P and type Remote-SSH: Connect to Host.
Select your Raspberry Pi from the list of configured hosts.
VS Code will open a new window connected to the Raspberry Pi. You can now interact with it as if you're working on the Pi directly.

## 6.Set Up and Test Your Environment

Open or create a new folder on the Raspberry Pi by using the File Explorer.
Install any required extensions for your programming language (e.g., Python, C++, etc.). VS Code will prompt you to install the necessary server-side extensions when you open a project.

## 7.  Write and Run Programs

Use the integrated terminal (`Ctrl+```) to execute commands directly on the Raspberry Pi.
Test your programs as you would locally. For instance, for Python scripts, run:

  `  python3 your_script.py`

For Node.js, C++, or other languages, configure the build/run tasks as required.

## 8. Debug Remotely (Optional)

Set up breakpoints and launch the debugger in VS Code.
Ensure that the required debugging tools are installed on the Raspberry Pi (e.g., gdb for C++, Python debugger for Python).

Additional Tips:

Transfer Files: You can use VS Code's file explorer to drag and drop files between your local machine and Raspberry Pi.
Optimize SSH: If you frequently reconnect, set up an SSH key-based authentication for convenience. Generate a key pair on your local machine with ssh-keygen and copy the public key to the Raspberry Pi using ssh-copy-id.

This setup allows seamless coding, testing, and debugging on your Raspberry Pi from your local machine using VS Code.
