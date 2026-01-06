"# Ansible_Playbook_With_Sample_Python_Script" 

Prerequisites: 
1. An Ansible control node with Ansible installed.
2. A remote host (managed node) accessible via SSH, with Python installed (Ansible uses Python on managed nodes).
3. Passwordless SSH access configured between the control node and the remote host for seamless automation.


The `system_info.py` file gathers simple system information on the remote machine and prints it as a JSON format.

Make the `system_info.py` script executable on your local machine (ansible control node) using command `chmod +x system_info.py`

The `inventory.ini` file define the hosts you are targeting. Replace your_target_ip, your_username, and path/to/ssh/key with your actual details.

The ansible playbook `playbook.yml` file performs 3 main tasks:
1. Copies the Python script to a temporary location on the remote host.
2. Executes the script using a command module.
3. Registers the output and prints the JSON result using the debug module. 

To run this code, navigate to your project directory in your terminal and run the playbook using the ansible-playbook command: 

`
cd /ansible_playbook_with_python_script/ansible-playbook -i inventory.ini playbook.yml
`

Expected Output:

After running it will show the following output, with the final debug task displaying the structured JSON data gathered by the Python script: 


PLAY [Deploy and execute a system info Python script] ******************************************

TASK [Copy Python script to the remote machine] ********************************
changed: [webserver1]

TASK [Execute the script with a demonstration argument] ************************
changed: [webserver1]

TASK [Display the script's standard output (stdout)] ***************************
ok: [webserver1] => {
    "msg": {
        "arguments_received": [
            "arg1",
            "arg2"
        ],
        "machine": "x86_64",
        "node_name": "remote-server-hostname",
        "os": "Linux",
        "release": "5.15.0-101-generic",
        "version": "#111-Ubuntu SMP Fri Mar 15 16:47:08 UTC 2024"
    }
}

PLAY RECAP *********************************************************************
webserver1                 : ok=3    changed=2    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0

